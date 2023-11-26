import random

count = 0
r = random.randint(1, 100)

while True:
    num = int(input("请输入一个数字："))
    count += 1
    if num == r:
        print(f"猜对了，这次的数字是{num}，你一共猜了{count}次")
        break
    elif num > r:
        print("猜大了，请重新输入")
    else:
        print("猜小了，请重新输入")
