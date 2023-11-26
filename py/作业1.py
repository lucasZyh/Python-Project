'''sum = 0  # 赋初值，变量sum为累加的和
for i in range(1, 98, 2):  # 循环从1加到97
    sum = sum + i
print(f"sum = {sum}")  # 输出sum的值'''

'''sum = 0  # 赋初值，变量sum为奇数阶乘的和
a = 1  # 赋初值，变量a计算阶乘
for i in range(1, 16):
    a = a * i  # 求阶乘
    if i % 2 != 0:  # 判断是否为奇数的阶乘
        sum = sum + a  # 奇数的阶乘相加
print(f"sum = {sum}")  # 输出sum的值'''

'''for i in range(9, 0, -1):  # 循环i从9到1
    for j in range(1, i + 1, 1):  # 循环j从1到i
        sum = i * j  # 计算 i*j 的值
        print(f"{i}x{j}={sum} ", end=' ')  # 输出，并且不换行
    print()  # 从新的一行开始'''

'''a = input("请输入比赛成绩 ").split()  # 输入成绩
max = int(a[0])  # 强制类型转换，把字符型转换成整型
min = int(a[0])  # 强制类型转换，把字符型转换成整型
sum = 0  # 赋初值，变量sum为总成绩

for i in range(1, 10, 1):  # 循环，比较大小，找出最大值
    if int(a[i]) > max:
        max = int(a[i])

for i in range(1, 10, 1):  # 循环，比较大小，找出最小值
    if int(a[i]) < min:
        min = int(a[i])

for i in range(0, 10, 1):  # 求总成绩
    sum = sum + int(a[i])

grade = sum - min - max#计算有效成绩
print(f"平均成绩为:{grade / 8}")  # 输出平均值'''

'''n = int(input("输入打印三角形的层数: "))  # 输入数值，并将其转换成整型
for i in range(n):  # 控制所在行
    for j in range(n - i - 1):  # 打印出每一行需要的空格
        print(" ", end="")
    for j in range(i + 1):  # 打印出每行的*
        print("*", end=" ")
    print()  # 进入下一行'''

num = int(input("输入打印菱形的层数: "))  # 输入数值，并将其转换成整型。
n = num // 2 + 1  # 打印菱形实际需要的行数
# 打印上半部分的三角形
for i in range(n):  # 控制所在行
    for j in range(n - i - 1):  # 打印出每一行需要的空格
        print(" ", end="")
    for j in range(i + 1):  # 打印出每行的*
        print("*", end=" ")
    print()  # 进入下一行'
# 打印下半部分的三角形
m = n - 1
for i in range(m):  # 控制所在行
    for j in range(i + 1):  # 打印出每一行需要的空格
        print(" ", end="")
    for j in range(m - i):  # 打印出每行的*
        print("*", end=" ")
    print()  # 进入下一行
