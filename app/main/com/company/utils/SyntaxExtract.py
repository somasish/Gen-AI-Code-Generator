class SyntaxExtractor:

    def __init__(self):
        """Constructor"""
        extractedText =''
        pass

    def extractPlantUMLSyntaxFromResponse(self, response):

        syntaxStarting = "@startuml"
        syntaxEnding = "@enduml"

        startIndex = response.index(syntaxStarting)
        endIndex = response.index(syntaxEnding)
        subStr = response[startIndex:endIndex]
        extractedText = subStr + "@enduml"
        return extractedText