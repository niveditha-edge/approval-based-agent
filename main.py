
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def prepare_action(request: str) -> str:
    """
    Generate a personalized letter using Groq AI.
    Missing details must remain placeholders.
    """

    if not request or not request.strip():
        raise ValueError("Please provide a request.")

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Check your .env file."
        )

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional writing assistant. "
                    "Create a complete, polite, professional letter "
                    "based on the user's request. "
                    "Never invent dates, names, diagnoses, reasons, "
                    "or other personal details. "
                    "If information is missing, use clear placeholders "
                    "such as [Start Date], [End Date], "
                    "[Manager Name], and [Your Name]. "
                    "Do not assume today's date or calculate dates "
                    "unless the user provides the necessary information. "
                    "Do not claim that a manager has approved a request. "
                    "Include a subject, greeting, body, and closing. "
                    "Return plain text without Markdown formatting."
                )
            },
            {
                "role": "user",
                "content": request.strip()
            }
        ],
        temperature=0.2
    )

    draft = response.choices[0].message.content

    if not draft or not draft.strip():
        raise ValueError("The AI returned an empty draft.")

    return draft.strip()


def execute_action(letter: str) -> str:
    """
    Prepare the approved letter for download.
    This function does not send an email.
    """

    if not letter or not letter.strip():
        raise ValueError("Cannot execute an empty letter.")

    return f"Approved letter is ready for download:\n\n{letter}"
