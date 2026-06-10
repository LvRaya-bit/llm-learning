"""
Day 4: RAG（检索增强生成）入门
功能：让AI基于文档内容回答问题
"""

from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="你的DeepSeek-API-Key",  # 请替换成你自己的Key
    base_url="https://api.deepseek.com"
)

# ============================================
# 知识库文档
# ============================================
documents = [
    {"id": 1, "title": "年假政策", "content": "入职满1年有5天年假，满3年有10天年假"},
    {"id": 2, "title": "加班政策", "content": "周末加班按2倍工资计算"},
    {"id": 3, "title": "请假政策", "content": "事假需提前1天申请，病假需提供医院证明"}
]

print("=" * 60)
print("📚 知识库已加载")
print("=" * 60)
for doc in documents:
    print(f"  - {doc['title']}: {doc['content']}")

# ============================================
# 检索函数：找到和问题最相关的文档
# ============================================
def search_documents(question, documents):
    """关键词检索，返回最相关的文档"""
    
    scored_docs = []
    question_lower = question.lower()
    
    for doc in documents:
        content = doc["content"].lower()
        score = 0
        
        # 关键词匹配
        keywords = ["年假", "加班", "事假", "病假", "周末", "工资", "申请", "证明"]
        for kw in keywords:
            if kw in question_lower and kw in content:
                score += 10
        
        # 标题匹配
        if doc["title"] in question_lower:
            score += 5
        
        if score > 0:
            scored_docs.append((score, doc))
    
    scored_docs.sort(reverse=True, key=lambda x: x[0])
    return [doc for score, doc in scored_docs[:1]] if scored_docs else []

# ============================================
# RAG问答函数：检索 + AI生成
# ============================================
def rag_answer(question):
    print(f"\n{'='*40}")
    print(f"👤 用户问：{question}")
    
    # 第1步：检索相关文档
    relevant_docs = search_documents(question, documents)
    
    if not relevant_docs:
        return "❌ 知识库中没有找到相关信息"
    
    # 第2步：获取检索到的内容
    doc = relevant_docs[0]
    context = f"【{doc['title']}】{doc['content']}"
    print(f"📚 检索到：{context}")
    
    # 第3步：构建给AI的消息
    user_prompt = f"""请基于下面的参考文档回答问题。

参考文档：
{context}

问题：{question}

请直接回答："""
    
    # 第4步：调用AI
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是公司助手，必须严格基于参考文档回答。"},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )
    
    # 第5步：返回答案
    return response.choices[0].message.content

# ============================================
# 测试
# ============================================
print("\n" + "=" * 60)
print("🚀 开始RAG问答测试")
print("=" * 60)

questions = [
    "年假有多少天？",
    "周末加班怎么算？",
    "事假怎么请？",
    "病假需要什么？"
]

for q in questions:
    answer = rag_answer(q)
    print(f"🤖 AI答：{answer}")

print("\n" + "=" * 60)
print("✅ RAG 学习完成！")
print("=" * 60)