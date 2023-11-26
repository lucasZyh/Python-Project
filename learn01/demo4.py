# 查询余额
def query(show_flag):
    if show_flag:
        print("------------------查询余额------------------")
    print(f"{name}，您好，您的余额是{money}元")


# 存款
def save():
    global money
    num = int(input(f"{name}你好，请输入存款金额："))
    money += num
    query(False)


# 取款
def withdraw():
    global money
    num = int(input(f"{name}请输入取款金额："))
    if num > money:
        print("余额不足")
    else:
        money -= num
    query(False)


def main():
    print(f"---------{name}你好，欢迎来到郑州轻工业大学ATM取款机---------")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    print("请输入你的选择：")


money = 5000000
name = input("请输入用户名：")

while True:
    main()
    num = int(input())
    if num == 1:
        query(True)
    elif num == 2:
        save()
    elif num == 3:
        withdraw()
    elif num == 4:
        print("欢迎下次光临")
        break
    else:
        print("输入有误，请重新输入")
