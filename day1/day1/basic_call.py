from openai import OpenAI

# 初始化客户端（记得替换成你的真实API Key）
client = OpenAI(
    api_key="sk-b0531c63b0d74c5fa10f75509c6ff455",  # 这里替换成你的真实key
    base_url="https://api.deepseek.com"
)

print("=" * 50)
print("🤖 第一次API调用")
print("=" * 50)

# 最简单的API调用
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "帮我写一个pytest测试用例，测试加法函数"}
    ]
)

print("\n📥 LLM返回的内容：")
print("=" * 50)
print(response.choices[0].message.content)
print("=" * 50)

# 打印token使用情况
print(f"\n📊 Token使用：")
print(f"   - 输入token: {response.usage.prompt_tokens}")
print(f"   - 输出token: {response.usage.completion_tokens}")
print(f"   - 总计token: {response.usage.total_tokens}")
