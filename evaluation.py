from openai import OpenAI
from pydantic import BaseModel
from typing import Optional
from PySide6.QtCore import QObject, Signal
from database import Session, AnswerKey


client = OpenAI()


class SolutionGrade(BaseModel):
    correct_steps: int
    total_steps: int
    weight: int
    sol_grade: int


class ProblemResponse(BaseModel):
    problem_number: int 
    problem: str
    ask_to_allow_asm: Optional[str] = None
    result: str
    employed_asm: Optional[bool]
    sol_calculation: Optional[list[SolutionGrade]]
    fa_grade: Optional[int]
    overall_grade: Optional[int]

    
class AssistantResponse(BaseModel):
    problems: Optional[list[ProblemResponse]]
    no_HAS_message: Optional[str] = None

    

class Evaluation(QObject):  # Now inherits QObject for PySide6 compatibility
    ask_asm_signal = Signal(object)  # Signal to ask main thread for ASM choice
    asm_response_signal = Signal(str)  # Signal to receive ASM response
    evaluation_done_signal = Signal(object)

    def __init__(self, session_id):
        super().__init__()  
        
        self.conversation = [
                {"role": "system", "content": ("""
You are an expert at grading HAS (Handwritten Algebraic Solutions) step-by-step based strictly on the Answer Key (AK).
Grade = Solution (SOL) % + Final Answer (FA) %. FA is the last and not a SOL step. Deduct SOL points for each missing or wrong step; accept redundancy and partial simplifications of a step. Ignore the first line(s) in the HAS if it is also first in the AK, as it is the algebraic problem setup. Use formula: (C/T)W for SOL grading, where C = correct SOL steps from HAS aligned with AK counterpart, T = total SOL steps from AK, and W = SOL weight.
If the HAS employs an Alternative Solution Method (ASM) different from the AK, state: 'The solution has an Alternative Method used... Do you want to allow it? (Yes/No)' and wait for user confirmation before grading. If allowed: alter T in SOL formula to total steps in the HAS instead of the AK, and C to simply correct steps. Refrain from asking again for subsequent HAS with similar ASM, or if the user forbid ASMs.
For the result, briefly state the Problem from the AK, and if a step is Correct or not. Display Grade as: 'Solution = (substituted formula) = #%,\nFinal Answer = #%,\nGrade = #%'. If the HAS has no SOL or fails support any requirement to solve the problem(s), state in the result: 'There is no provided solution aiming to...'.
Always use delimiters to help MathJax render mathematical content.
                """)}]

        self.session_id = session_id
        
        self.ak_count = 0
        self.num_of_asm = 0  # Store first ASM message permanently
        self.prev_num_of_ask = 0
        self.saved_conv = 1

        self.fetchAnswerKey()


    def fetchAnswerKey(self):
        session = Session()  # Open a new session
        try:
            # Query all AnswerKey entries linked to the session_id
            ak_entries = session.query(AnswerKey).filter(AnswerKey.session_id == self.session_id).all()

            # Extract IDs and store answer key data
            self.ak_ids = [ak.id for ak in ak_entries]
            self.ak_count = len(self.ak_ids)

            self.ak_data = [
                {
                    "steps": ak.steps_count,  # Estimate steps from LaTeX lines
                    "sol_weight": ak.sol_weight,
                    "fa_weight": ak.fa_weight,
                    "ak_latex": ak.ak_latex,
                    
                    "asm_steps": ak.asm_steps if ak.asm_steps else None,
                    "asm_latex": ak.asm_latex if ak.asm_latex else None,
                    "asm_choice": ak.asm_choice if ak.asm_choice else None,
                    
                }

                for ak in ak_entries
            ]

            print(f"Found {self.ak_count} Answer Keys for session {self.session_id}: {self.ak_ids}")

        except Exception as e:
            print(e)
        finally:
            session.close()  # Close the session

    def evaluate(self, has_latex):
        self.has_latex = has_latex

        # Evaluate HAS and ensure ASM stays in conversation permanently
        ak_sections = []
        for i, ak in enumerate(self.ak_data, start=1):
            if not ak['asm_latex']:
                ak_section = (
f"""### AK {i}:\n
SOL = {ak['steps']} steps, {ak['sol_weight']}% weight; FA = {ak['fa_weight']}%

'{ak['ak_latex']}'
"""
                )
            else:
                ak_section = (
f"""### AK {i}:
SOL = {ak['steps']} steps, {ak['sol_weight']}% weight; FA = {ak['fa_weight']}%

'{ak['ak_latex']}

ASM for AK {i}: 
SOL = {ak['asm_steps']}

'{ak['asm_latex']}'
    
User Choice:
{ak['asm_choice']} and refrain from asking for user confirmation regarding it.
"""             
                )
            
            ak_sections.append(ak_section)
            
        prompt = f"\n{'\n\n'.join(ak_sections)}\n---\n\n### HAS: '{self.has_latex}'"
        print(prompt)
        # Add HAS input to conversation
        self.conversation.append({"role": "user", "content": prompt})

        # Get GPT response
        self.result = self.getResponse()
        self.conversation.append({"role": "assistant", "content": str(self.result)})

        print("\nGPT:", self.result)
        
        if self.result.problems:
            #check if problems exists
            for problem in self.result.problems:
                #IF HAS has ASM:
                if problem.ask_to_allow_asm:
                    self.num_of_asm += 1
                    print("ASM confirmation... Keeping conversation history.")
                    self.ask_asm_signal.emit(problem)  # Emit signal to main thread
                    
                    # Do NOT continue evaluation until user responds
                    return None
                    
                    #IF 2ND ONWARDS            
                #IF HAS FOLLOWS AK
                else:
                    #  Reset conversation but keep ASM user choice, and its result if it exists
                    print("HAS follows Answer Key method. Resetting conversation.")
                    if self.prev_num_of_ask == self.num_of_asm:
                        self.conversation = self.conversation[:self.saved_conv] # Reset to only system message or previous saved conv
                    else:
                        self.saved_conv += 4
                        self.conversation = self.conversation[:self.saved_conv] # save asm conversation
                        self.prev_num_of_ask = self.num_of_asm
        else:
            self.conversation = self.conversation[:self.saved_conv] # save asm conversation
        
        print(self.conversation)
        return self.result


    def getResponse(self):
        # Send conversation to GPT model and parse structured response.
        completion = client.beta.chat.completions.parse(
        model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::BFZWjNAX",
        messages=self.conversation,
        temperature=0.2,
        response_format=AssistantResponse,
        store=True
        )
        event = completion.choices[0].message.parsed
        return event
    

    def handleASM1(self, user_choice):
        # Handle ASM user choice from main thread
        self.user_choice = user_choice
        print(f"Received user choice from GUI: {self.user_choice}")

        self.conversation.append({"role": "user", "content": self.user_choice})

        #  Get assistant's final grading response for this HAS
        self.result = self.getResponse()
        self.conversation.append({"role": "assistant", "content": str(self.result)})
        
        print("\nGPT:", self.result)

        print(self.conversation)
        return self.result