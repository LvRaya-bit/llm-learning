from openai import OpenAI

client = OpenAI(
    api_key="你的API-Key",
    base_url="https://api.deepseek.com"
)

def stream_chat(question):
    print(f"\n🤖 AI: ", end="", flush=True)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": question}],
        stream=True
    )
    for chunk in response:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()

while True:
    user_input = input("\n👤 你: ")
    if user_input == 'quit':
        break
    stream_chat(user_input)