# 学习笔记

快速跳转：[Day 1](day1/) | [Day 2](day2/) | [Day 3](day3/) | [Day 4](day4/) | [Day 5](day5/) | [Day 6](day6/)| [Day 7](day7/)

## Day 1 - API基础

API调用本质：发送文本到远程服务器

messages三种role：
- system: 设置AI行为准则
- user: 用户输入
- assistant: AI回复

## Day 2 - 高级特性

temperature: 控制创造性（0.1稳定 - 1.5创意）
- max_tokens: 限制回复长度
- 多轮对话：维护完整历史实现上下文记忆
- 输出格式控制：用system prompt和低temperature保证格式

## Day 3 - Function Calling

- AI通过description匹配工具，自动决定调用哪个函数
- AI不执行函数，只负责"决定"，真正执行由你的代码完成
- 需要两次API调用：第一次决定调用什么，第二次基于结果回答
- 可实现多功能助手（天气查询、计算器等）

## Day 4 - RAG入门

- RAG = 检索（Retrieval）+ 生成（Generation）
- 先检索相关文档，再让AI基于文档内容回答
- 让AI能够读取私有知识库（公司政策、产品手册等）
- 核心流程：用户提问 → 关键词检索 → 构建上下文 → AI生成答案

## Day 5 - 流式输出

- `stream=True`：开启流式输出，实现打字机效果
- `delta`：流式模式中，每次返回的是新增的内容（增量）
- `flush=True`：强制立即输出，不等待缓冲区，保证实时性
- 核心价值：大幅降低用户感知的等待时间，提升体验

## Day 6 - 实战项目（智能客服助手）

- **项目整合**：将前5天所有知识（多轮对话、RAG、Function Calling、流式输出）整合到一个完整应用中。
- **核心功能**：
  - 📚 **RAG查询**：自动检索并回答公司政策（如年假、加班）。
  - 📦 **工具调用**：通过 Function Calling 查询订单状态。
  - 💬 **多轮记忆**：记住上下文，支持连续追问。
  - 💨 **流式体验**：回答逐字显示，接近真实对话。
- **架构设计**：一个 `process_user_input` 函数统一处理用户请求，根据意图智能选择是检索文档、调用工具还是直接对话。

## Day 7 - 总结整理

- **复习核心概念**：巩固 system/user/assistant、temperature、Function Calling、RAG、流式输出等知识点。
- **准备面试题**：整理了基础、进阶、实战三类常见问题及解答。
- **完善GitHub作品集**：7天学习全部完成，形成完整的学习记录和项目展示。
