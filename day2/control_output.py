from openai import OpenAI

client = OpenAI(
    api_key="your_api_key",
    base_url="https://api.deepseek.com"
)

print("=" * 60)
print("🎨 控制输出格式")
print("=" * 60)

# 示例1：强制JSON输出
print("\n📋 示例1：JSON格式输出")
print("-" * 40)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个数据提取专家，必须用JSON格式返回，不要有任何其他文字"},
        {"role": "user", "content": """
        从这段话提取信息：
        用户张三，今年28岁，职业是软件工程师，喜欢编程和羽毛球
        
        返回格式：{"name": "姓名", "age": 年龄, "job": "职业", "hobbies": ["爱好1", "爱好2"]}
        """}
    ],
    temperature=0.3
)

print(response.choices[0].message.content)

# 示例2：代码生成
print("\n\n💻 示例2：只生成代码，不要解释")
print("-" * 40)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个代码生成器，只返回Python代码，不要有任何解释文字"},
        {"role": "user", "content": "生成一个计算斐波那契数列的函数"}
    ],
    temperature=0.2,
    max_tokens=300
)

print(response.choices[0].message.content)

print("\n💡 控制输出技巧：")
print("1. 用system prompt明确指定输出格式")
print("2. 使用低temperature保证格式稳定")
print("3. 在prompt中给出格式示例")