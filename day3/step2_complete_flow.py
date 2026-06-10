"""
Day 3 - 第二步：完整的Function Calling流程
从提问到得到答案的完整过程
"""

from openai import OpenAI
import json

client = OpenAI(
    api_key="你的DeepSeek-API-Key",
    base_url="https://api.deepseek.com"
)

print("=" * 60)
print("完整的Function Calling流程")
print("=" * 60)

# 1. 定义工具
tools = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "执行数学计算",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {"type": "string"}
            },
            "required": ["expression"]
        }
    }
}]

# 2. 真实的计算函数
def calculator(expression):
    try:
        result = eval(expression)
        return f"{expression} = {result}"
    except:
        return f"计算错误：{expression}"

# 3. 完整流程
def ask_with_calculator(question):
    print(f"\n用户：{question}")
    
    messages = [{"role": "user", "content": question}]
    
    # 第一次调用
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools
    )
    
    ai_msg = response.choices[0].message
    
    if ai_msg.tool_calls:
        print("→ AI决定调用计算器")
        
        # 获取参数
        tool_call = ai_msg.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        expression = args["expression"]
        
        # 执行真实函数
        result = calculator(expression)
        print(f"→ 计算结果：{result}")
        
        # 第二次调用
        messages.append(ai_msg)
        messages.append({"role": "tool", "content": result})
        
        final = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )
        
        print(f"→ 最终回答：{final.choices[0].message.content}")
    else:
        print(f"→ AI直接回答：{ai_msg.content}")

# 测试
ask_with_calculator("123 + 456 等于多少？")
ask_with_calculator("25 * 4 的结果是多少？")

print("\n" + "=" * 60)
print("关键理解：")
print("1. AI决定调用哪个工具")
print("2. 你的代码执行真实函数")
print("3. 需要两次API调用")
print("=" * 60)