import os
from dotenv import load_dotenv
from google import genai


# Load .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")


# Create Gemini client
client = genai.Client(api_key=api_key)


def analyze_document(text):
    prompt = f"""
Analyze the following document.

Give the result in this format:

Document Type:
Main Topic:
Summary:
AI Generated Probability:
Reason:

Document:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    print("AI Analyzer is working!")