from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv", sep=",")


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True, margin=0)


for index, row in df.iterrows():
    # Add new page
    pdf.add_page()
    pdf.set_font("Times", "B", 24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 12, txt=row["Topic"], ln=True, align="L")
    pdf.line(10, 20, 200, 20)
    
    for i in range(10, 281, 10):
        pdf.line(10, i, 200, i)
    
    # Add footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 10, txt=f"Page {pdf.page_no()}", ln=True, align="R")

    # Add extra pages
    for _ in range(row["Pages"] - 1):
        pdf.add_page()
        
        for i in range(0, 281, 10):
            pdf.line(10, i, 200, i)
        
        # Add footer to extra pages
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=f"Page {pdf.page_no()}", ln=True, align="R")


pdf.output("simple_demo.pdf")