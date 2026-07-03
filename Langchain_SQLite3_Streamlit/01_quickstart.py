# 内容：用 LangChain 调用 DeepSeek，测试连通性
# 目标：确认环境正常
"""
LangChain 快速开始 - 第一次调用
"""

from langchain_openai import ChatOpenAI

# 初始化模型（使用 DeepSeek）
llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key="your_api_key",  # 替换成你自己的Key
    openai_api_base="https://api.deepseek.com",
    temperature=0.7
)

# 第一次调用
response = llm.invoke("用一句话介绍Python")
print(response.content)
