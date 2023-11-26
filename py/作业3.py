'''def number_sum(n):  # 定义一个求和函数
    sum = 0  # 赋初值
    for i in range(1, n + 1, 2):  # 循环求奇数和
        sum = sum + i
    return sum  # 返回sum的值


if __name__ == "__main__":  # 判断运行时是否作为主函数运行
    a = int(input("请输入数字："))  # 输入值
    num = number_sum(a)  # 调用求和函数
    print("结果为：", num)  # 打印结果'''

'''import ren_wu1  # 调用一个模块

a = int(input("数字："))  # 输入数值
sum = ren_wu1.number_sum(a)  # 调用模块里面的求和函数
print("结果为：", sum)  # 打印结果'''

wen_jian = open('E:\SEA\Python培训\引用.txt', 'a')  # 以存入的方式打开文档
flag = []  # 定义一个列表
wen_jian.write("url: https://www.google.com/,e-mail:maker@163.com,usernamfore:maker" + '\n')  # 向文档中添加内容
wen_jian.close()  # 关闭文档

wen_jian = open('E:\SEA\Python培训\引用.txt')  # 再次打开文档
for i in wen_jian.readlines():  # 遍历文档
    dic = {}  # 每次循环都定义一个新字典
    i = str(i).replace("\n", "")  # 把文档的每一行转换成字符串格式，并且将'\n'转换成无，即把'\n'扔掉
    i = i.split(",", 2)  # 把每一行先按','分成三部分
    for j in i:  # 遍历字符串
        dic[j.split(":", 1)[0]] = j.split(":", 1)[1]  # 把每一小部分再按':'分成两部分，前半部分为键，后半部分为值，存入字典
    flag.append(dic)  # 把这个字典放入列表中
wen_jian.close()  # 关闭文档
print(flag)  # 打印列表

'''import time#导入时间模块

Time = open(r'E:\SEA\Python培训\time.txt', 'a')  # 以追加的形式打开文档
a = time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime())  # 把格式话的时间日期赋给变量a
Time.write(a)  # 把a的内容打印进文档里面
Time.close()  # 关闭文档'''
'''import json  # 导入json模块

dic = {}  # 创建一个字典
char = input("请输入一串字符：")  # 输入字符串
f = open(r'E:\SEA\Python培训\char.txt', 'a')  # 打开文档

a = len(char)  # 求字符串长度
dic[char] = a  # 把字符串为建，长度为值存入字典中
print(dic)  # 打印字典
f.write(json.dumps(dic) + '\n')  # 把字典写入文档，然后在文档中换行
f.close()  # 关闭文档'''
