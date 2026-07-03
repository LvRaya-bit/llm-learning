import streamlit as st

st.set_page_config(page_title="智能客服", page_icon="🤖")
st.title("🤖 智能客服助手")

# 1️⃣ 初始化聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2️⃣ 显示历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 3️⃣ 输入框
user_input = st.chat_input("请输入你的问题...")
if user_input:
    # 显示用户消息
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # 模拟 AI 回复（后面再接入真实逻辑）
    with st.chat_message("assistant"):
        response = f"你说了：{user_input}"
        st.write(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})