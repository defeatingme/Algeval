from openai import OpenAI
from pydantic import BaseModel
from PySide6.QtCore import QObject


client = OpenAI()
    

class ASM_Recommendation(BaseModel):
    alternative_solution: str
    steps_count: int
    


class Recommendation(QObject):  # Now inherits QObject for PySide6 compatibility
    def __init__(self, ak_latex, steps_count):
        super().__init__()  
        
        self.conversation = [
                {"role": "system", "content": (r"""
You are an expert in generating step-by-step Alternative Solution Methods (ASM) for algebraic problems based on the given Answer Key (AK). 
Ensure the ASM remains mathematically valid and leads to the same result as the AK despite the different step-by-step approach.
Count the number of solution steps in the ASM. These are each of the lines excluding the problem setup, redundant duplicates, and the final answer.
Needless to state anything else, such as explanations, justifications, and grading.
Maintain proper mathematical notation using delimiters '\[...\]' to ensure MathJax rendering.
        """)}]

        self.ak_latex = ak_latex
        self.steps_count = steps_count


    def recommend(self, request):
        prompt = f"AK: SOL = {self.steps_count} steps\n\n'{self.ak_latex}'\n\n\nASM Request: {request}"

        # Add HAS input to conversation
        self.conversation.append({"role": "user", "content": prompt})
        print(self.conversation)

        # Get GPT response
        self.result = self.getResponse()
        
        #reset conv
        self.conversation = self.conversation[:1]

        print("GPT:", self.result)

        return self.result


    def getResponse(self):
        # Send conversation to GPT model and parses the structured response
        completion = client.beta.chat.completions.parse(
        model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::BFZWjNAX",
        messages=self.conversation,
        temperature=0.2,
        response_format=ASM_Recommendation,
        store=True
        )
        event = completion.choices[0].message
        return event