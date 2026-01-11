A3VS – Automated Authenticated AI-based Vulnerability Scanner

A3VS (Automated Authenticated AI-based Vulnerability Scanner) is a Python-based graphical vulnerability assessment tool that automates Nmap and Nmap Scripting Engine (NSE) for network scanning and vulnerability detection.
It enhances traditional scanning by providing real-time scan progress, authenticated scanning support, and AI-generated human-readable security reports, including PDF export.

This project is designed for ethical security auditing, academic research, and cybersecurity learning.

🚀 Key Features

🖥️ GUI-based vulnerability scanner (PyQt5)

⚡ Quick, Full, and Vulnerability scan modes

🔄 Real-time scan progress with percentage bar

🔐 Authenticated scanning support (where applicable)

🤖 Offline AI-based vulnerability explanation (Local LLM)

📄 Human-readable reports (Markdown + PDF)

📊 Automated Nmap & NSE script execution

🧩 Modular & extensible architecture

⚠️ Ethical-use disclaimer included

🧠 How A3VS Works (High-Level Workflow)

User enters a target IP address or domain

Selects a scan type (Quick / Full / Vulnerability)

(Optional) Provides authentication credentials

A3VS:

Executes Nmap with curated NSE scripts

Tracks scan progress in real time

Collects raw scan output

An offline AI (Local LLM) analyzes results

Generates:

Raw scan output (.txt)

Human-readable report (.md)

Professional PDF report (.pdf)

📂 Project Structure
A3VS/
├── src/
│   ├── main.py
│   ├── gui/
│   │   └── main_gui.py
│   ├── scanner/
│   │   ├── nmap_runner.py
│   │   ├── progress_tracker.py
│   │   └── auth_scanner.py
│   ├── ai/
│   │   ├── report_generator.py
│   │   └── pdf_generator.py
│   └── config/
│       └── scan_profiles.py
├── reports/
│   ├── raw_scan.txt
│   ├── final_report.md
│   └── final_report.pdf
├── assets/
├── requirements.txt
├── README.md
└── DISCLAIMER.md

🧪 Scan Types Supported
Scan Type	Description
Quick Scan	Fast scan to check host availability and common ports
Full Scan	Scans a large port range with service & OS detection
Vulnerability Scan	Uses Nmap NSE scripts to detect known vulnerabilities
🤖 AI-Based Reporting (Offline)

A3VS integrates a local Large Language Model (LLM) using Ollama, enabling:

Fully offline AI processing

No API keys required

Privacy-preserving vulnerability analysis

Simple explanations for non-security users

The AI converts raw Nmap output into:

Open-port explanations

Risk assessment (Low / Medium / High)

Potential vulnerability insights

Recommended mitigation steps

🧾 PDF Report Export

After every scan, A3VS automatically generates a professional PDF report, suitable for:

Security audits

Academic submission

Documentation

Sharing with stakeholders

⚙️ Requirements
Software

Python 3.10+

Nmap 7.95+

Ollama (for offline AI)

Python Dependencies

Install using:

python -m pip install -r requirements.txt


requirements.txt

PyQt5
requests
reportlab

▶️ How to Run
cd src
python main.py

⚠️ Input Guidelines

Enter only IP address or domain

❌ Do NOT include http:// or https://

✅ Example:

scanme.nmap.org
192.168.1.1

🔐 Ethical Usage Disclaimer

This tool is intended only for educational purposes and authorized security testing.

Do NOT scan:

Systems you do not own

Networks without explicit permission

The authors are not responsible for misuse.

Refer to DISCLAIMER.md
 for details.

📊 Academic Relevance

This project aligns with:

Network Security

Ethical Hacking

Vulnerability Assessment

Automation in Cybersecurity

AI-assisted Security Auditing

It supports IEEE-style research and implementation.

📌 Future Enhancements

Attack Surface Management (ASM)

CVE database enrichment

Scan comparison (before vs after)

Dashboard (Web UI)

Endpoint & API scanning

Advanced AI risk scoring

👨‍💻 Author

Venkat Vatsav
Cybersecurity Enthusiast | Ethical Security Researcher

GitHub:
👉 https://github.com/venkatvatsav2003

⭐ Acknowledgements

Nmap & NSE community

Open-source cybersecurity researchers

Ollama & Local LLM ecosystem

📜 License

This project is released for educational and research purposes.
Refer to the disclaimer before use.
