import json

data = [{"name": "张三", "age": 13}, {"name": "李四", "age": 18}, {"name": "王五", "age": 19}]

# 将列表转换为json字符串
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

# 将json字符串转换为列表
data2 = json.loads(json_str)
print(data2)
