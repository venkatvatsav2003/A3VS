from fpdf import FPDF
from utils.logger import logger

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'A3VS - AI Vulnerability Scan Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf_report(markdown_content: str, output_path: str):
    """
    Converts markdown report to a simple PDF.
    """
    try:
        pdf = PDFReport()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Simple markdown to PDF (just stripping some symbols for now)
        lines = markdown_content.split('\n')
        for line in lines:
            if line.startswith('# '):
                pdf.set_font("Arial", 'B', 14)
                pdf.multi_cell(0, 10, line[2:])
                pdf.set_font("Arial", size=12)
            elif line.startswith('## '):
                pdf.set_font("Arial", 'B', 13)
                pdf.multi_cell(0, 10, line[3:])
                pdf.set_font("Arial", size=12)
            elif line.startswith('- '):
                pdf.multi_cell(0, 10, f'  * {line[2:]}')
            else:
                pdf.multi_cell(0, 10, line)
            pdf.ln(2)
            
        pdf.output(output_path)
        logger.info(f"PDF report generated at {output_path}")
    except Exception as e:
        logger.error(f"Failed to generate PDF report: {e}")
