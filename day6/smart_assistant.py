"""
Day 6 - 智能客服助手
整合：多轮对话 + RAG + Function Calling + 流式输出
"""

from openai import OpenAI
import json

# 初始化
client = OpenAI(
    api_key="你的API-Key",
    base_url="https://api.deepseek.com"
)

print("=" * 60)
print("🤖 智能客服助手")
print("=" * 60)
print("功能：")
print("  - 📚 查询公司政策（年假、加班等）")
print("  - 📦 查询订单状态（ORD001/ORD002/ORD003）")
print("  - 💬 多轮对话记忆")
print("  - 💨 流式输出")
print("=" * 60)

# 知识库（RAG用）
knowledge_base = [
    {"title": "年假政策", "content": "入职满1年有5天年假，满3年有10天年假"},
    {"title": "加班政策", "content": "周末加班按2倍工资计算"},
    {"title": "请假政策", "content": "事假需提前1天申请，病假需提供医院证明"}
]

# 订单数据库
orders_db = {
    "ORD001": {"status": "已发货", "tracking": "SF1234567890", "date": "2026-06-10"},
    "ORD002": {"status": "处理中", "tracking": None, "date": "2026-06-12"},
    "ORD003": {"status": "已送达", "tracking": "YT9876543210", "date": "2026-06-05"}
}

# 对话历史
conversation = [
    {"role": "system", "content": "你是智能客服助手，友好、专业。"}
]

# ============================================
# RAG：检索知识库
# ============================================
def search_knowledge(question):
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
# Function Calling：查询订单
# ============================================
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
                        "description": "订单号，格式如ORD001"
                    }
                },
                "required": ["order_id"]
            }
        }
    }
]

def get_order_status(order_id):
    """查询订单状态"""
    if order_id in orders_db:
        order = orders_db[order_id]
        return f"订单{order_id}状态：{order['status']}，下单日期：{order['date']}"
    else:
        return f"未找到订单{order_id}，请确认订单号是否正确"

# ============================================
# 处理用户输入（流式版本）
# ============================================
def process_user_input(user_input):
    """处理用户输入 - 流式输出"""
    
    # 先检索知识库（可以用于增强prompt，这里先保留）
    knowledge = search_knowledge(user_input)
    
    # 构建消息
    messages = conversation.copy()
    messages.append({"role": "user", "content": user_input})
    
    # 第一次调用：让AI决定是否需要调用工具
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    
    ai_message = response.choices[0].message
    
    # 如果AI想调用工具
    if ai_message.tool_calls:
        tool_call = ai_message.tool_calls[0]
        tool_name = tool_call.function.name
        
        if tool_name == "get_order_status":
            args = json.loads(tool_call.function.arguments)
            order_id = args["order_id"]
            tool_result = get_order_status(order_id)
            
            # 第二次调用：基于工具结果回答
            messages.append(ai_message)
            messages.append({"role": "tool", "content": tool_result})
            
            final_response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages
            )
            
            answer = final_response.choices[0].message.content
            print(f"\n🤖 AI: {answer}")
    else:
        # 不需要调用工具，直接流式输出
        print("\n🤖 AI: ", end="", flush=True)
        
        stream_response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=True
        )
        
        answer = ""
        for chunk in stream_response:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                answer += content
        print()
    
    # 保存对话历史
    conversation.append({"role": "user", "content": user_input})
    conversation.append({"role": "assistant", "content": answer})
    
    return answer

# ============================================
# 主程序
# ============================================
if __name__ == "__main__":
    print("\n命令：输入 'quit' 退出，'clear' 清空历史\n")
    
    while True:
        user_input = input("👤 你: ")
        
        if user_input.lower() == 'quit':
            print("👋 再见！")
            break
        elif user_input.lower() == 'clear':
            conversation = [{"role": "system", "content": "你是智能客服助手，友好、专业。"}]
            print("✅ 对话历史已清空")
            continue
        
        process_user_input(user_input)