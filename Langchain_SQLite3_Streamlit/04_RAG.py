"""
LangChain RAG - 检索增强生成
"""

from langchain_openai import ChatOpenAI

# ============================================
# 1. 创建模型
# ============================================
llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key="your-api-key",  # 替换成你自己的Key
    openai_api_base="https://api.deepseek.com",
    temperature=0.3
)

# ============================================
# 2. 知识库（模拟文档）
# ============================================
knowledge_base = [
    {"title": "年假政策", "content": "入职满1年有5天年假，满3年有10天年假"},
    {"title": "加班政策", "content": "周末加班按2倍工资计算"},
    {"title": "请假政策", "content": "事假需提前1天申请，病假需提供医院证明"}
]

# ============================================
# 3. 检索函数（从知识库中找相关内容）
# ============================================
def search(question):
    """根据问题关键词检索相关文档"""
    question_lower = question.lower()
    
    for item in knowledge_base:
        # 如果问题中包含标题关键词，返回该文档内容
        if item["title"] in question_lower:
            return item["content"]
        
        # 额外检查：常见关键词
        for kw in ["年假", "加班", "请假", "病假", "事假"]:
            if kw in question_lower and kw in item["content"]:
                return item["content"]
    
    return None  # 没找到返回 None

# ============================================
# 4. RAG 问答
# ============================================
def rag_ask(question):
    # 第1步：检索相关文档
    context = search(question)
    
    if context is None:
        return "知识库中没有找到相关信息"
    
    # 第2步：构建提示词，把检索到的内容作为上下文
    prompt = f"""
请基于以下文档内容回答问题。

文档内容：
{context}

问题：{question}

请直接回答："""
    
    # 第3步：调用 AI
    response = llm.invoke(prompt)
    
    # 第4步：返回回答
    return response.content

# ============================================
# 5. 测试
# ============================================
if __name__ == "__main__":
    questions = [
        "年假有多少天？",
        "周末加班怎么算？",
        "事假怎么请？"
    ]

    for q in questions:
        print(f"\n用户问：{q}")
        answer = rag_ask(q)
        print(f"AI答：{answer}")