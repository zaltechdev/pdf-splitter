import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_dir):
    """Splits a PDF into individual pages."""
    if not os.path.exists(input_pdf_path):
        print(f"Error: File {input_pdf_path} not found.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reader = PdfReader(input_pdf_path)
    
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        
        output_filename = os.path.join(output_dir, f"page_{i + 1}.pdf")
        with open(output_filename, "wb") as output_pdf:
            writer.write(output_pdf)
        
        print(f"Created: {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python splitpdf.py <input_pdf_path> [output_directory]")
    else:
        input_pdf = sys.argv[1]
        output_directory = sys.argv[2] if len(sys.argv) > 2 else "output"
        split_pdf(input_pdf, output_directory)
