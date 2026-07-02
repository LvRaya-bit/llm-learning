# 🤖 智能客服助手 (LangChain + Streamlit)

这是一个基于 LangChain 和 Streamlit 构建的智能客服助手 Web 应用。它集成了多种功能，能够回答关于公司政策、订单状态等问题。

## ✨ 主要功能

- 💬 **多轮对话**：能够记住对话上下文，进行连贯的交流。
- 📚 **RAG 检索**：从 `company_policies.txt` 文档中检索信息，回答关于年假、加班、培训等政策问题。
- 📦 **订单查询**：通过 Function Calling 调用工具，从 SQLite 数据库中查询真实的订单状态。
- 🖥️ **友好界面**：提供简洁的 Web 聊天界面，方便交互。

## 🚀 如何运行

1.  **克隆仓库** (或下载本项目)
    ```bash
    git clone <你的仓库地址>
    cd llm-learning/langchain-project

## 结构说明
langchain/
├── app_03.py                     # Web 应用主程序
├── 01_quickstart.py              # 第1步：基础调用
├── 02_memory.py                  # 第2步：多轮对话
├── 03_tools.py                   # 第3步：Function Calling
├── 04_rag.py                     # 第4步：RAG 检索
├── 05_smart_assistant.py         # 第5步：命令行客服助手
├── get_order_status.py           # SQLite 查询函数
├── load_knowledge_from_file.py   # 文档加载函数
├── company_policies.txt          # 知识库文档
└── company.db                    # 订单数据库（自动生成）

## 运行方式
```bash
python langchain/01_quickstart.py

#在项目目录下运行
streamlit run app_03.py
