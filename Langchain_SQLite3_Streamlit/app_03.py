import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from get_order_status import get_order_status
import os  # 新增

# ============================================
# 1. 页面配置
# ============================================
st.set_page_config(page_title="智能客服助手", page_icon="🤖")
st.title("🤖 智能客服助手")

# ============================================
# 2. 加载知识库函数
# ============================================
def load_knowledge_from_file(file_path: str) -> list:
    knowledge = []
    # 使用脚本所在目录的绝对路径
    full_path = os.path.join(os.path.dirname(__file__), file_path)
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        st.warning(f"未找到 {full_path}，请确认文件存在")
        return []
    # ... 其余代码不变
    current_title = None
    current_content = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "政策" in line:
            if current_title and current_content:
                knowledge.append({
                    "title": current_title,
                    "content": "".join(current_content).strip()
                })
            current_title = line
            current_content = []
        else:
            current_content.append(line)
    if current_title and current_content:
        knowledge.append({
            "title": current_title,
            "content": "".join(current_content).strip()
        })
    return knowledge

# ============================================
# 3. 初始化（只在第一次运行时执行）
# ============================================
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.chat_history = []
    st.session_state.knowledge_base = load_knowledge_from_file("company_policies.txt")
    
    # 创建模型
    st.session_state.llm = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key=st.secrets["DEEPSEEK_API_KEY"],  # 替换成你自己的Key
        openai_api_base="https://api.deepseek.com",
        temperature=0.3
    )
    
    # 定义工具
    tools = [{
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
    }]
    st.session_state.llm_with_tools = st.session_state.llm.bind_tools(tools)

# ============================================
# 4. 检索函数
# ============================================
def search(question, knowledge_base):
    question_lower = question.lower()
    for item in knowledge_base:
        if item["title"] in question_lower:
            return item["content"]
        for kw in ["年假", "加班", "请假", "病假", "远程", "培训", "晋升", "福利", "团建"]:
            if kw in question_lower and kw in item["content"]:
                return item["content"]
    return None

# ============================================
# 5. 处理用户输入
# ============================================
def process_user_input(user_input: str) -> str:
    # 检索 RAG
    rag_result = search(user_input, st.session_state.knowledge_base)
    if rag_result:
        enhanced_input = f"【参考信息】{rag_result}\n【用户问题】{user_input}\n请基于参考信息回答。"
    else:
        enhanced_input = user_input
    
    # 更新历史
    st.session_state.chat_history.append(HumanMessage(content=enhanced_input))
    
    # 调用模型
    response = st.session_state.llm_with_tools.invoke(st.session_state.chat_history)
    
    # 处理工具调用
    if response.tool_calls:
        tool_call = response.tool_calls[0]
        if tool_call["name"] == "get_order_status":
            order_id = tool_call["args"]["order_id"]
            status = get_order_status(order_id)
            st.session_state.chat_history.append(AIMessage(content=f"订单状态：{status}"))
            return status
        return "抱歉，不支持该工具"  # 新增
    else:
        st.session_state.chat_history.append(AIMessage(content=response.content))
        return response.content
    
    # 删除这行：return "抱歉，处理出错了"

# ============================================
# 6. 显示对话历史
# ============================================
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ============================================
# 7. 输入框
# ============================================
user_input = st.chat_input("请输入你的问题...")
if user_input:
    # 显示用户消息
    with st.chat_message("user"):
        st.write(user_input)
    
    # 生成并显示AI回复
    with st.chat_message("assistant"):
        response = process_user_input(user_input)
        st.write(response)
