import pandas
from fpdf import FPDF
import pandas as pd

df = pandas.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4") #P = Portrait, L = landscape
pdf.set_auto_page_break(auto=False, margin=0) # Page is not breaked automatically

for index, row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page() # Adding the page (FIRST PAGE)

        if i == 0:
            pdf.set_font('Arial', 'B', 14) # (family, style, size)
            pdf.set_text_color(100, 100, 100) #RGB
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1) # ln is actually a break line
            pdf.line(10, 20, 200, 20) # (x1,y1,x2,y2)

            pdf.ln(258)  # 258mm
            pdf.set_font('Arial', 'B', 8)  # (family, style, size)
            pdf.set_text_color(180, 180, 180)  # RGB
            pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

        else:
            pdf.ln(267)  # 267mm
            pdf.set_font('Arial', 'B', 8)  # (family, style, size)
            pdf.set_text_color(180, 180, 180)  # RGB
            pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)




pdf.output("output.pdf") #Kreiranje PDF-ja