# 学习笔记

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
