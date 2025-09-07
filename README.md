# 🔐 Mailcious_QR_scan_CI_CD
Mailcious_QR_scan_CI_CD is a GitHub Actions workflow that automatically scans QR codes stored in an image folder during each commit or manual trigger. The workflow analyzes QR codes for potentially malicious links, phishing attempts, or unsafe redirects, and generates a detailed security report as a CI/CD artifact.









![logo](https://github.com/user-attachments/assets/5ccf6f4b-6e3d-4472-be96-75ddda499fbd)





In today’s digital landscape, attackers are increasingly leveraging **social engineering vectors** such as **QR codes** embedded in documents and images to deliver **phishing links, malicious payloads, or hidden scripts**. While CI/CD pipelines accelerate software delivery, they can also become a weak link if weaponized content slips through undetected.  

Traditional malware scanners often miss **steganography-based QR payloads** or **obfuscated links**, leaving organizations vulnerable to exploitation. With the growing reliance on QR codes in business workflows, ensuring **proactive detection and remediation** has become an essential part of **DevSecOps practices**.  

---

## 🚀 Project Overview

To address this gap, we developed a **GitHub Actions workflow** that automatically:  

- 🔍 Scans images and documents (`.jpg`, `.png`, `.pdf`) for hidden QR codes.  
- 📖 Extracts and analyzes QR code content for suspicious or malicious patterns.  
- ⚠️ Flags potential threats such as phishing URLs or encoded payloads.  
- 📝 Generates detailed security reports as CI/CD artifacts for auditing and remediation.  

This project demonstrates how **automated QR code threat detection** can be embedded into a CI/CD pipeline, helping organizations strengthen their **supply chain security** and prevent attacks before deployment.  

---

## 📌 Introduction  

QR codes are widely used for convenience, but they are also being exploited as a **threat vector**.  
This project, **Mailcious_QR_scan_CI_CD**, was designed to secure CI/CD pipelines by **automatically scanning for malicious QR codes in uploaded files**.  

By integrating QR scanning and payload analysis directly into **GitHub Actions**, the workflow ensures that no hidden QR-based attack is deployed into production.  
The output is a **security report** that flags any suspicious findings, enabling quick response and remediation.  

---

## ✨ Key Features  

- 📄 Scans `.pdf`, `.jpg`, and `.png` files for embedded QR codes.  
- 🔐 Extracts QR data and analyzes it for **malicious links or hidden scripts**.  
- ⚙️ Runs automatically in **GitHub Actions** as part of the CI/CD pipeline.  
- 📊 Generates **security reports** for auditing and compliance.  


---

## 📂 File Structure  



```bash
.
Mailcious_QR_scan_CI_CD-main/
│── LICENSE                  # Open-source license for usage
│── README.md                # Project documentation
│── requirements.txt         # Python dependencies
│
├── .github/
│   └── workflows/
│       └── qr_scan.yml      # GitHub Actions workflow definition
│
├── scripts/
│   └── scan_qr.py           # Main QR scanning logic
│
├── qr_images/               # Sample test files containing QR codes
│   ├── my_doc.pdf
│   ├── qr_01.jpg
│   ├── qr_02.jpg
│   ├── qr_03.jpg
│   └── qr_04.jpg
│
├── reports/                 # Security scan reports
│   └── example.txt

```

**Explanation of structure:**  
- **`.github/workflows`** → CI/CD pipeline that triggers scans automatically on each commit.  
- **`docker/`** → Contains the Dockerfile and app to be scanned.  
- **`scripts/`** → Automation scripts for generating reports and framework mappings.  
- **`assets/`** → Images and charts used in PDF reporting.  
- **`reports/`** → Stores raw JSON scan results and final consolidated outputs.  
- **`requirements.txt`** → Lists dependencies (ReportLab, Matplotlib, etc.).  
- **`report.pdf`** → The final professional security report.  

---

## 🛠️ Technology Used  

- **Backend:** Python (QR detection, decoding, content analysis).  
- **Libraries/Tools:**  
  - OpenCV / Pyzbar → Detect and decode QR codes.  
  - ReportLab → Generate structured PDF reports.  
  - Regex / Custom Rules → Identify malicious or suspicious QR patterns.  
- **CI/CD:** GitHub Actions (automated scans in the pipeline).  
- **Testing Files:** Sample `.pdf` and `.jpg` documents containing QR codes for validation.  

---

## ⚙️ Workflow & Tools Used  

The GitHub Actions workflow (`.github/workflows/qr_scan.yml`) automates the QR code scanning pipeline. It runs automatically whenever files are pushed to the repository.

### 🔹 1. Install Dependencies
```yaml
- name: Install Dependencies
  run: pip install -r requirements.txt
```
- Tool: Docker
- Purpose: Builds the application container image from the Dockerfile inside the ./docker directory.
- Output: A containerized application (my-custom-app:latest) that is ready for security scanning.


### **2. Run QR Scan Script**
```yaml
- name: Run QR Scanner
  run: python scripts/scan_qr.py --input ./qr_images --output ./reports
```
- Tool: scan_qr.py
- Purpose: Scans `.jpg`, `.png`, and `.pdf` files for QR codes, decodes them, and extracts embedded data.

### 🔹 3. Content Analysis

- Identifies malicious URLs, encoded payloads, or hidden scripts within QR data.
- Uses regex rules and keyword checks (e.g., `http://`, `base64`, suspicious domains).
- Flags risky patterns for further inspection. 


### 🔹 4. Report Generation

- Generates `.txt` and optional PDF reports with flagged findings.
- Summarizes:
- File scanned
- QR content
- Suspicion level (Safe / Suspicious / Malicious)

### 🔹 5. Upload Artifacts

```
- name: Upload Scan Report
  uses: actions/upload-artifact@v4
  with:
    name: qr-security-report
    path: reports/

```

- Purpose: Makes reports available as GitHub CI/CD artifacts for download and review.







---

## 🎯 Purpose  
The primary purpose of this project is to:  

- Embed QR code threat detection directly into CI/CD pipelines.
- Prevent phishing and malicious payload delivery via QR codes.
- Provide security teams with quick remediation insights.
- Align findings with DevSecOps principles for continuous security.


---

## ✅ Advantages  


- **Automated**: Runs on every push via GitHub Actions.
- **Focused**: Specially designed to catch QR-based attack vectors.
- **Lightweight**: Uses Python + open-source libraries.
- **Actionable Reports**: Generates CI/CD artifacts for auditing.
- **Integrable**: Can be extended with external threat intelligence feeds.

---

## ⚡ Challenges Faced  

1. **False Positives**: Benign QR codes flagged due to generic patterns.
2. **PDF Scanning**: Extracting embedded images from PDFs required extra parsing.
3. **Content Obfuscation**: Detecting malicious intent in encoded QR payloads.
4. **CI/CD Artifacts**: Ensuring reports were consistent and easy to interpret.

---

## 🖼️ Sample Report Preview  

Below is a preview of the kind of report generated by the scanner:  

![Download Vulnerability Test Report](https://github.com/ADITYADAS1999/Mailcious_QR_scan_CI_CD/actions/runs/17493757847/artifacts/3937089225)  

The PDF includes:  
- Vulnerability summary tables.  
- Severity distribution charts.  
- Type of threat detected (e.g., phishing URL, malicious script, unsafe function)
- Risk level (High / Medium / Low / Safe)
- Final consolidated recommendations.  

---

## 🔚 Conclusion  
Mailcious_QR_scan_CI_CD strengthens CI/CD pipelines by detecting hidden QR code threats before they reach production. By combining automated scanning, content analysis, and report generation, it provides a practical DevSecOps tool for mitigating QR-based risks.

Future Work:  
- Enhance detection with machine learning–based URL risk scoring.
- Integrate with threat intelligence feeds for real-time blacklists.
- Extend support for encrypted QR codes and multi-layer steganography.

---

## 📜 License  
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.  






