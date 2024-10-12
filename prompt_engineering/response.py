import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("GITHUB_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
model = "gpt-4o-mini"
message_limit = 200 # 200 char limit (for now, may bump)

client = OpenAI(
    base_url=endpoint,
    api_key=api_key,
)

def get_response(user_msg, system_prompt) -> str:
    if len(user_msg) > message_limit:
        return f"message limit of {message_limit} chars exceeded"

    response = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_msg,
            }
        ],
        model = model
    )

    response_msg = response.choices[0].message.content

    if response_msg is None:
        return "response failed"
    else:
        return response_msg
