def number_sum(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum = sum + i
    return sum


if __name__ == "__main__":
    a = int(input("请输入数字："))
    num = number_sum(a)
    print("结果为：",num)
