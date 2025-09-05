import os
from pyzbar.pyzbar import decode
from PIL import Image
import requests

QR_FOLDER = "qr_images"
REPORT_FOLDER = "reports"
REPORT_FILE = os.path.join(REPORT_FOLDER, "qr_scan_report.md")

SUSPICIOUS_KEYWORDS = ["http://", "bit.ly", "tinyurl", "goo.gl", "qrco.de"]

def extract_qr_data(image_path):
    try:
        img = Image.open(image_path)
        results = decode(img)
        return [r.data.decode("utf-8") for r in results]
    except Exception as e:
        return [f"Error decoding {image_path}: {str(e)}"]

def analyze_qr_data(data):
    if any(keyword in data.lower() for keyword in SUSPICIOUS_KEYWORDS):
        return "⚠️ Suspicious", "High"
    if data.startswith("https://"):
        return "✅ Safe", "Low"
    return "❓ Unknown", "Medium"

def main():
    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)

    with open(REPORT_FILE, "w") as report:
        report.write("# QR Code Scan Report\n\n")
        report.write("| File | QR Data | Status | Risk |\n")
        report.write("|------|---------|--------|------|\n")

        for file in os.listdir(QR_FOLDER):
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                path = os.path.join(QR_FOLDER, file)
                qr_data_list = extract_qr_data(path)

                if not qr_data_list:
                    report.write(f"| {file} | No QR code found | ❌ Failed | High |\n")
                    continue

                for qr_data in qr_data_list:
                    status, risk = analyze_qr_data(qr_data)
                    report.write(f"| {file} | {qr_data} | {status} | {risk} |\n")

    print(f"Report generated: {REPORT_FILE}")

if __name__ == "__main__":
    main()
