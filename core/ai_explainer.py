import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def explain_vulnerability(scan_result):
    """
    Uses OpenAI GPT to explain vulnerabilities and mitigation
    """
    prompt = f"""
    You are an ethical hacker AI assistant.
    Analyze the following scan result and provide:
    1. Clear explanation of potential security risks
    2. Recommended mitigation steps
    Scan result: {scan_result}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        explanation = response['choices'][0]['message']['content']
    except Exception as e:
        explanation = f"AI explanation failed: {str(e)}"

    return explanation
