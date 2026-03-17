import openai
import os
from utils.logger import logger

# Set API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "NOT_SET")

def generate_ai_report(raw_output: str) -> str:
    """
    Generates a security report using AI based on nmap results.
    """
    if openai.api_key == "NOT_SET":
        logger.warning("OpenAI API key not set. Returning placeholder report.")
        return f"# AI Vulnerability Report (Placeholder)\n\nNmap output provided, but no OpenAI API key found.\n\n## Raw Output Summary:\n```\n{raw_output[:500]}...\n```\nPlease set OPENAI_API_KEY to get AI insights."

    prompt = f"""
You are a cybersecurity analyst.

Explain the following Nmap scan in simple human language.
Include:
- Open ports explanation
- Possible vulnerabilities
- Risk level
- Suggested remediation

Nmap Output:
{raw_output}
"""

    try:
        logger.info("Requesting report from OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # Using 3.5-turbo as it's faster and cheaper for general scanning
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        logger.info("AI report generated successfully.")
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Failed to generate AI report: {e}")
        return f"# AI Report Error\n\nCould not generate report due to: {str(e)}\n\n## Raw Scan:\n```\n{raw_output}\n```"
