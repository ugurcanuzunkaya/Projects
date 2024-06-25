from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv", sep=",")


pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Times", "B", 24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 12, txt=row["Topic"], ln=True, align="L")
    


pdf.output("simple_demo.pdf")