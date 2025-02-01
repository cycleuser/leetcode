import os
import glob
from pathlib import Path
import requests
import time

def process_code_with_ollama(code: str) -> str:
    """
    使用Ollama处理代码
    Using Ollama to process code
    """
    prompt = """请对以下Python代码进行优化和双语注释改进:
    1. 添加清晰的中英文注释，一定要中英文双语注释
    2. 适度优化代码结构和性能
    3. 保持代码简洁易读
    4. 不要改变主要逻辑
    5. 要求只保留生成的代码部分，其他内容都作为文档注释保留
    6. 也就是代码开头和结尾的三个之间的内容不要删除，其他的都不要保留    
    请输出代码和注释，不要输出其他内容！不要评价，不要总结，什么多余的都不要放。
    
    代码如下:
    {}""".format(code)
    
    try:
        response = requests.post('http://localhost:11434/api/generate', 
                               json={
                                   "model": "qwen2.5:7b",
                                   "prompt": prompt,
                                   "stream": False
                               })
        return response.json()['response']
    except Exception as e:
        print(f"处理出错 Error occurred: {e}")
        return code



def process_python_files():
    """
    处理当前目录下所有Python文件
    Process all Python files in current directory
    """
    python_files = glob.glob("*.py")
    
    for file_path in python_files:
        if file_path == os.path.basename(__file__):
            continue
            
        # 检查是否存在备份文件
        # Check if backup file exists
        backup_path = f"{file_path}.bak"
        if os.path.exists(backup_path):
            print(f"跳过已处理文件 Skipping already processed file: {file_path}")
            continue
            
        print(f"处理文件 Processing: {file_path}")
        
        try:
            # 读取原始代码
            # Read original code
            with open(file_path, 'r', encoding='utf-8') as f:
                original_code = f.read()
            
            # 处理代码
            # Process code
            improved_code = process_code_with_ollama(original_code)
            
            # 备份原文件
            # Backup original file
            Path(file_path).rename(backup_path)
            
            # 写入优化后的代码
            # Write improved code
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(improved_code)
                
            print(f"完成处理 Completed: {file_path}")
            
            # 添加短暂延迟避免请求过快
            # Add short delay to avoid too frequent requests
            time.sleep(1)
            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错 Error while processing: {e}")

# ...existing code for if __name__ == "__main__"...
if __name__ == "__main__":
    process_python_files()