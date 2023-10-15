import PyPDF2


class PDFFileRead:

    def extractPDFFileContent(self,pdf_file_path):

        # Open the PDF file in binary mode
        with open(pdf_file_path, 'rb') as pdf_file:
             # Create a PDF reader object
             pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                # Check if the PDF file is encrypted
             if pdf_reader.isEncrypted:
                pdf_reader.decrypt("")  # Provide the decryption password if the PDF is encrypted

            # Initialize an empty string to store the extracted text
                extracted_text = ''
            # Loop through each page in the PDF
             for page_number in range(pdf_reader.numPages):
                # Get the text content of the page
                page = pdf_reader.getPage(page_number)
                page_text = page.extractText()
        # Append the page text to the extracted_text string
                extracted_text += page_text

    # Print or process the extracted text as needed
        print(extracted_text)
        return extracted_text
