import time

from google import genai
from config import AI_API_KEY


client = genai.Client(
    api_key=AI_API_KEY
)

chat = client.chats.create(
    model="gemini-3.6-flash"
)


SYSTEM_PROMPT = """
You are Jarvis, a fast desktop voice assistant.

Give short and useful answers.
Keep normal answers under 3 sentences.
Do not use Markdown.
Do not use bullet points unless necessary.
Speak naturally because your response will be read aloud.
If the user asks for an explanation, keep it simple and concise.
"""


def ask_ai(prompt):

    message = f"""
{SYSTEM_PROMPT}

User: {prompt}

Jarvis:
"""

    for attempt in range(2):

        try:

            response = chat.send_message(
                message
            )

            if response and response.text:

                return response.text.strip()

            return "I couldn't generate a response."

        except Exception as e:

            print(
                f"AI attempt {attempt + 1} failed: {e}"
            )

            if attempt == 0:

                time.sleep(0.5)

            else:

                return (
                    "Sorry, the AI service is "
                    "temporarily unavailable."
                )