import os


class CreateCucumberFeaturefile:
    def __init__(self):
        """Construtor"""
        additional_scenarios = ''
        pass

    def createCucumberFile(self, scenarios , fileName):
        file = open(os.path.join('c:\\',fileName),'w')
        file.write(scenarios)
        print("scenarios.feature file saved in c drive")
        file.close()
        