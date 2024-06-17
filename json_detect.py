import json

# 假设您有一个名为'annotations_1.json'的文件
filename = 'annotations_1.json'

# 打开并读取JSON文件
with open(filename, 'r', encoding='utf-8') as file:
    # 解析文件中的JSON数据
    data = json.load(file)

# 查询每个key下的元素个数
element_counts = {}
for key, value in data.items():
    if isinstance(value, list):
        element_counts[key] = len(value)
    elif isinstance(value, dict):
        element_counts[key] = sum(1 for item in value.values())
    else:
        element_counts[key] = 1

# 输出每个key下的元素个数
for key, count in element_counts.items():
    print(f"{key}: {count} elements")
