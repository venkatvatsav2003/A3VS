# 🛡️ A3VS – Automated Authenticated AI-based Vulnerability Scanner

A3VS (Automated Authenticated AI-based Vulnerability Scanner) is a **Python-based graphical vulnerability assessment tool** that automates **Nmap and the Nmap Scripting Engine (NSE)** for network scanning and vulnerability detection.  
It enhances traditional scanning by providing **real-time scan progress**, **authenticated scanning support**, and **AI-generated human-readable security reports**, including **PDF export**.

This project is intended for **ethical security auditing, academic research, and cybersecurity learning**.

---

## 🚀 Key Features

- 🖥️ GUI-based vulnerability scanner (PyQt5)
- ⚡ Quick, Full, and Vulnerability scan modes
- 🔄 Real-time scan progress with percentage bar
- 🔐 Authenticated scanning support (where applicable)
- 🤖 Offline AI-based vulnerability explanation (Local LLM)
- 📄 Human-readable reports (Markdown + PDF)
- 📊 Automated Nmap & NSE script execution
- 🧩 Modular and extensible architecture
- ⚠️ Ethical-use disclaimer included

---

## 🧠 How A3VS Works (Workflow)

1. User enters a **target IP address or domain**
2. Selects a **scan type** (Quick / Full / Vulnerability)
3. (Optional) Provides **authentication credentials**
4. A3VS:
   - Executes Nmap with curated NSE scripts
   - Tracks scan progress in real time
   - Collects raw scan output
5. An **offline AI (Local LLM)** analyzes the results
6. Generates:
   - Raw scan output (`.txt`)
   - Human-readable report (`.md`)
   - Professional PDF report (`.pdf`)

---





This project is released for educational and research purposes.
Refer to the disclaimer before use.
