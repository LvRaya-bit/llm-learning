from openai import OpenAI

client = OpenAI(
    api_key="your_api_key",  # 替换成你自己的DeepSeek API Key
    base_url="https://api.deepseek.com"
)

print("=" * 60)
print("💬 多轮对话演示 - 记住上下文")
print("=" * 60)

# 维护对话历史
conversation = []

# 第一轮对话
print("\n📌 第1轮对话")
user_input = "我叫小明，我今年25岁，我喜欢学习Python"
print(f"👤 用户: {user_input}")

conversation.append({"role": "user", "content": user_input})

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=conversation
)

ai_response = response.choices[0].message.content
print(f"🤖 AI: {ai_response}")
conversation.append({"role": "assistant", "content": ai_response})

# 第二轮对话 - 测试是否记住上文
print("\n📌 第2轮对话 - 测试记忆")
user_input = "我刚才说我叫什么名字？今年多大？"
print(f"👤 用户: {user_input}")

conversation.append({"role": "user", "content": user_input})

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=conversation
)

ai_response = response.choices[0].message.content
print(f"🤖 AI: {ai_response}")

print("\n✅ 如果AI正确回答了'小明'和'25岁'，说明记住了上下文！")
print("\n💡 多轮对话原理：")
print("- 每次调用都把完整的对话历史传给API")
print("- AI根据历史消息理解上下文")
print("- 重要：对话历史会消耗更多tokens")
print(f"   - 总计token: {response.usage.total_tokens}")