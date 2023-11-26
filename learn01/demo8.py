f = open("iodic.txt", "r", encoding="utf-8")

# 读取文件中的内容
# 1. read() 读取文件中的所有内容
# content = f.read(20)
# print(content)

# 2. readline() 读取文件中的一行内容
# content = f.readline()
# print(content)

# 3. readlines() 读取文件中的所有内容，返回一个列表，每一行是列表中的一个元素
# content = f.readlines()
# print(content)

# 4. for循环遍历文件对象
for line in f:
    print(line)

# 关闭文件
f.close()

# with open可以自动关闭文件

with open("itheima.txt", "r", encoding= "utf-8") as f:
    # 方法一：
    # count = 0
    # for line in f:
    #     lines = line.strip().split(" ")
    #     for word in lines:
    #         if word == "itheima":
    #             count += 1

    read = f.read()
    count = read.count("itheima")
    print(count)
