num = 136
num2 = 5

num3 = 135.6

name1 = "郑州轻工业大学位于科学大道%s号，东风路%s号" % (num, num2)

print(name1)
print("整数：%5d" % num2)
print("浮点数：%.2f" % num3)
print(f"浮点数：{num3},整数：{num2}")

user_name = input("请输入用户类型：")
user_type = input("请输入用户类型：")
print(f"你好，尊贵的{user_name}，你的身份是{user_type}")
