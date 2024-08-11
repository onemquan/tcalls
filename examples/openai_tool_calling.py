import json

import openai

from tcalls.openai_tool_call import get_openai_tool_schema


def get_weather(city: str) -> str:
    """Get the current weather temperature for a giving city."""
    return f"The {city} current weather temperature is 35 °C"


tools = [get_openai_tool_schema(get_weather)]

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Hi, please show current weather, I am in Shanghai."},
]

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)


finish_reason = response.choices[0].finish_reason
print(f"finish_reason: {finish_reason}")
tool_call = response.choices[0].message.tool_calls[0]
name = tool_call.function.name
arguments = json.loads(tool_call.function.arguments)

if name == "get_weather":
    print(get_weather(**arguments))
