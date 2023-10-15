class TextFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "File not found."

    def write_file(self, content):
        try:
            with open(self.filename, 'w') as file:
                file.write(content)
            return "File written successfully."
        except Exception as e:
            return f"An error occurred: {str(e)}"

##if __name__ == "__main__":
    # Example usage:
##    file_handler = TextFileHandler("example.txt")

    # Reading the file
##    file_content = file_handler.read_file()
##    print("File Content:")
##    print(file_content)

    # Writing to the file
##    new_content = "This is some new content."
##    write_result = file_handler.write_file(new_content)
##    print(write_result)
