import base64
from openai import OpenAI
from pydantic import BaseModel
from typing import Optional

client = OpenAI()

class Solution(BaseModel):
    problem_setup: Optional[str]
    expressions: Optional[str]

class OCRResponse(BaseModel):
    name: Optional[str]
    full_solutions: Optional[list[Solution]]
    steps_count: int
    empty_message: Optional[str] = None

    
class SimulateOCR():
    def __init__(self, image):
        super().__init__()  
        self.image = image
        self.base64_image = None
        
        self.conversation = [
            {"role": "system", "content": (r"""
You are an expert at Optical Character Recognition (especially in handwritten characters), only generating the extracted text from the image and nothing else
Extract the full step-by-step math solution exactly as shown in the image, including mistakes in the solution. Do not omit any numbers or symbols.
If included in the image, also extract the name of the writer of the solution, typically at the top left of the image.
Include the full mathematical problem setup (statement + equation) if visible
Use well documented and DOUBLE BACKLASHED latex code starting and ending each line with delimiters '\[...\]' specifically. NOT '$...$'
Identify the problem equation separately if possible. If not, assume the first expression is the problem equation. 
Count the number of solution steps. These are the expressions excluding the problem equation, redundant duplicates, and the final answer.
Final answers are typically boxed and the last line of solutions
There are instances of multiple solutions in an image. Thus, separately list them
        """)}]
        
        self.simulate()


    def simulate(self):  
        with open(self.image, "rb") as image_file:
            self.base64_image = base64.b64encode(image_file.read()).decode("utf-8")
      
        prompt = {"role": "user","content": [{
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{self.base64_image}",
            }]}
        # Add HAS input to conversation
        self.conversation.append({"role": "user", "content": prompt})

        # Get GPT response
        self.output = self.getResponse()
        
        print(self.conversation)
        #Reset Conversation
        self.conversation = self.conversation[:1]
        
        return self.output


    def getResponse(self):
        completion = client.beta.chat.completions.parse(
            model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::BFZWjNAX",
            messages=self.conversation,
            temperature=0.2,
            response_format=OCRResponse,
            store=True
        )
        event = completion.choices[0].message.parsed
        return event
    