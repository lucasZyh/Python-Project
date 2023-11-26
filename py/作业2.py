'''list = [101, 95, 33, 24, 70, 65, 23, 84, 121, 90]  # 列表
a = []  # 存放大于50的数的列表
b = []  # 存放小于50的数的列表
for i in list:  # 遍历列表list
    if i > 50:
        a.append(i)  # 大于50的数添加至列表a
    else:
        b.append(i)  # 小于50的数添加至列表b
dic = {'key1': a, 'key2': b}  # 创建字典
print(dic)  # 打印字典'''

'''a = [9, 6, 5, 4, 1]  # 列表a
a.reverse()  # 反向列表中元素
a.append('hi')  # 列表后添加新元素
print(a)  # 打印列表'''

'''a = [7, 5, 3, 1, 2, 0, 9, 4, 6, 15]  # 列表a
b = []  # 创建新列表，存放符合题意的元素
for i in a:  # 遍历列表
    for j in a:  # 遍历列表
        if i + j == 9:  # 判断
            b.append((i, j))  # 按要求格式存储元素
print(b)  # 打印列表'''

'''str = input("输入一串字符")  # 输入字符串
dic = {}  # 创建字典
for i in str:  # 遍历字符串
    num = str.count(i)  # 计算相同字母出现次数
    dic[i] = num  # 以字母为键，出现次数为值存入字典
print(dic)  # 打印字典'''
tes = []  # 创建列表
dev = []  # 创建列表
a = b = 0  # 赋初值
dep = {'kitch': [{"aki": "tester", "ennis": "tester", "nancy": "tester", "c": "tester", "kevin": "develop",
                  "tavis": "develop"}]}  # 一个字典
for dic in dep['kitch']:  # 遍历字典值里面的列表
    for i in dic:  # 遍历列表里面的字典
        if dic[i] == 'tester':  # 判断字典里面的值是否为tester，
            tes.append(i)  # 把值对应的键添加至列表
            a = a + 1  # 统计出现次数
        if dic[i] == 'develop':  # 判断字典里面的值是否为develop
            dev.append(i)  # 把值对应的键添加至列表
            b = b + 1  # 统计出现次数
print("tester:", a, tes)  # 打印次数和列表
print("develop:", b, dev)  # 打印次数和列表
