# Write a program to manipulate pdf files using pyPDF. your program should be able to merge multiple pdf files into a single pdf.


from pypdf import PdfReader, PdfWriter

reader = PdfReader("Day 24/abc.pdf")

# to claculate total pages

print(f"Total pages {len(reader.pages)}")

# to extract the content of the pdf

page = reader.pages[0]
print(page.extract_text())        

# merges pdf

writer = PdfWriter()

files = ['Day 24/abc.pdf', 'Day 24/pqr.pdf', 'Day 24/xyz.pdf']

for file in files:
    writer.append(file)

with open("Day 24/merged.pdf", "wb") as output_pdf:
    writer.write(output_pdf)