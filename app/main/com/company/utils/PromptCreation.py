class PromptCreation:


    @staticmethod
    def create_initial_prompt(file_content):
        prompt = file_content +("Provide me the complex class diagram with all the "
                                "relationships for the above requirement in PlantUML syntax "
                                "you should ignore all the comment lines and provide the response "
                                "in the following json format:"
                                "{"
                                "\"plantUmlSyntax\": <Generated PlantUML syntax>"
                                "}")
        return prompt

    @staticmethod
    def create_cucumber_prompt(file_content):
        cucumber_prompt = file_content +("Provide me the complex class diagram with all the "
                                "relationships for the above requirement in PlantUML syntax "
                                "you should ignore all the comment lines and provide the response "
                                "in the following json format:"
                                "{"
                                "\"plantUmlSyntax\": <Generated PlantUML syntax>"
                                "}")
        return cucumber_prompt


    @staticmethod
    def create_enhancement_prompt(initial_text, enhancement):
        enhancement_prompt = initial_text + "Enhance this system with the requirement " + enhancement +(" Provide me the complex class diagram with all the "
                                "relationships for the above requirement in PlantUML syntax "
                                "you should ignore all the comment lines and provide the response "
                                "in the following json format:"
                                "{"
                                "\"gherkinCucumberScenario\": <create cucumber testcases>"
                                "}")
        return enhancement_prompt