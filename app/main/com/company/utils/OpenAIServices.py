import openai

from app.main.com.company.utils.ProjectConstants import model_token


class OpenAIServices:
    def __init__(self):
        self.api_key = model_token
        openai.api_key = self.api_key

    def get_openai_response(self, prompts, max_tokens=50, temperature=0.7, engine="text-davinci-002"):
        response = openai.Completion.create(
            engine=engine,
            prompt=prompts,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].text


    # Replace with your actual API key

    # Create an instance of the OpenAIChatbot class
    #chatbot = OpenAIChatbot()

    # Example conversation with system message, headers, and user message
    #system_message = "You are chatting with a helpful assistant."
    #user_message = "Translate the following English text to French:"
    #header = "Header: Please translate the following text."
    #user_input = "'Hello, how are you?'"

    # Combine system message, headers, and user message into the prompt
    #combined_prompt = f"{system_message}\n{header}\n{user_message}\n{user_input}"

    # Get a response from OpenAI
    #response = chatbot.get_openai_response(combined_prompt)

    # Print the response
    #print(response)









