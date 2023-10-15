import json
import os
import openai

from flask import Flask, request
from app.main.com.company.utils.ProjectConstants import model_token
from app.main.com.company.utils.PDFFileRead import PDFFileRead
from app.main.com.company.utils.PromptCreation import PromptCreation
from app.main.com.company.utils.PromptTexts import completions_system_msg
from app.main.com.company.utils.SyntaxExtract import SyntaxExtractor
from app.main.com.company.utils.PlantUMLUtil import PlantUMLUtil

app = Flask(__name__)


@app.route('/api/public/generateuml', methods=['POST'])
def post_generate_uml():

    request_json = json.loads(request.data)
    token = model_token
   # read the requirement from input.pdf in the util folder. Provide File path if the file is in some other folder
    pdffileread = PDFFileRead()
    current_path=os.getcwd()
    path_components = current_path.split(os.path.sep)
    parent_directory = os.path.sep.join(path_components[:-1])
    requirement = pdffileread.extractPDFFileContent(parent_directory+os.sep+utils+os.sep+"input.pdf")
    prompt = PromptCreation.create_initial_prompt(requirement)

    # Create an instance of the OpenAIChatbot class
    chatbot = OpenAIServices()

    # Example conversation with system message, headers, and user message
    system_message = completions_system_msg
    user_message = prompt
    #header = "Header: Please translate the following text."
    #user_input = "'Hello, how are you?'"

    # Combine system message, headers, and user message into the prompt
    combined_prompt = f"{system_message}\n{user_message}"

    # Get a response from OpenAI
    responseText = chatbot.get_openai_response(combined_prompt)
    response = responseText.json()['choices'][0]['message']['content']
    syntaxExtractor = SyntaxExtractor()
    syntax = syntaxExtractor.extractPlantUMLSyntaxFromResponse(response)
    plantUMLObj = PlantUMLUtil()
    plantUMLObj.generateUMLFromSyntax(syntax,parent_directory+os.sep+utils+os.sep+"UMLDiagram.png")
    return response
