import json
import sys

def calculate_accuracy(standard_file, model_file):
    with open(standard_file, 'r', encoding='utf-8') as f:
        standard_data = {item["question"]: item["answer"] for item in json.load(f)}
    with open(model_file, 'r', encoding='utf-8') as f:
        model_data = {item["question"]: item["answer"] for item in json.load(f)}
    correct = sum(1 for q, ans in standard_data.items() if model_data.get(q) == ans)
    return correct / len(standard_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python eval_output_jsonl.py <standard_file> <model_file>")
        sys.exit(1)
    standard_file = sys.argv[1]
    model_file = sys.argv[2]
    accuracy = calculate_accuracy(standard_file, model_file)
    print("Accuracy:", accuracy)