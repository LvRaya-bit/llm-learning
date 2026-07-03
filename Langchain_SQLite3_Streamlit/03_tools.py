# 内容：用 @tool 装饰器定义工具，bind_tools 绑定
# 目标：理解 LangChain 如何实现 Function Calling
"""
LangChain 1.0+ 完整 Function Calling
"""

from langchain_openai import ChatOpenAI

# ============================================
# 1. 创建模型
# ============================================
llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key="your_api_key",
    openai_api_base="https://api.deepseek.com",
    temperature=0.3
)

# ============================================
# 2. 定义真正的工具函数（AI 不会执行它）
# ============================================
def get_weather(city: str) -> str:
    """模拟查询天气"""
    weather_db = {
        "北京": "晴天，25°C",
        "上海": "多云，28°C",
        "深圳": "阵雨，30°C"
    }
    return weather_db.get(city, f"暂无{city}的天气数据")

# ============================================
# 3. 定义工具描述（给 AI 看的说明书）
# ============================================
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的天气",  
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {          
                        "type": "string",
                        "description": "城市名称，如：北京、上海"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# ============================================
# 4. 把工具绑定到模型
# ============================================
llm_with_tools = llm.bind_tools(tools)  
# ============================================
# 5. 用户提问
# ============================================
user_question = "北京天气怎么样？"

# 6. AI 返回调用意向
response = llm_with_tools.invoke(user_question)

# 7. 检测 AI 是否想调用工具
if response.tool_calls:
    # 获取第一个工具调用信息
    tool_call = response.tool_calls[0]
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    
    print(f"🔧 AI 想调用工具：{tool_name}")
    print(f"📝 参数：{tool_args}")

    # 8. 根据工具名执行对应的函数
    if tool_name == "get_weather":
        city = tool_args["city"]
        result = get_weather(city)  
        print(f"✅ 执行结果：{result}")
    
    # 9. 把执行结果发回给 AI，让它组织最终回复
    final_response = llm.invoke(
        f"用户问：{user_question}\n工具返回结果：{result}\n请用自然语言回答。"
    )
    print(f"\n🤖 AI 最终回答：{final_response.content}")
else:
    # AI 直接回答，没有调用工具
    print(f"🤖 AI 直接回答：{response.content}")
