import os

import openai
from dotenv import load_dotenv

flag = "some_flag!!"

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": "say this is a test",
            }
        ],
        model="gpt-3.5-turbo"
    )

print(chat_completion)
