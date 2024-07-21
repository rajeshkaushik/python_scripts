import random
import datetime
import textwrap
from fpdf import FPDF

def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')

# create a product and price dictionary
books = {
    "product1_name": "Modern Data Engineering with Apache Spark",
    "product1_price": 3800,
    "product2_name": 'Azure DevOps Explained',
    "product2_price": 2620,
    "product3_name": "Power Excel with MrExcel - 2017 Edition",
    "product3_price":  1910,
    "product4_name": 'Amazon Redshift Cookbook ',
    "product4_price": 3200,
    "product5_name": 'Big Data Application Architecture Q&A ',
    "product5_price": 2940,
    "product6_name": 'AWS Certified Solutions Architect Associate Training Notes 2023',
    "product6_price": 3800,
    "product7_name": 'Aws Certified Solutions Architect Associate All-In-One Exam Guide',
    "product7_price": 3560,
    "product8_name": 'AWS Certified Solutions Architect Associate Practice Tests',
    "product8_price": 2380,
    "product9_name": 'Cloud Native Architectures',
    "product9_price": 2950,
    "product10_name": 'AWS Certified Solutions Architect Study Guide ',
    "product10_price": 3140,
    "product11_name": 'Serverless Architectures on AWS',
    "product11_price": 3520,
    "product12_name": 'Professional Cloud Architect - Google Cloud Certification Guide',
    "product12_price": 2720,
    "product13_name": "The Professional Cloud Architect's Big Fact Sheet",
    "product13_price": 3200,
    "product14_name": 'Practical Machine Learning with AWS',
    "product14_price": 3910,
    "product15_name": 'Programming Rust: Fast, Safe Systems Development ',
    "product15_price": 2450,
    "product16_name": 'Learn MongoDB 4.x',
    "product16_price": 2660,
    "product17_name": 'Mastering Apache Cassandra 3.X',
    "product17_price": 2550,
    "product18_name": 'Expert Apache Cassandra Administration',
    "product18_price": 3400,
    "product19_name": 'Practical Amazon EC2, SQS, Kinesis, and S3',
    "product19_price": 3660,
    "product20_name": 'Rust Web Programming ',
    "product20_price": 2580,
    "product21_name": 'Mastering Redis',
    "product21_price": 3500,
    "product22_name": 'Disaster Recovery and Business Continuity',
    "product22_price": 2800,
    "product23_name": 'Professional SQL Server High Availability and Disaster Recovery',
    "product23_price": 2550,
    "product24_name": 'Introducing Disaster Recovery with Microsoft Azure ',
    "product24_price": 3490,
    "product25_name": 'Advanced TypeScript Programming Projects ',
    "product25_price": 2700,
    "product26_name": 'Node.js Design Patterns',
    "product26_price": 3120,
    "product27_name": "Solutions Architect's Handbook",
    "product27_price": 3590,
    "product28_name": 'Google Cloud Certified Professional Cloud Developer Exam Guide',
    "product28_price": 2950,
    "product29_name": 'React and React Native',
    "product29_price": 3450,
    "product30_name": 'Roadmap to a Google Cloud Professional Machine Learning Engineer',
    "product30_price": 2800,
    "product31_name": 'Azure Data Factory Cookbook ',
    "product31_price": 2990,
    "product32_name": 'Implementing Microsoft Azure Architect Technologies ',
    "product32_price": 2570,
    "product33_name": 'Azure Networking Cookbook ',
    "product33_price": 3200,
    "product34_name": 'Official Google Cloud Certified Professional Cloud Architect Study Guide',
    "product34_price": 3550,
    "product35_name": 'Expert Apache Cassandra Administration',
    "product35_price": 3380,
    "product36_name": 'Azure Data Factory Cookbook',
    "product36_price": 2650,
    "product37_name": 'DynamoDB Applied Design Patterns ',
    "product37_price": 2900,
    "product38_name": 'The Definitive Guide to Azure Data Engineering',
    "product38_price": 3420,
    "product39_name": 'SQL Server Data Automation Through Frameworks',
    "product39_price": 2870,
    "product40_name": 'Python for DevOps',
    "product40_price": 1995,
    "product41_name": 'Mastering Python Networking ',
    "product41_price": 2750,
    "product42_name": 'Implementing Azure DevOps Solutions',
    "product42_price": 2850,
    "product43_name": 'Practical Ansible 2',
    "product43_price": 2110,
    "product44_name": 'AWS Lambda in Action: Event-driven serverless applications',
    "product44_price": 2800,
    "product45_name": 'Mastering Git',
    "product45_price": 3195,
    "product46_name": 'JIRA Software Essentials - Second Edition ',
    "product46_price": 2190,
    "product47_name": 'Codeless Data Structures and Algorithms',
    "product47_price": 3330,
    "product48_name": 'BoElements of Discrete Mathematics oks',
    "product48_price": 1255,
    "product49_name": 'Oracle PL / SQL For Dummies',
    "product49_price": 2350,
    "product50_name": 'Serverless ETL and Analytics with AWS Glue ',
    "product50_price": 3000,
    "product51_name": 'AWS Certified Advanced Networking Official Study Guide ',
    "product51_price": 3440,
    "product52_name": 'AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide ',
    "product52_price": 3230,
    "product53_name": 'Simplify Big Data Analytics with Amazon EMR',
    "product53_price": 2800,
    "product54_name": 'Machine Learning with BigQuery ML ',
    "product54_price": 3000,
    "product55_name": 'The Kubernetes Bible',
    "product55_price": 3200,
    "product56_name": 'Docker in Action, Second Edition ',
    "product56_price": 3150,
    "product57_name": 'Mastering MariaDB',
    "product57_price": 3400,
    "product58_name": 'Nginx HTTP Server - Fourth Edition',
    "product58_price": 3120,
    "product59_name": 'Building Python Web APIs with FastAPI ',
    "product59_price": 2800,
    "product60_name": 'Clean Android Architecture',
    "product60_price": 2420,
    "product61_name": 'Clean Agile: Back to Basics ',
    "product61_price": 2880,
    "product62_name": 'CLEAN ARCHITECTURE ',
    "product62_price": 1100,
    "product63_name": 'Clean Craftsmanship: Disciplines, Standards, and Ethics ',
    "product63_price": 3440,
    "product64_name": 'TOGAF STANDARD 10TH EDITION ARCHITECTURE ',
    "product64_price": 3550,
    "product65_name": 'Flutter Cookbook ',
    "product65_price": 2400,
    "product66_name": 'Generative AI with Python and TensorFlow 2',
    "product66_price": 2780,
    "product67_name": 'Technology Trends in Practice: Grow Your Businessby Using 30 New Technology Trends for Success',
    "product67_price": 2450,
    "product68_name": 'The DevOps Handbook: How to Create World-Class Agility, Reliability, & Security in Technology',
    "product68_price": 1750,
    "product69_name": 'Generative AI on AWS: Building Context-Aware Multimodal Reasoning Applications',
    "product69_price": 2250,
    "product70_name": 'Generative AI For Business Leaders',
    "product70_price": 3350,
    "product71_name": 'Deciphering Data Architectures: Choosing Between a Modern Data Warehouse, Data Fabric, Data Lakehouse, and Data Mesh',
    "product71_price": 1400,
    "product72_name": 'Data Management at Scale: Modern Data Architecture with Data Mesh and Data Fabric',
    "product72_price": 1950,
    "product73_name": 'Data Engineering with dbt: A practical guide to building a cloud-based, pragmatic, and dependable data platform with SQL',
    "product73_price": 2550,
    "product74_name": 'Data Governance Handbook: A practical approach to building trust in data',
    "product74_price": 3650,
    "product75_name": 'DAMA-DMBOK (2ND EDITION) 2/E',
    "product75_price": 2490,
    "product76_name": 'Mastering NLP from Foundations to LLMs: Apply advanced rule-based techniques to LLMs and solve real-world business problems',
    "product76_price": 3750,
    "product77_name": 'Prompt Engineering for Generative AI',
    "product77_price": 1780,
    "product78_name": 'Knowledge Graphs: Fundamentals, Techniques, and Applications',
    "product78_price": 2500,
    "product79_name": 'The Five Dysfunctions of a Team: A Leadership Fable',
    "product79_price": 2300,
    "product80_name": 'Inspired: How to Create Tech Products Customers Love',
    "product80_price": 1770,
    "product81_name": 'Servant Leadership in Action: How You Can Achieve Great Relationships and Results',
    "product81_price": 2440,
    # "product82_name": 'Books',
    # "product82_price": 50.95,
    # "product83_name": 'Books',
    # "product83_price": 50.95,
    # "product84_name": 'Books',
    # "product84_price": 50.95,
    # "product85_name": 'Books',
    # "product85_price": 50.95,
    # "product86_name": 'Books',
    # "product86_price": 50.95,
    # "product87_name": 'Books',
    # "product87_price": 50.95,
    # "product88_name": 'Books',
    # "product88_price": 50.95,
    # "product89_name": 'Books',
    # "product89_price": 50.95,
    # "product90_name": 'Books',
    # "product90_price": 50.95,
    }

