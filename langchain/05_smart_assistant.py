"""
智能客服助手 - 整合所有功能
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

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
# 2. 知识库（RAG用）
# ============================================
knowledge_base = [
    {"title": "年假政策", "content": "入职满1年有5天年假，满3年有10天年假"},
    {"title": "加班政策", "content": "周末加班按2倍工资计算"},
    {"title": "请假政策", "content": "事假需提前1天申请，病假需提供医院证明"}
]

def search(question):
    """从知识库中检索相关文档"""
    question_lower = question.lower()
    for item in knowledge_base:
        if item["title"] in question_lower:
            return item["content"]
        for kw in ["年假", "加班", "请假", "病假", "事假"]:
            if kw in question_lower and kw in item["content"]:
                return item["content"]
    return None

# ============================================
# 3. 工具（Function Calling用）
# ============================================
orders_db = {
    "ORD001": "已发货，预计明天到达",
    "ORD002": "处理中，请稍候",
    "ORD003": "已送达"
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "查询订单状态",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "订单号，如ORD001"
                    }
                },
                "required": ["order_id"]
            }
        }
    }
]

def get_order_status(order_id: str) -> str:
    """真正执行订单查询的函数"""
    return orders_db.get(order_id, f"未找到订单{order_id}")

llm_with_tools = llm.bind_tools(tools)

# ============================================
# 4. 主程序
# ============================================
# 对话历史（Memory）
chat_history = []

print("=" * 50)
print("🤖 智能客服助手已启动")
print("命令：输入 'quit' 退出")
print("=" * 50)

while True:
    user_input = input("\n👤 你：")
    if user_input.lower() == "quit":
        print("👋 再见！")
        break
    
    # --- 先检查RAG ---
    rag_result = search(user_input)
    
    # --- 构建发送给AI的消息 ---
    if rag_result:
        enhanced_input = f"【参考信息】{rag_result}\n【用户问题】{user_input}\n请基于参考信息回答。"
    else:
        enhanced_input = user_input
    
    # 把用户消息加入历史
    chat_history.append(HumanMessage(content=enhanced_input))
    
    # --- 调用模型（含工具） ---
    response = llm_with_tools.invoke(chat_history)
    
    # --- 检查是否要调用工具 ---
    if response.tool_calls:
        tool_call = response.tool_calls[0]
        
        if tool_call["name"] == "get_order_status":
            order_id = tool_call["args"]["order_id"]
            status = get_order_status(order_id)
            
            # 把工具结果加入对话历史
            chat_history.append(AIMessage(content=f"订单状态：{status}"))
            print(f"🤖 AI：{status}")
        else:
            # 其他工具（目前只有一个，这里作为备用）
            print(f"🤖 AI：{response.content}")
    else:
        # 不需要调用工具，直接输出
        print(f"🤖 AI：{response.content}")
        # 把AI的回答加入历史（以便多轮对话）
        chat_history.append(AIMessage(content=response.content))