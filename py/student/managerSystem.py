from student import *  # 导⼊入student模块


class StudentManager(object):
    def __init__(self):
        self.student_list = []  # 建立一个存储数据用的列表

    def run(self):  # 程序入口函数
        self.load_student()  # 加载学员信息

        while True:
            self.show_menu()  # 显示功能菜单
            menun_num = int(input("请输入您需要的功能序号："))  # 用户输入功能序号

            # 根据输入的序号，执行不同的功能
            if menun_num == 1:  # 添加学员
                self.add_student()
            elif menun_num == 2:  # 删除学员
                self.del_student()
            elif menun_num == 3:  # 修改学员信息
                self.modify_student()
            elif menun_num == 4:  # 查询学员信息
                self.search_student()
            elif menun_num == 5:  # 显示所有学员信息
                self.show_student()
            elif menun_num == 6:  # 保存学员信息
                self.save_student()
            elif menun_num == 7:  # 退出系统
                break
            elif menun_num == 8:  # 显示所有学员的姓名信息
                self.show_student_name()
            elif menun_num == 9:  # 显示所有男学员的全部信息
                self.show_male_studente()
            elif menun_num == 10:  # 删去年龄大于20的全部学员信息
                self.del_student_in_age()

    # 定义功能函数
    def show_menu(self):  # 显示功能菜单
        print("请选择如下功能------------")
        print("1:添加学员")
        print("2:删除学员")
        print("3:修改学员信息")
        print("4:查询学员信息")
        print("5:显示所有学员信息")
        print("6:保存学员信息")
        print("7:退出系统")
        print("8:显示所有学员的姓名信息")
        print("9:显示所有男学员的全部信息")
        print("10:删去年龄大于20的全部学员信息")

    def add_student(self):  # 添加学员

        # 用户输⼊姓名、性别、手机号、年龄
        name = input("请输入您的姓名")
        gender = input("请输入您的性别")
        tel = input("请输入您的手机号")
        age = input("请输入您的年龄")

        student = Student(name, gender, tel, age)  # 创建学员对象
        self.student_list.append(student)  # 将该学员对象添加到列表

        print(self.student_list)  # 打印信息
        print(student)  # 打印信息

    def del_student(self):  # 删除学员
        del_name = input('请输⼊要删除的学员姓名：')  # 用户输入目标学员姓名

        # 如果用户输入的目标学员存在则删除，否则提示学员不不存在
        for i in self.student_list:  # 遍历学生信息列表
            if i.name == del_name:  # 查找学生是否存在
                self.student_list.remove(i)  # 删除学生信息
                break
        else:
            print("查无此人！")

        print(self.student_list)  # 打印学生列表，验证删除功能

    def modify_student(self):  # 修改学员信息
        modify_name = input('请输⼊要修改的学员的姓名：')  # 用户输入目标学员姓名

        # 如果用户输入的目标学员存在，则修改信息，否则提示学员不存在
        for i in self.student_list:  # 遍历学生信息列表
            if i.name == modify_name:  # 查找学生是否存在
                # 更改学员信息
                i.name = input('请输⼊学员姓名：')
                i.gender = input('请输⼊学员性别：')
                i.tel = input('请输⼊学员手机号：')
                i.age = input('请输入学员年龄：')
                print(f'修改该学员信息成功，姓名{i.name},性别{i.gender}, 手机号{i.tel}, 年龄{i.age}')  # 打印学生信息，验证是否更改成功
                break
        else:
            print('查无此人！')

    def search_student(self):  # 查询学员信息
        search_name = input('请输⼊要查询的学员的姓名：')  # 用户输入目标学员姓名
        # 如果用户输入的目标学员存在，则打印学员信息，否则提示学员不存在
        for i in self.student_list:  # 遍历学生信息列表
            if i.name == search_name:  # 查找学生是否存在
                print(f'姓名{i.name},性别{i.gender}, 手机号{i.tel}, 年龄{i.age}')  # 打印学员信息
                break
        else:
            print('查无此⼈！')

    def show_student(self):  # 显示所有学员信息
        print('姓名\t性别\t手机号\t年龄')  # 打印信息名称
        for i in self.student_list:  # 遍历学生信息列表
            print(f'{i.name}\t{i.gender}\t\t{i.tel}\t{i.age}')  # 打印学员信息

    def save_student(self):  # 保存学员信息
        f = open('student.data', 'w', encoding='utf-8')  # 打开文件
        new_list = [i.__dict__ for i in self.student_list]  # 将学员数据转换成列表字典数据
        print(new_list)  # 打印信息
        f.write(str(new_list))  # 转换成字符串，存入文档
        f.close()  # 关闭文件

    def load_student(self):  # 加载学员信息
        # 尝试以"r"模式打开数据文件，文件不存在则提示用户；文件存在（没有异常）则读取数据
        try:
            f = open('student.data', 'r', encoding='utf-8')
        except:
            f = open('student.data', 'w', encoding='utf-8')
        else:
            data = f.read()  # 读取数据
            # 转换数据类型，再转换为字典为对象后存储到学员列表
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel'], i['age']) for i in new_list]
        finally:
            f.close()  # 关闭文件

    def show_student_name(self):  # 打印所有学员的姓名信息
        print('姓名')  # 打印信息名称
        for i in self.student_list:  # 遍历学生信息列表
            print(f'{i.name}')  # 打印学员姓名

    def show_male_studente(self):  # 显示所有男学员的全部信息
        print('姓名\t性别\t手机号\t年龄')  # 打印信息名称
        for i in self.student_list:  # 遍历学生信息列表
            if i.gender == '男':  # 判断性别
                print(f'{i.name}\t{i.gender}\t\t{i.tel}\t{i.age}')  # 打印学员信息

    def del_student_in_age(self):  # 删去年龄大于20的全部学员信息
        a = len(self.student_list)  # 计算列表长度
        for i in range(a - 1, -1, -1):  # 遍历学生信息列表
            if self.student_list[i].age > '20':  # 判断年龄
                self.student_list.remove(self.student_list[i])  # 删除学生信息

        print(self.student_list)  # 打印学生列表，验证删除功能
