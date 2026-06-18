# 面试题整理

## 基础题

### 1. messages 中 system/user/assistant 各是什么作用？

| Role | 作用 | 示例 |
|------|------|------|
| system | 设置AI角色和行为准则 | "你是专业的客服助手" |
| user | 用户输入的问题 | "年假有多少天？" |
| assistant | AI的回复，用于保存对话历史 | "入职满1年有5天年假" |

---

### 2. temperature 参数的作用是什么？

- **低温度（0.1-0.3）**：回答稳定、准确，适合事实性问题、代码生成
- **高温度（1.0-1.5）**：回答有创意、多样，适合头脑风暴、创意写作

---

### 3. 如何实现多轮对话？

维护一个 `conversation` 列表，每次调用API时把完整历史传过去。

```python
conversation = []
conversation.append({"role": "user", "content": "我叫小明"})
# AI回复后
conversation.append({"role": "assistant", "content": "你好小明"})
# 下次调用时传入完整 conversation