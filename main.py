import pandas
from fpdf import FPDF
import pandas as pd

df = pandas.read_csv("topics.csv")


pdf = FPDF(orientation="P", unit="mm", format="A4") #P = Portrait, L = landscape

pdf.add_page() # Adding the page (FIRST PAGE)

pdf.set_font('Arial', 'B', 14) # (family, style, size)
pdf.cell(w=0, h=12, txt="Hello", align="L", ln=1, border=1) # ln is actually a break line
pdf.cell(w=0, h=12, txt="Hi there...", align="L", ln=1, border=1)

pdf.add_page() # Adding the page (SECOND PAGE)

pdf.set_font('Arial', 'B', 14) # (family, style, size)
pdf.cell(w=0, h=12, txt="Hello", align="L", ln=1, border=1) # ln is actually a break line
pdf.cell(w=0, h=12, txt="Hi there...", align="L", ln=1, border=1)

pdf.output("output.pdf") #Kreiranje PDF-ja