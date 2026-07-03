import streamlit as st

st.title("🤖 我的第一个 Streamlit 应用")
st.write("欢迎来到智能客服助手！")

user_input = st.text_input("请输入你的问题：")
if user_input:
    st.write(f"你输入了：{user_input}")