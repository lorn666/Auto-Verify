import json

def modify_jsonl(input_file, output_file):
    """
    读取 JSONL 文件，将 `problem` 字段名改为 `question`，并保存到新的文件中。

    :param input_file: 输入 JSONL 文件路径
    :param output_file: 输出 JSONL 文件路径
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                data = json.loads(line.strip())  # 解析每一行的 JSON 数据
                if 'problem' in data:
                    data['question'] = data.pop('problem')  # 修改字段名
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')  # 写入修改后的数据
        print(f"成功将 `problem` 字段名修改为 `question`，结果已保存到 {output_file}")
    except FileNotFoundError:
        print(f"错误：文件 {input_file} 未找到！")
    except json.JSONDecodeError:
        print("错误：文件内容不是有效的 JSON 格式！")
    except Exception as e:
        print(f"发生错误：{e}")

# 示例用法
if __name__ == "__main__":
    input_file = "MATH_500.jsonl"  # 输入文件路径
    output_file = "MATH_500_2.jsonl"  # 输出文件路径
    modify_jsonl(input_file, output_file)
