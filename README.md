# 🛡️ A3VS – Advanced Automated Authenticated AI-based Vulnerability Scanner

A3VS is a professional-grade network security auditing tool that combines the power of **Nmap** with **Artificial Intelligence (LLM)** to provide insightful, human-readable vulnerability reports.

## 🚀 New & Advanced Features

- 🖥️ **Modernized GUI:** Enhanced PyQt5 interface with professional styling and real-time status bar.
- ⚡ **Asynchronous Architecture:** Non-blocking Nmap scanning and AI report generation using multi-threading.
- 🔄 **Real-time Progress:** Intelligent parsing of Nmap `--stats-every` output for accurate percentage tracking.
- 🔐 **Secure Execution:** Sanitized command construction without shell injection risks.
- 🤖 **AI-Driven Analysis:** Summarizes complex Nmap outputs into actionable security advice.
- 📄 **Dual Reporting:** Automatic generation of both **Markdown** and **PDF** reports.
- 🪵 **Centralized Logging:** Detailed logs of all scan operations for auditing.

---

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/A3VS.git
    cd A3VS
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Environment:**
    Create a `.env` file (optional) or export your OpenAI API Key:
    ```bash
    export OPENAI_API_KEY="your-key-here"
    ```

4.  **Run A3VS:**
    ```bash
    python3 src/main.py
    ```

---

## 🛠️ How It Works

1.  **Scan Configuration:** Choose from several scan profiles (Quick, Full, Vulnerability, Service Discovery).
2.  **Authentication:** (Optional) Provide credentials for authenticated NSE script execution.
3.  **Streaming Output:** Watch the Nmap output in real-time within the integrated console.
4.  **AI Post-Processing:** Once the scan finishes, the raw data is sent to an LLM to generate a plain-English report.
5.  **Report Export:** Access your results in the `reports/` directory in both text and PDF formats.

---

## ⚠️ Disclaimer

This project is intended for **ethical security auditing** and **academic research**. Unauthorized scanning of networks you do not own or have explicit permission to audit is illegal. The authors are not responsible for any misuse.

---

*Stay Secure. Stay Informed.*
