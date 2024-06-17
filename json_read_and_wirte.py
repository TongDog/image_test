import json

# 假设您有一个名为'example.json'的文件
filename = 'annotations_1.json'

# 打开并读取JSON文件
with open(filename, 'r', encoding='utf-8') as file:
    # 解析文件中的JSON数据
    data = json.load(file)


new_filename = 'new.json'
with open('new.json', 'r', encoding='utf-8') as file2:

    data2 = json.load(file2)

keys = data.keys()

#print(keys)
#print(data2['categories'])
print(keys)

for key in keys:
    if key !='info':

        print(isinstance(data[key], list))
        data[key].extend(data2[key])
    # print(data2[key])
    #print(key)
merged_path = 'annotations.json'
with open(merged_path, 'w', encoding='utf-8') as file:
    json.dump(data, file)
