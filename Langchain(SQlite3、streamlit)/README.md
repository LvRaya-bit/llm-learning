text
# 🤖 智能客服助手 (LangChain + Streamlit)

这是一个基于 LangChain 和 Streamlit 构建的智能客服助手 Web 应用。它集成了多种功能，能够回答关于公司政策、订单状态等问题。

- 💬 **多轮对话**：能够记住对话上下文，进行连贯的交流。
- 📚 **RAG 检索**：从 `company_policies.txt` 文档中检索信息，回答关于年假、加班、培训等政策问题。
- 📦 **订单查询**：通过 Function Calling 调用工具，从 SQLite 数据库中查询真实的订单状态。
- 🖥️ **友好界面**：提供简洁的 Web 聊天界面，方便交互。

---

## 📦 依赖包说明

| 包名 | 版本要求 | 用途 |
|------|----------|------|
| `streamlit` | >=1.28.0 | Web 界面框架，让客服助手变成网页应用 |
| `langchain` | >=0.2.0 | 核心框架，管理对话、RAG 检索等 |
| `langchain-openai` | >=0.1.0 | 让 LangChain 调用 DeepSeek 等兼容 OpenAI 格式的模型 |
| `langchain-core` | >=0.2.0 | LangChain 的基础组件（HumanMessage、AIMessage 等） |
| `openai` | >=1.0.0 | 底层 HTTP 客户端，被 langchain-openai 依赖 |

---

## 🚀 如何运行

### 1. 克隆仓库（或下载本项目）

```bash
git clone <你的仓库地址>
cd llm-learning/langchain-project
2. 安装依赖包
bash
pip install -r requirements.txt
3. 配置 API 密钥
在 app_03.py 文件中，找到 openai_api_key 参数，替换成你自己的 DeepSeek API Key。

4. 启动 Web 应用
bash
streamlit run app_03.py
浏览器会自动打开 http://localhost:8501。

📁 结构说明
text
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
🧪 运行其他示例
bash
# 测试基础调用
python 01_quickstart.py

# 测试多轮对话
python 02_memory.py

# 测试工具调用
python 03_tools.py

# 测试 RAG 检索
python 04_rag.py

# 启动命令行版客服助手
python 05_smart_assistant.py
🛠️ 技术栈
LangChain：LLM 应用开发框架

Streamlit：Web 界面框架

SQLite：轻量级数据库

DeepSeek API：大语言模型服务
