import plantuml
import subprocess
import os

class PlantUMLUtil():

    def generateUMLFromSyntax(self,syntax,outputFilePath):
        plantuml_process = subprocess.Popen(['java', '-jar', os.getcwd() + os.sep + "plantuml-1.2023.11.jar", '-p'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        syntax_in_bytes = bytes(syntax, 'utf-8')
        stdout, stderr = plantuml_process.communicate(syntax_in_bytes)

        if plantuml_process.returncode == 0:
            # Save the diagram as an image file (e.g., output.png)
            with open(output_file, 'wb') as f:
                f.write(stdout)
                f.close()
            print(f"UML diagram saved as {outputFilePath}")
        else:
            print("Error while generating the diagram:")
            print(stderr.decode())
            decodedPrompt = stderr.decode()
            return decodedPrompt


