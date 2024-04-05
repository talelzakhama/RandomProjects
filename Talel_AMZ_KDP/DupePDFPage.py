import PyPDF2
import argparse
"""
This script takes a pdf file, and copies the first page of it (template) n times.

Example of use:
  python3 <path_to_DupePDF_Page> -I <path_to_input_file> -O <path_to_output_file> -N <number_of_copies>
"""

parser = argparse.ArgumentParser(description="Add copy first page of pdf n times")
parser.add_argument('-N','--num_copies',type=int,metavar='',required=True,help='Number of Copies')
parser.add_argument('-I','--input_file',type=str,metavar='',required=True,help='Path to input file')
parser.add_argument('-O','--output_file',type=str,metavar='',required=True,help='Path to output file')
group = parser.add_mutually_exclusive_group()
args = parser.parse_args()

def copy_pdf_page(input_file, output_file, num_copies):
    """Copies a single page from a PDF file multiple times and creates a new PDF.

  Args:
    input_file: Path to the input PDF file.
    output_file: Path to the output PDF file.
    num_copies: Number of times to copy the page.
  """
    with open(input_file, 'rb') as pdf_file, open(output_file, 'wb') as out_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Get the first page from the input PDF
        page = pdf_reader.pages[0]

        # Add the copied page to the output PDF multiple times
        for _ in range(num_copies):
            pdf_writer.add_page(page)

        pdf_writer.write(out_file)

if __name__ == '__main__':
  copy_pdf_page(args.input_file, args.output_file, args.num_copies)
