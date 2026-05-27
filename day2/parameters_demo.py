# 注意：这里是小写的 openai，导入的是首字母大写的 OpenAI
from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="your_api_key",  # 替换成你自己的DeepSeek API Key
    base_url="https://api.deepseek.com"
)

print("客户端初始化成功!")
print("🧠 理解 temperature 参数")
print("=" * 50)
question = "请解释一下 temperature 参数在生成式模型中的作用。"

# 低温度 - 稳定保守
print("\n❄️ temperature=0.1 (稳定保守，每次回答都类似):")
print("-" * 40)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": question}],
    temperature=0.1,
    max_tokens=150
)
print(response.choices[0].message.content)

# 高温度 - 创意多样
print("\n🔥 temperature=1.5 (创意多样，每次回答都不同):")
print("-" * 40)
response_high = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": question}],
    temperature=1.5,
    max_tokens=150
)
print(response_high.choices[0].message.content)

print("\n💡 总结：")
print("- temperature=0.1: 回答稳定，适合需要准确答案的场景")
print("- temperature=1.5: 回答富有创意，适合头脑风暴和创意写作")