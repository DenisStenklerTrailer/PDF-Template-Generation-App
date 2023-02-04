import pandas
from fpdf import FPDF
import pandas as pd

df = pandas.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4") #P = Portrait, L = landscape

for index, row in df.iterrows():
    pdf.add_page() # Adding the page (FIRST PAGE)

    pdf.set_font('Arial', 'B', 14) # (family, style, size)
    pdf.set_text_color(100, 100, 100) #RGB
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1) # ln is actually a break line
    pdf.line(10, 20, 200, 20) # (x1,y1,x2,y2)

pdf.output("output.pdf") #Kreiranje PDF-ja