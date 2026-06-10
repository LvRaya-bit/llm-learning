"""
Day 3 - 实战：智能天气助手
"""

from openai import OpenAI
import json

client = OpenAI(
    api_key="你的DeepSeek-API-Key",
    base_url="https://api.deepseek.com"
)

print("=" * 60)
print("🌤️ 智能天气助手")
print("=" * 60)

# 模拟天气数据
weather_db = {
    "北京": "晴天，25°C，湿度45%",
    "上海": "多云，28°C，湿度65%",
    "深圳": "阵雨，30°C，湿度80%",
}

# 定义工具
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "获取城市天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]

def get_weather(city):
    return weather_db.get(city, f"暂无{city}天气数据")

def ask_weather(question):
    print(f"\n用户：{question}")
    
    messages = [{"role": "user", "content": question}]
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools
    )
    
    ai_msg = response.choices[0].message
    
    if ai_msg.tool_calls:
        tool_call = ai_msg.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        city = args["city"]
        
        weather = get_weather(city)
        
        messages.append(ai_msg)
        messages.append({"role": "tool", "content": weather})
        
        final = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )
        
        print(f"助手：{final.choices[0].message.content}")
    else:
        print(f"助手：{ai_msg.content}")

# 测试
ask_weather("北京天气怎么样？")
ask_weather("上海今天热吗？")
ask_weather("深圳会下雨吗？")