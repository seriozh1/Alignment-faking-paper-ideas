from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

api_thing = Anthropic(api_key=api_key)

messages = [{"role": "user", "content": "Hello there, AI!"}]

response = api_thing.messages.create(
   model="claude-3-7-sonnet-latest",
   max_tokens=4096,
   messages=messages
)

print(response.content[0].text)