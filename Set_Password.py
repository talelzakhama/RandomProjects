import PyPDF2
import argparse

parser = argparse.ArgumentParser(description="Set a password for a pdf file")
parser.add_argument('-I','--input_file',type=str,metavar='',required=True,help='Path to input file')
parser.add_argument('-O','--output_file',type=str,metavar='',required=True,help='Path to output file')
parser.add_argument('-P','--password',type=str,metavar='',required=True,help='Desired Password')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true',help='print quiet')
group.add_argument('-v','--verbose',action='store_true',help='print verbose')
args = parser.parse_args()


def set_password(input_pdf, output_pdf, password):
    # Open the input PDF file
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    # Copy all pages from the input to the output PDF
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # Add a password to the output PDF
    pdf_writer.encrypt(password)

    # Write the output PDF to a file
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"PDF file '{output_pdf}' has been encrypted with the password provided.")


# Usage
input_pdf_path = args.input_file
output_pdf_path = args.output_file
password = args.password

set_password(input_pdf_path, output_pdf_path, password)
