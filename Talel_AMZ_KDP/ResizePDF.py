import fitz  # PyMuPDF
import argparse

"""
Use:
python3 <path_to_this_script> -I "path_to_input_file" -O <path_to_output_file> -s <desired_size(A2,A3,A4,A5)>
"""
parser = argparse.ArgumentParser(description="Resize PDF file")
parser.add_argument('-s','--size',type=str,metavar='',required=True,help='Desired page size (A2,A3,A4,A5)')
parser.add_argument('-I','--input_file',type=str,metavar='',required=True,help='Path to input file')
parser.add_argument('-O','--output_file',type=str,metavar='',required=True,help='Path to output file')
group = parser.add_mutually_exclusive_group()
args = parser.parse_args()



def resize_pdf(input_pdf_path, output_pdf_path, new_width, new_height,dpi=300):
    doc = fitz.open(input_pdf_path)
    new_doc = fitz.open()  # Create a new PDF for output

    for page in doc:
        # Calculate the scale to fit the new size, preserving aspect ratio
        scale_x = new_width / page.rect.width
        scale_y = new_height / page.rect.height
        scale = min(scale_x, scale_y)

        # Create a transformation matrix for scaling, same resolution
        matrix = fitz.Matrix(scale, scale)

        # # The default rendering is 72 DPI, so adjust the scale factor for higher DPI
        # matrix = fitz.Matrix(scale * dpi / 72, scale * dpi / 72)

        # Render page to a pixmap (an image) applying the transformation matrix
        pix = page.get_pixmap(matrix=matrix)

        # Create a new PDF page with the desired dimensions
        new_page = new_doc.new_page(width=new_width, height=new_height)

        # Insert the rendered image into the new page
        new_page.insert_image(new_page.rect, pixmap=pix)

    # Save the resized PDF
    new_doc.save(output_pdf_path)
    new_doc.close()
    doc.close()


#
# System    Size Name	Width (in)	Height (in)	Width (mm)	Height (mm)
# ISO   	A0	        33.11	    46.81	    841	        1189
#           A1	        23.39	    33.11	    594	        841
#           A2	        16.54	    23.39	    420	        594
#           A3	        11.69	    16.54	    297	        420
#           A4	        8.27	    11.69	    210	        297
#           A5	        5.83	    8.27	    148	        210
#           A6	        4.13	    5.83	    105	        148
#           A7	        2.91	    4.13	    74	        105


# Mapping size in Point po
paper_size = {"A2":(1190.7, 1683.99),"A3":(841.995, 1190.7),"A4":(595.35, 841.995),"A5":(419.58, 595.35)}
resize_pdf(args.input_file, args.output_file, paper_size[args.size][0], paper_size[args.size][1],700)

