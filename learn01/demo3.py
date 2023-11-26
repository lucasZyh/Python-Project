import random

money = 10000

for x in range(1, 21):
    grade = random.randint(1, 10)
    if grade < 5:
        print(f"员工{x}，对不起，你的绩效为{grade}，不能发工资")
        continue
    else:
        print(f"员工{x}，恭喜你，你的绩效为{grade}，发工资1000元")
        money -= 1000
    print(f"剩余工资{money}")
    if money <= 0:
        print("钱不够了，发工资结束")
        break
