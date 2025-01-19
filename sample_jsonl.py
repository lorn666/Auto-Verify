import json
import random
from typing import List

def sample_jsonl(input_file: str, output_file: str, n: int) -> None:
    """
    从JSONL文件中随机采样n条记录并保存到新文件
    
    参数:
    input_file (str): 输入JSONL文件路径
    output_file (str): 输出JSONL文件路径
    n (int): 需要采样的记录数量
    """
    # 读取所有行
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 确保采样数量不超过总行数
    n = min(n, len(lines))
    
    # 随机采样
    sampled_lines = random.sample(lines, n)
    
    # 写入新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(sampled_lines)

if __name__ == "__main__":
    # 示例使用
    input_file = "math_testset_annotation.jsonl"    # 输入文件路径
    output_file = "math_500_sample.jsonl"  # 输出文件路径
    n = 500                       # 需要采样的记录数量
    
    sample_jsonl(input_file, output_file, n)
    print(f"已从{input_file}中随机采样{n}条记录并保存到{output_file}")
