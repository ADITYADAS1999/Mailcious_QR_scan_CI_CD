import os
from pyzbar.pyzbar import decode
from PIL import Image
from pdf2image import convert_from_path
from docx import Document
import io
import markdown
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

QR_FOLDER = "qr_images"
REPORT_FOLDER = "reports"
REPORT_MD = os.path.join(REPORT_FOLDER, "qr_scan_report.md")
REPORT_HTML = os.path.join(REPORT_FOLDER, "qr_scan_report.html")
REPORT_PDF = os.path.join(REPORT_FOLDER, "qr_scan_report.pdf")

SUSPICIOUS_KEYWORDS = ["http://", "bit.ly", "tinyurl", "goo.gl", "qrco.de"]

# --- Extractors ---
def extract_qr_data_from_image(image_path):
    try:
        img = Image.open(image_path)
        results = decode(img)
        return [r.data.decode("utf-8") for r in results]
    except Exception as e:
        return [f"Error decoding {image_path}: {str(e)}"]

def extract_qr_data_from_pdf(pdf_path):
    qr_results = []
    try:
        pages = convert_from_path(pdf_path)  # convert each page to image
        for page_num, page in enumerate(pages, start=1):
            results = decode(page)
            for r in results:
                qr_results.append(f"[Page {page_num}] {r.data.decode('utf-8')}")
    except Exception as e:
        qr_results.append(f"Error decoding {pdf_path}: {str(e)}")
    return qr_results

def extract_qr_data_from_docx(docx_path):
    qr_results = []
    try:
        doc = Document(docx_path)
        for rel in doc.part.rels.values():
            if "image" in rel.reltype:
                img_data = rel.target_part.blob
                img = Image.open(io.BytesIO(img_data))
                results = decode(img)
                for r in results:
                    qr_results.append(r.data.decode("utf-8"))
    except Exception as e:
        qr_results.append(f"Error decoding {docx_path}: {str(e)}")
    return qr_results

# --- Analyzer ---
def analyze_qr_data(data):
    if any(keyword in data.lower() for keyword in SUSPICIOUS_KEYWORDS):
        return "⚠️ Suspicious", "High"
    if data.startswith("https://"):
        return "✅ Safe", "Low"
    return "❓ Unknown", "Medium"

# --- Generators ---
def generate_md_report(results):
    with open(REPORT_MD, "w", encoding="utf-8") as report:
        report.write("# QR Code Scan Report\n\n")
        report.write("| File | QR Data | Status | Risk |\n")
        report.write("|------|---------|--------|------|\n")
        for row in results:
            report.write(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |\n")

def generate_html_report():
    with open(REPORT_MD, "r", encoding="utf-8") as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=["tables"])
    with open(REPORT_HTML, "w", encoding="utf-8") as f:
        f.write("<html><head><title>QR Scan Report</title></head><body>")
        f.write(html_content)
        f.write("</body></html>")

def generate_pdf_report(results):
    doc = SimpleDocTemplate(REPORT_PDF, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("QR Code Scan Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    table_data = [["File", "QR Data", "Status", "Risk"]]
    for row in results:
        table_data.append(row)

    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)

# --- Main ---
def main():
    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)

    results = []

    for file in os.listdir(QR_FOLDER):
        path = os.path.join(QR_FOLDER, file)

        qr_data_list = []
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            qr_data_list = extract_qr_data_from_image(path)
        elif file.lower().endswith(".pdf"):
            qr_data_list = extract_qr_data_from_pdf(path)
        elif file.lower().endswith(".docx"):
            qr_data_list = extract_qr_data_from_docx(path)

        if not qr_data_list:
            results.append((file, "No QR code found", "❌ Failed", "High"))
            continue

        for qr_data in qr_data_list:
            status, risk = analyze_qr_data(qr_data)
            results.append((file, qr_data, status, risk))

    # Generate reports
    generate_md_report(results)
    generate_html_report()
    generate_pdf_report(results)

    print(f"✅ Reports generated in {REPORT_FOLDER}")


if __name__ == "__main__":
    main()
