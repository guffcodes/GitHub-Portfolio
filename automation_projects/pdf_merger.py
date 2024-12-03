# PDF Merger - consolidates multiple pdf files into one merged pdf
from PyPDF2 import PdfMerger

# Create Merger object
merger = PdfMerger()

# These "sample" files are local files - feel free to replace with others
merger.append("sample1.pdf")
merger.append("sample2.pdf")
merger.append("sample3.pdf", pages = (0, 3, 1)) # pages is a range (calls for pgs 1-3 in increments of 1)

# Write the merged pdf into a new file
merger.write("merged.pdf")
merger.close()

print("PDFs have been successfully merged into 'merged.pdf'")
