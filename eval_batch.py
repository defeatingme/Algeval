from openai import OpenAI
from pydantic import BaseModel
from typing import Optional

from PySide6.QtCore import QObject
from database import Session, AnswerKey


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
        self.slice_batch = 0
        
        self.fetchAnswerKey()
        
    def fetchAnswerKey(self):
        session = Session()  # Open a new session
        try:
            # Query all AnswerKey entries linked to the session_id
            ak_entries = session.query(AnswerKey).filter(AnswerKey.session_id == self.session_id).all()

            # Extract IDs and store answer key data
            self.ak_ids = [ak.id for ak in ak_entries[:2]]
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


    def evaluate(self, output):
        print(":33")
        self.output = output
        
        all_results = []  # List to store the results for each image
        print(self.output)
        
        i = self.slice_batch  # Start from where we left off
        while i < len(self.output):
            image_result = self.output[i]

            has_latex = "\n\n\n".join(
                f"{j+1}. {item.get('problem_setup', '_')}\n" + item.get('expressions', 'No solution')
                for j, item in enumerate(image_result.get('result', {}).get("full_solutions", []))
            )
            print(has_latex)
            print(":33")

            # Evaluate HAS and ensures first ASM stays in conversation permanently
            ak_sections = []
            for j, ak in enumerate(self.ak_data, start=1):
                ak_section = (
f"""### AK {j}:\n
SOL = {ak['steps']} steps, {ak['sol_weight']}% weight; FA = {ak['fa_weight']}%

'{ak['ak_latex']}'\n

User Choice:
{ak['asm_choice']} and refrain from asking for user confirmation regarding it.
"""
                )
                ak_sections.append(ak_section)
            
            prompt = f"\n{'\n\n'.join(ak_sections)}\n---\n\n### HAS: '{has_latex}'"

            # Add HAS input to conversation
            self.conversation.append({"role": "user", "content": prompt})
            print(prompt)

            # Get GPT response
            self.result = self.getResponse()
            if self.result is None:
                # Resetting function:
                print(f"Result type: {type(self.result)}")

                print(f"resetting for HAS {i+1}...")
                self.slice_batch = i  # Remember where we are
                # Don't recursively call evaluate; we'll retry this item in the next iteration
                continue

            self.conversation.append({"role": "assistant", "content": str(self.result)})

            print("GPT:", self.result)
            
            self.conversation = self.conversation[:1] # save asm conversation
            
            print(self.conversation)
            
            # Optionally, save the result in the all_results list
            has_result = {
                "has_latex": has_latex,
                "gpt_response": str(self.result),  # Store the stringified GPT response
            }
            all_results.append(has_result)
            print(has_result)

            i += 1
    
        print("\n", all_results)
        return all_results


    def getResponse(self):
        try:
            client = OpenAI()

            # Sends conversation to GPT model and parses the structured response.
            completion = client.beta.chat.completions.parse(
            model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::BFZWjNAX",
            messages=self.conversation,
            temperature=0.2,
            response_format=AssistantResponse,
            store=True,
            timeout=17,
            )
            event = completion.choices[0].message.parsed
            return event
        except Exception as e:
            print(f"Error in API call: {e}")
            return None
