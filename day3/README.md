# Day 3: Function Calling 学习笔记

## 📚 学习内容

- [x] 理解Function Calling的概念
- [x] 掌握工具定义方法
- [x] 完成完整调用流程
- [x] 实现天气助手

## 🔑 核心理解

### Function Calling是什么？
让AI能够"调用"外部工具/函数，获取实时数据。

### 为什么需要？
AI训练数据不是实时的，无法获取天气、新闻等动态信息。

### 工作流程
1. 用户提问 → 2. AI决定调用哪个工具 → 3. 你的代码执行函数 → 4. AI基于结果回答

### 关键点
- AI只负责"决定"，不负责"执行"
- 需要两次API调用
- 通过description匹配工具

## 📁 代码文件

| 文件 | 说明 |
|-----|------|
| step1_basic.py | 最简单的例子 |
| step2_complete_flow.py | 完整流程演示 |
| weather_assistant.py | 天气助手实战 |

## 🚀 运行方式

```bash
python day3/step1_basic.py
python day3/step2_complete_flow.py
python day3/weather_assistant.py