import openai

openai.api_key = "PUT_YOUR_API_KEY_HERE"

def generate_ai_report(raw_output: str) -> str:
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

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
