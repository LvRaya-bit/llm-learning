def load_knowledge_from_file(file_path: str) -> list:
    """
    从文本文件读取知识库
    文件格式：每段以标题行开头，后面跟着内容
    """
    knowledge = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    current_title = None
    current_content = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 如果这行包含"政策"两个字，把它当作标题
        if "政策" in line:
            # 保存之前的内容
            if current_title and current_content:
                knowledge.append({
                    "title": current_title,
                    "content": "".join(current_content).strip()
                })
            # 开始新的段落
            current_title = line
            current_content = []
        else:
            current_content.append(line)
    
    # 保存最后一段
    if current_title and current_content:
        knowledge.append({
            "title": current_title,
            "content": "".join(current_content).strip()
        })
    
    return knowledge