"""
Day 3 - 第一步：最简单的Function Calling例子
理解AI如何选择工具
"""

from openai import OpenAI
import json

client = OpenAI(
    api_key="你的DeepSeek-API-Key",
    base_url="https://api.deepseek.com"
)

print("=" * 60)
print("最简单的Function Calling示例")
print("=" * 60)

# 定义工具
tools = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "执行数学计算",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "数学表达式"
                }
            },
            "required": ["expression"]
        }
    }
}]

# 测试
user_input = "帮我算一下 25 乘以 4"
print(f"\n用户：{user_input}")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": user_input}],
    tools=tools
)

ai_msg = response.choices[0].message

if ai_msg.tool_calls:
    tool_call = ai_msg.tool_calls[0]
    print(f"AI决定调用：{tool_call.function.name}")
    print(f"参数：{tool_call.function.arguments}")
else:
    print(f"AI直接回答：{ai_msg.content}")