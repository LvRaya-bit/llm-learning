# 7天学习总结

## 📚 学习历程

### Day 1: API基础
- 学会了调用大模型API
- 理解了 messages 结构：system/user/assistant
- 完成第一次API调用

### Day 2: 参数调优 + 多轮对话
- temperature：控制创意度（低=稳定，高=创意）
- max_tokens：限制回复长度
- 实现多轮对话：维护 conversation 历史

### Day 3: Function Calling
- AI自动决定调用哪个工具
- 需要2次API调用
- 实现天气查询助手

### Day 4: RAG入门
- RAG = 检索 + 生成
- 让AI读取文档回答问题
- 实现公司政策问答

### Day 5: 流式输出
- stream=True 开启流式输出
- 实现打字机效果
- 大幅提升用户体验

### Day 6: 实战项目
- 整合所有知识点
- 完成智能客服助手
- 具备：多轮对话 + RAG + Function Calling + 流式输出

### Day 7: 总结整理
- 复习核心概念
- 准备面试题
- 完善GitHub作品集

---

## 💡 核心知识点汇总

| 概念 | 一句话总结 |
|------|-----------|
| messages | system设角色，user提问题，assistant记历史 |
| temperature | 低=准确稳定，高=创意多样 |
| Function Calling | AI决定，你的代码执行 |
| RAG | 先检索，再生成 |
| stream=True | 逐字输出，打字机效果 |

---

## 🎯 项目成果

**智能客服助手（Day 6）** 整合了全部知识点：

- 📚 RAG：查询公司政策
- 📦 Function Calling：查询订单状态
- 💬 多轮对话：记住上下文
- 💨 流式输出：打字机效果

---

## 🚀 下一步方向

- 学习 LangChain 框架
- 接入真实数据库
- 添加 Web 界面
- 支持语音对话