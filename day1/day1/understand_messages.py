from openai import OpenAI

client = OpenAI(
    api_key="你的DeepSeek-API-Key",  # 替换成你的真实key
    base_url="https://api.deepseek.com"
)

print("=" * 60)
print("📝 理解 messages 结构")
print("=" * 60)

# 示例1：只有user
print("\n📌 示例1: 只有 user role")
print("-" * 40)
response1 = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "什么是pytest？"}
    ],
    max_tokens=100
)
print(f"回复: {response1.choices[0].message.content}")

# 示例2：system + user
print("\n📌 示例2: system + user role")
print("-" * 40)
response2 = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个专业的测试工程师，回答要简洁专业，不超过50字"},
        {"role": "user", "content": "什么是pytest？"}
    ],
    max_tokens=100
)
print(f"回复: {response2.choices[0].message.content}")

# 解释三种role的作用
print("\n" + "=" * 60)
print("💡 三种role的作用：")
print("=" * 60)
print("""
1. system（系统）：
   - 设置AI的行为准则和角色定位
   - 优先级最高，贯穿整个对话
   
2. user（用户）：
   - 用户的问题或指令
   - 每次对话的核心输入
   
3. assistant（助手）：
   - AI生成的回复
   - 用于多轮对话时提供上下文
""")