productid_set = set(range(1,81))

# create a company name and information
company_name = 'Vishakha Books.'
company_address = 'Indira garden, Khora Colony, OPP, Sector 62'
company_city = 'Noida, Uttar Pradesh - 201309'

# declare ending message
message = 'Thanks for shopping with us today!'

for fileno in range(50):
    try:
        if len(productid_set) < 3:
            break
        bill_date = datetime.datetime.now() + datetime.timedelta(days=random.randint(-20, 160))

        # create a top border
        # print('*' * 85)
        text = u''
        text = '*' * 85

        # print(f'\n\tBill Date: {bill_date.date()}')
        text += f'\n\n\tBill Date: {bill_date.date()}'
        # print(f'\tBill No: {random.randint(100, 999)}')
        text += f'\n\tBill No: {random.randint(100, 999)}\n'

        # print company information first using format
        # print('\n\n\t\t\t{}'.format(company_name.title()))
        text += '\n\t\t\t{}'.format(company_name.title())
        # print('\t\t\t{}'.format(company_address.title()))
        text += '\n\t\t\t{}'.format(company_address.title())
        # print('\t\t\t{}\n'.format(company_city.title()))
        text += '\n\t\t\t{}\n\n\n'.format(company_city.title())

        # print a line between sections
        # print('=' * 85)
        text += '=' * 85

        # print out header for section of items
        # print('\n\tProduct Name\t\t\t\t\t\tProduct Price\n')
        text += '\n\n\tProduct Name\t\t\t\t\t\tProduct Price\n\n'

        total = 0

        while True:
    
            x = random.choice(list(productid_set))
            total += books[f"product{x}_price"]

            if total < 9800:

                product_name = books[f"product{x}_name"]
                product_name = f"{product_name:<45}"
                product_name = f"{product_name:.45}"
                product_price = books[f"product{x}_price"]
                # create a print statement for each item
                # print(f"\t{product_name}\t\tRs. {product_price}\n")
                text += f"\n\t{product_name}\t\tRs. {product_price}\n"

                productid_set.remove(x)
            else:
                total -= books[f"product{x}_price"]
                break

        # print a line between sections
        # print('\n\n\n\n\n\n')
        text += '\n\n\n\n\n\n\n\n\n\n\n\n'
        # print('=' * 85)
        text += '=' * 85

        # print out header for section of total
        # print('\n\t\t\t\t\t\t\t\tTotal\n')
        text += '\n\n\t\t\t\t\t\t\t\tTotal\n'

        # print('\t\t\t\t\t\t\t\tRs. {}\n'.format(total))
        text += '\n\t\t\t\t\t\t\t\tRs. {}\n\n'.format(total)

        # print a line between sections
        # print('=' * 85)
        text += '=' * 85


        # print('\n\n\n\t\t\t\t\t\t\t\tAuthorised Signatory')
        text += '\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tAuthorised Signatory'

        # output thank you message
        # print('\n\t\t\t{}\n'.format(message))
        text += '\n\n\n\n\t\t\t{}\n\n'.format(message)

        # create a bottom border
        # print('*' * 85)
        text += '*' * 85
        # print('\n\n\n\n')
        text += '\n\n\n\n'

        file_name = f"bills/books/{bill_date.date()}.pdf"

        text_to_pdf(text, file_name)
    except Exception as excep:
        print(text)
        import ipdb; ipdb.set_trace()
        print(excep)
