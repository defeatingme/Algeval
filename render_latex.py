import re


# Define HTML content with MathJax
def MathJaxSOL(latex_raw):
    # Convert Markdown horizontal rule (---) to HTML with extra spacing
    processed_content = re.sub(r'^---+$', r'<hr class="separator">', latex_raw, flags=re.MULTILINE)

    # Process Markdown headings before sending to MathJax
    processed_content = re.sub(r'### (.*?)(?=\n|$)', r'<h3>\1</h3>', latex_raw)
    
    # Convert "Step X:" format to bold text
    processed_content = re.sub(r'(Step \d+:)', r'<b>\1</b>', processed_content)
    
    # Convert "Final Answer:" to bold text
    processed_content = re.sub(r'(Final Answer:)', r'<b>\1</b>', processed_content)
    
    # Highlight correctness evaluations
    processed_content = processed_content.replace("is Correct", "<span class='correct'>is Correct</span>")
    processed_content = processed_content.replace("is Incorrect", "<span class='incorrect'>is Incorrect</span>")
    
    # Style score information
    processed_content = re.sub(r'(Solution = .*?%)', r'<div class="score">\1</div>', processed_content)
    processed_content = re.sub(r'(Final Answer = .*?%)', r'<div class="score">\1</div>', processed_content)
    processed_content = re.sub(r'(Overall Score = .*?%)', r'<div class="overall-score">\1</div>', processed_content)
    
    # Convert newlines to <br> tags to preserve formatting
    processed_content = processed_content.replace('\n', '<br>')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script id="MathJax-script" async 
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style>
            body {{
                background-color: rgb(64, 64, 64); /* Dark background */
                color: rgb(224, 224, 224); /* Light gray text */
                font-size: 16px;
                padding: 10px;
                font-family: Arial, sans-serif;
                overflow: auto; /* Enable scrolling if needed */
                border: 1px solid rgb(208, 172, 220);
            }}
            .math-container {{
                text-align: left;
                line-height: 1.5;
            }}
            h3 {{
                color: rgb(255, 200, 87); /* Goldish color for headings */
                margin-top: 15px;
                margin-bottom: 10px;
                font-size: 18px;
            }}
            b {{
                color: rgb(150, 255, 150); /* Light green for steps */
            }}
            .correct {{
                color: rgb(100, 255, 100); /* Green for correct items */
            }}
            .incorrect {{
                color: rgb(255, 100, 100); /* Red for incorrect items */
            }}
            .score {{
                margin-top: 10px;
                color: rgb(200, 200, 255); /* Light blue for scores */
                font-weight: bold;
            }}
            .overall-score {{
                color: rgb(255, 255, 150); /* Light yellow for overall score */
                font-weight: bold;
                font-size: 18px;
                margin-top: 5px;
            }}
            .separator {{
                height: 1px;
                background-color: rgb(150, 150, 150);
                border: none;
                margin-top: 25px;
                margin-bottom: 25px;
            }}
        </style>
    </head>
    <body>
        <div class="math-container">
            {processed_content}
        </div>
    </body>
    </html>
    """
    return html_content


def MathJaxRes(latex_raw):
    processed_content = re.sub(r'^---+$', r'<hr class="separator">', latex_raw, flags=re.MULTILINE)

    # Process Markdown headings before sending to MathJax
    processed_content = re.sub(r'### (.*?)(?=\n|$)', r'<h3>\1</h3>', latex_raw)
    
    # Convert "Step X:" format to bold text
    processed_content = re.sub(r'(Step \d+:)', r'<b>\1</b>', processed_content)
    
    # Convert "Final Answer:" to bold text
    processed_content = re.sub(r'(Final Answer:)', r'<b>\1</b>', processed_content)
    
    # Highlight correctness evaluations
    processed_content = processed_content.replace("is Correct", "<span class='correct'>is Correct</span>")
    processed_content = processed_content.replace("is Incorrect", "<span class='incorrect'>is Incorrect</span>")
    
    # Style score information
    processed_content = re.sub(r'(Solution = .*?%)', r'<div class="score">\1</div>', processed_content)
    processed_content = re.sub(r'(Final Answer = .*?%)', r'<div class="score">\1</div>', processed_content)
    processed_content = re.sub(r'(Overall Score = .*?%)', r'<div class="overall-score">\1</div>', processed_content)
    
    # Convert newlines to <br> tags to preserve formatting
    processed_content = processed_content.replace('\n', '<br>')

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script id="MathJax-script" async 
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style>
            body {{
                background-color: rgb(64, 64, 64); /* Dark background */
                color: rgb(224, 224, 224); /* Light gray text */
                font-size: 16px;
                padding: 10px;
                font-family: Arial, sans-serif;
                overflow: auto; /* Enable scrolling if needed */
                border: 1px solid rgb(208, 172, 220);
            }}
            .math-container {{
                text-align: left;
                line-height: 1.5;
            }}
            h3 {{
                color: pink; /* Goldish color for headings */
                margin-top: 15px;
                margin-bottom: 10px;
                font-size: 18px;
            }}
            b {{
                color: pink; /* Light green for steps */
            }}
            .correct {{
                color: rgb(100, 255, 100); /* Green for correct items */
            }}
            .incorrect {{
                color: rgb(255, 100, 100); /* Red for incorrect items */
            }}
            .score {{
                margin-top: 10px;
                color: rgb(175, 192, 220);; /* Light blue for scores */
                font-weight: bold;
            }}
            .overall-score {{
                color: rgb(255, 200, 87); /* Light yellow for overall score */
                font-weight: bold;
                font-size: 18px;
                margin-top: 5px;
            }}
            .separator {{
                height: 1px;
                background-color: rgb(150, 150, 150);
                border: none;
                margin-top: 25px;
                margin-bottom: 25px;
            }}
        </style>
    </head>
    <body>
        <div class="math-container">
            {processed_content}
        </div>
    </body>
    </html>
    """
    return html_content


def ClearHTML():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: rgb(64, 64, 64);
                margin: 0; /* Ensures no unwanted spacing */
                height: 100vh; /* Makes sure the background covers the whole viewport */
            }
        </style>
    </head>
    <body>
    </body>
    </html>
    """
    return html_content


def LoadHTML():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: rgb(64, 64, 64); /* Dark background */
                color: rgb(224, 224, 224); /* Light gray text */
                font-size: 14px; /* Adjusted for better visibility in 320x300 px */
                padding: 2px;
                font-family: Arial, sans-serif;
                overflow: auto; /* Enable scrolling if needed */
                border: 1px solid rgb(208, 172, 220)
            }
            .math-container {
                text-align: left;
                white-space: pre-wrap; /* Preserve new lines */
                font-size: 14px; /* Ensuring 7-8 layers fit */
                line-height: 1.5; /* Reduce line spacing */
            }
        </style>
    </head>
    <body>
        <div class="math-container">
            Loading...
        </div>
    </body>
    </html>
    """
    return html_content