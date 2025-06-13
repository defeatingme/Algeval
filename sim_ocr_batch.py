import base64
import os
from openai import OpenAI
from pydantic import BaseModel
from typing import Optional


class Solution(BaseModel):
    problem_setup: Optional[str]
    expressions: Optional[str]


class OCRResponse(BaseModel):
    name: Optional[str]
    full_solutions: Optional[list[Solution]]
    steps_count: int
    empty_message: Optional[str] = None

    
    
class SimulateOCR():
    def __init__(self, folder):
        super().__init__()  
        self.folder = folder
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
        folder_contents = [os.path.join(self.folder, f) for f in os.listdir(self.folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        all_outputs = []
        for image_path in folder_contents:
            # Read and encode image
            with open(image_path, "rb") as image_file:
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
            
            # Create a dictionary for the result of this image and append to the list
            image_result = {
                "has_file": str(image_path),
                "result": {
                    "has_file": str(image_path),
                    "full_solutions": self.ocr_output.full_solutions or [{
                        "problem_setup": "_",
                        "expressions": "No solution"
                    }],
                    "steps_count": self.ocr_output.steps_count,
                    "empty_message": self.ocr_output.empty_message or None
                }
            }
            all_outputs.append(image_result)
        return all_outputs


    def getResponse(self):
        client = OpenAI()
        
        completion = client.beta.chat.completions.parse(
            model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::BFZWjNAX",
            messages=self.conversation,
            temperature=0.2,
            response_format=OCRResponse,
            store=True
        )
        event = completion.choices[0].message.parsed
        return event
    