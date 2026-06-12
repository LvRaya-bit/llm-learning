from openai import OpenAI

client = OpenAI(
    api_key="你的API-Key",
    base_url="https://api.deepseek.com"
)

print("普通模式：")
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "用一句话介绍Python"}],
    stream=False
)
print(response.choices[0].message.content)

print("\n流式模式：")
print(">>> ", end="")
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "用一句话介绍Python"}],
    stream=True
)
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()