from PyPDF2 import PdfReader, PdfWriter

# Set the input and output file paths
input_pdf_path = "/Users/jcarhart/Documents/NarxCare-Demo-Script-for-NABP-Aug.pdf"
output_pdf_path = "/Users/jcarhart/Documents/NarxCare-Demo-Script-for-NABP-Aug-cleaned.pdf"

# Read the input PDF
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# Loop through each page and add it to the writer
for i in range(len(reader.pages)):
    writer.add_page(reader.pages[i])

# Write the cleaned PDF to the output path
with open(output_pdf_path, "wb") as f:
    writer.write(f)

print(f"Cleaned PDF saved to {output_pdf_path}")
