"""
LangChain Memory - 官方推荐方式（LangChain 1.0+）
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 1. 创建模型
llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key="your-api-key",  # 替换成你自己的Key
    openai_api_base="https://api.deepseek.com",
    temperature=0.7
)

# 2. 用列表管理对话历史（最简单、最稳定）
chat_history = []

# 3. 对话函数
def chat_with_memory(user_input):
    # 把用户消息加入历史
    chat_history.append(HumanMessage(content=user_input))
    
    # 调用模型
    response = llm.invoke(chat_history)
    
    # 把AI回答加入历史
    chat_history.append(AIMessage(content=response.content))
    
    return response.content

# 4. 测试
print("第1轮对话：")
print(chat_with_memory("我叫小明，我喜欢学习Python"))

print("\n第2轮对话（测试记忆）：")
print(chat_with_memory("我叫什么名字？"))

print("\n第3轮对话（继续测试）：")
print(chat_with_memory("我喜欢什么？"))
