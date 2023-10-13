import openai

from app.main.com.company.utils.ProjectConstants import model_token

class OpenAIServices:

    def __init__(self):
        """Constructor"""
        pass

    # Define a function to interact with the API
    def get_openai_response(prompt):
        openai.api_key = model_token
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can choose the appropriate engine
            prompt=prompt,
            max_tokens=1000,  # Adjust this based on the desired response length
            temperature=0.2  # Adjust for response creativity (0.2 is more focused, 1.0 is more random)
        )
        return response.choices[0].text








