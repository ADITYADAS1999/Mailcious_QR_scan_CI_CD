# Mailcious_QR_scan_CI_CD
Mailcious_QR_scan_CI_CD is a GitHub Actions workflow that automatically scans QR codes stored in an image folder during each commit or manual trigger. The workflow analyzes QR codes for potentially malicious links, phishing attempts, or unsafe redirects, and generates a detailed security report as a CI/CD artifact.









![logo](https://github.com/user-attachments/assets/5ccf6f4b-6e3d-4472-be96-75ddda499fbd)


# 🔐 Mailcious_QR_scan_CI_CD


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

- **Backend:** Python (scripts for scanning, mapping, and report generation).  
- **Frontend/Reports:**  
  - ReportLab → To generate structured PDF reports.  
  - Matplotlib → To generate severity charts and visual data.  
- **Security Tools:**  
  - **Trivy** → Detects vulnerabilities in Docker images.  
  - **Bandit** → Analyzes Python code for common security issues.  
  - **Docker Scout** → Checks image dependencies against known CVEs.  
- **Frameworks:**  
  - **NIST CSF** → Compliance & categorization.  
  - **MITRE ATT&CK** → Threat actor technique mapping.  
  - **OWASP Top 10** → Common web application risks.  
- **CI/CD:** GitHub Actions (automated scans in pipeline).  
- **Containerization:** Docker (for image builds and scans).  

---

## ⚙️ Workflow & Tools Used  

This project includes a **GitHub Actions workflow** (`.github/workflows/docker-scan.yml`) that automates the **DevSecOps security pipeline**.  
The workflow runs automatically on every push to the `main` branch and executes the following stages:  

---

### 🔹 1. Build Docker Image  
```yaml
- name: Build Docker Image
  run: docker build -t my-custom-app:latest ./docker
```
- Tool: Docker
- Purpose: Builds the application container image from the Dockerfile inside the ./docker directory.
- Output: A containerized application (my-custom-app:latest) that is ready for security scanning.


### 🔹 2. Trivy (Docker Image Vulnerability Scanner)

```
- name: Run Trivy Docker Scan
  run: trivy image --ignore-unfixed --exit-code 0 --format json --output reports/trivy.json my-custom-app:latest
```
- Tool: Trivy
- Purpose: Scans the built Docker image for known vulnerabilities (CVEs) in OS packages and dependencies.
- Output: reports/trivy.json → JSON report containing vulnerability details with severity levels.

### 🔹 3. Bandit (Python Source Code Analysis)

```
- name: Run Bandit Scan
  run: bandit -ll -ii -r . -f json -o reports/bandit.json || true
```
- Tool: Bandit
- Purpose: Performs Static Application Security Testing (SAST) for Python source code.
- Detects issues such as:
-Insecure function usage (eval, exec)
-Hardcoded credentials
-Insecure file permissions
- Output: reports/bandit.json → JSON report of security issues in code.


### 🔹 4. Docker Scout (Optional Dependency Scanner)

```
# docker scout quickview
# docker scout cves
```
- Tool: Docker Scout
- Purpose: Provides insights into container dependencies, image provenance, and supply chain vulnerabilities.
- Benefit: Complements Trivy by analyzing image layers and dependencies more deeply.

### 🔹 5. MITRE ATT&CK (Atomic Red Team Simulation)

```
- name: Run Atomic Red Team (MITRE ATT&CK)
  shell: pwsh
  run: |
    git clone https://github.com/redcanaryco/atomic-red-team.git
    git clone https://github.com/redcanaryco/invoke-atomicredteam.git
    Import-Module ./invoke-atomicredteam/Invoke-AtomicRedTeam.psd1 -Force
    Invoke-AtomicTest T1003 ...
```
- Tools:
-Atomic Red Team
-Invoke-AtomicRedTeam

- Purpose: Simulates MITRE ATT&CK techniques against the container or application.
- Example: T1003 – Credential Dumping test.
- Output: reports/mitre_T1003.json → JSON report mapping vulnerabilities to real-world adversarial behaviors.

### 🔹 6. NIST CSF Mapping

```
- name: Map Results to NIST CSF
  run: python scripts/mappings.py reports/ nist_report.json
```

- Purpose: Maps scan results from Trivy, Bandit, and MITRE ATT&CK into NIST Cybersecurity Framework (CSF) categories:
- Identify → Asset discovery issues
- Protect → Missing patches, insecure configs
- Detect → Intrusion detection gaps
- Respond/Recover → Response & recovery mechanisms

### 🔹 7. Report Generation (Charts + PDF)

```
- name: Generate Charts
  run: python scripts/gen_charts.py

- name: Generate PDF Report
  run: python scripts/generate_report.py
```
- Purpose: Produces a professional PDF report consolidating:
- Vulnerability details
- Severity breakdown (with charts)
- NIST CSF mapping
- MITRE ATT&CK mapping
- OWASP Top 10 mapping


### 🔹 8. Upload Artifacts

```
- name: Upload PDF Report
  uses: actions/upload-artifact@v4
  with:
    name: docker-vulnerability-report
    path: report.pdf
```

- Purpose: Uploads both the PDF report and raw JSON reports as GitHub build artifacts.
- Benefit: Results can be downloaded and reviewed by security teams after each workflow run.






## ⚡ Security Framework Integration  

### 🔹 NIST Cybersecurity Framework (CSF)  
The **NIST CSF** provides five functions: **Identify, Protect, Detect, Respond, Recover**.  
Each vulnerability is automatically mapped to one of these functions.  
For example:  
- A missing patch may map to **Protect**.  
- An insecure API exposure may map to **Detect/Respond**.  

This ensures findings are not just technical but **aligned with compliance requirements**.  

### 🔹 MITRE ATT&CK  
The **MITRE ATT&CK** knowledge base describes how attackers exploit systems.  
Vulnerabilities detected are mapped to adversarial techniques.  
For example:  
- Credential leakage → **T1003 (Credential Dumping)**.  
- Insecure file permissions → **T1078 (Valid Accounts)**.  

This allows security teams to understand **how real attackers might exploit vulnerabilities**.  

### 🔹 OWASP Top 10  
The **OWASP Top 10** is an industry-standard list of the most critical web application risks.  
This scanner maps findings to OWASP categories, such as:  
- **A01: Broken Access Control**  
- **A03: Injection Attacks**  
- **A04: Insecure Design**  

This helps prioritize remediation according to **global best practices**.  

---

## 🎯 Purpose  
The primary purpose of this project is to:  
- **Automate vulnerability management** for Dockerized applications.  
- Provide a **single, consolidated PDF report** instead of multiple scattered outputs.  
- Help developers, DevOps, and security teams **integrate security into CI/CD pipelines (DevSecOps)**.  
- Align findings with **compliance frameworks and attacker models**.  

---

## ✅ Advantages  

- **Automated** → Scans run automatically with every code push (via GitHub Actions).  
- **Comprehensive** → Covers Docker images, source code, and dependencies.  
- **Framework-Aware** → Maps to NIST CSF, MITRE ATT&CK, and OWASP Top 10.  
- **Professional Reports** → PDF reports with charts, severity analysis, and framework mappings.  
- **Open-Source & Extensible** → Easily add new scanners or frameworks.  

---

## ⚡ Challenges Faced  

1. **Data Normalization** → Different scanners produce JSON in different formats.  
2. **Framework Mapping** → Consistently mapping vulnerabilities across NIST, MITRE, and OWASP required custom logic (`mappings.py`).  
3. **PDF Reporting** → Ensuring the final report is clear, visual, and boardroom-ready.  
4. **Automation in CI/CD** → Ensuring scans work smoothly within GitHub Actions with minimal setup.  

---

## 🖼️ Sample Report Preview  

Below is a preview of the kind of report generated by the scanner:  

![Download Vulnerability Test Report](https://github.com/ADITYADAS1999/Automated-Docker-Security-Scanner/blob/main/vulnerability_report.pdf)  

The PDF includes:  
- Vulnerability summary tables.  
- Severity distribution charts.  
- NIST CSF, MITRE ATT&CK, OWASP Top 10 mappings.  
- Final consolidated recommendations.  

---

## 🔚 Conclusion  
The **Automated Docker Security Scanner** provides a **complete security assessment workflow** for containerized applications.  
By integrating scanning tools with industry-standard frameworks, it transforms raw scan data into **actionable insights** that can guide both developers and security teams.  

Future Work:  
- Add real-time **CVE database lookups**.  
- Build a **web dashboard** for interactive vulnerability tracking.  
- Extend support for more programming languages (Go, Java, etc.).  

---

## 📜 License  
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.  






