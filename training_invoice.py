import random
import datetime
import textwrap
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 16)
        # Moving cursor to the right:
        self.cell(40)
        # Printing title:
        self.cell(120, 10, "Advanced Institute of Online Training", border=1, align="C")

        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"No Bargaining", align="C")

productid_set = set(range(1,81))

# declare ending message
message = 'Thanks for shopping with us today!'

trainings = [
        "Generative AI for Beginners",
        "The Complete Python Pro Bootcamp",
        "Master Azure Databricks for Data Engineers",
        "Apache Spark - Beyond Basics",
        "Machine Learning Deep Learning model deployment",
        "Ultimate AWS Certified Cloud Practitioner",
        "Mastering dbt (Data Build Tool) ",
        "Machine Learning, Data Science and Generative AI with Python",
        "Snowflake Decoded",
        "Mastering Azure Data Engineering",
        "Regression Analysis & Data Analytics",
        "Data Management Masterclass",
        "Data Architecture with Microsoft Fabric",
        "Software Architecture & Design of Modern Systems"
        ]
random.shuffle(trainings)
try:
    for training in trainings[:7]:
        count = random.randint(3,5)
        for x in range(count):
            pdf = PDF()
            pdf.add_page()
            pdf.set_font("helvetica", "B", 14)
            pdf.cell(0, 5, "Main Churaha, R-Block, Mohan Garden, Uttam Nagar", border=0, align="C")
            pdf.ln(5)
            pdf.cell(0, 5, "New Delhi - 110059", border=0, align="C")
            pdf.ln(10)
            pdf.set_font("Times", "BI", 12)

            bill_date = datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 150))
            pdf.cell(0, 5, "RECEIPT", border=0, align="C")
            pdf.ln(10)
            pdf.set_font("Times", size=10)

            pdf.cell(0, 5, f'Bill No: {random.randint(100, 999)}', align='R')
            pdf.ln(10)
            pdf.cell(0, 5, f'Bill Date: {bill_date.date()}', align='R')
            pdf.ln(10)
            pdf.set_font("Times", 'B', size=10)
            pdf.cell(0, 5, f'Received With Thanks From:')
            pdf.set_font("Times", size=10)
            pdf.cell(0, 5, f'Rajesh Kaushik', align='R')
            pdf.ln(10)
            pdf.set_font("Times", 'B', size=10)
            pdf.cell(0, 5, f'Address:')
            pdf.set_font("Times", size=10)
            pdf.cell(0, 5, f'B-14, Sewak Park, Uttam Nagar, New Delhi - 110059', align='R')
            pdf.ln(10)
            pdf.set_font("Times", 'B', size=10)
            pdf.cell(0, 5, f'The Sum of Rs:')
            pdf.set_font("Times", size=10)
            pdf.cell(0, 5, f'Ten Thousands Only', align='R')
            pdf.ln(10)
            pdf.set_font("Times", 'B', size=10)
            pdf.cell(0, 5, f'On the Account of:')
            pdf.set_font("Times", size=10)
            pdf.cell(0, 5, f'{training}', align='R')
            pdf.ln(25)
            pdf.set_font("Times", 'B', 11)
            pdf.cell(0, 5, f'TOTAL: 10000', align='R')
            pdf.ln(30)
            pdf.set_font("Times", "BI", 12)
            pdf.cell(0, 5, f'Authorised Signatory', align='R')
            pdf.output(f"bills/trainings/{bill_date.date()}.pdf")
            # pdf.output('test.pdf')
except Exception as excep:
    import ipdb; ipdb.set_trace()
    print(excep)