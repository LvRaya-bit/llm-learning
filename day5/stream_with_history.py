from openai import OpenAI

client = OpenAI(
    api_key="你的API-Key",
    base_url="https://api.deepseek.com"
)

conversation = []

def stream_chat(question):
    conversation.append({"role": "user", "content": question})
    print(f"\n🤖 AI: ", end="", flush=True)
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=conversation,
        stream=True
    )
    
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content
    
    conversation.append({"role": "assistant", "content": full_response})
    print()

while True:
    user_input = input("\n👤 你: ")
    if user_input == 'quit':
        break
    elif user_input == 'clear':
        conversation = []
        print("历史已清空")
        continue
    stream_chat(user_input)