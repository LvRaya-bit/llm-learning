from openai import OpenAI

class SmartBot:
    """智能对话机器人"""
    
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key="your_api_key",
            base_url="https://api.deepseek.com"
        )
        self.conversation = []
    
    def set_role(self, role_description):
        """设置AI的角色"""
        self.conversation.append({
            "role": "system",
            "content": role_description
        })
        print(f"✅ 角色已设置: {role_description}")
    
    def ask(self, question, temperature=0.7):
        """提问并获取回答"""
        # 添加用户问题
        self.conversation.append({"role": "user", "content": question})
        
        # 调用API
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=self.conversation,
            temperature=temperature
        )
        
        # 获取回答
        answer = response.choices[0].message.content
        
        # 保存回答到历史
        self.conversation.append({"role": "assistant", "content": answer})
        
        # 打印token使用情况
        print(f"📊 Token使用 - 输入:{response.usage.prompt_tokens} 输出:{response.usage.completion_tokens}")
        
        return answer
    
    def clear_history(self):
        """清空对话历史（保留system prompt）"""
        system_prompts = [msg for msg in self.conversation if msg["role"] == "system"]
        self.conversation = system_prompts
        print("🗑️ 对话历史已清空")
    
    def show_history(self):
        """显示对话历史"""
        print("\n📜 对话历史：")
        print("-" * 40)
        for msg in self.conversation:
            role = msg["role"]
            content = msg["content"][:50] + "..." if len(msg["content"]) > 50 else msg["content"]
            print(f"{role}: {content}")
        print("-" * 40)


# 使用示例
if __name__ == "__main__":
    print("=" * 60)
    print("🤖 智能对话机器人")
    print("=" * 60)
    
    # 创建机器人（记得替换API Key）
    bot = SmartBot("你的DeepSeek-API-Key")
    
    # 设置角色
    bot.set_role("你是一个友好的Python编程导师，用简单的语言解释复杂概念")
    
    print("\n命令说明：")
    print("- 直接输入问题开始对话")
    print("- 输入 'clear' 清空对话历史")
    print("- 输入 'history' 查看对话历史")
    print("- 输入 'quit' 退出程序")
    print("\n" + "=" * 60)
    
    while True:
        user_input = input("\n👤 你: ")
        
        if user_input.lower() == 'quit':
            print("👋 再见！")
            break
        elif user_input.lower() == 'clear':
            bot.clear_history()
            continue
        elif user_input.lower() == 'history':
            bot.show_history()
            continue
        
        # 正常对话
        response = bot.ask(user_input)
        print(f"🤖 AI: {response}")