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
                self.save_student()
            elif menun_num == 2:  # 查询学员信息
                self.search_student()
            elif menun_num == 3:  # 显示所有学员信息
                self.show_student()
            elif menun_num == 4:  # 保存学员信息
                self.save_student()
            elif menun_num == 5:  # 删除学员
                self.del_student()
                self.save_student()
            elif menun_num == 6:  # 修改学员信息
                self.modify_student()
                self.save_student()
            elif menun_num == 7:  # 统计成绩
                self.data_statistic()
            elif menun_num == 8:  # 退出系统
                break

    # 定义功能函数

    def show_menu(self):  # 显示功能菜单
        print("请选择如下功能------------")
        print("1:添加学员")
        print("2:查询学员信息")
        print("3:显示所有学员")
        print("4:保存学员信息")
        print("5:信息删除学员")
        print("6:修改学员信息")
        print("7:统计成绩")
        print("8:退出系统")

    def add_student(self):  # 添加学员

        # 用户输⼊姓名、性别、手机号、年龄
        name = input("请输入您的姓名")
        gender = input("请输入您的性别")
        tel = input("请输入您的手机号")
        age = input("请输入您的年龄")

        scores = []
        score1 = input('请输入学科A成绩：')
        score2 = input('请输入学科B成绩：')
        scores.append(score1)
        scores.append(score2)

        student = Student(name, gender, tel, age, scores)  # 创建学员对象
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

                scores = []
                score1 = input('请输入学科A成绩：')
                score2 = input('请输入学科B成绩：')
                scores.append(score1)
                scores.append(score2)

                print(
                    f'姓名：{i.name}, 性别：{i.gender}, 手机号：{i.tel}, 年龄：{i.age}, 成绩A：{i.scores[0]}, 成绩B：{i.scores[0]}')  # 打印学生信息，验证是否更改成功
                break
        else:
            print('查无此人！')

    def search_student(self):  # 查询学员信息
        search_name = input('请输⼊要查询的学员的姓名：')  # 用户输入目标学员姓名
        # 如果用户输入的目标学员存在，则打印学员信息，否则提示学员不存在
        for i in self.student_list:  # 遍历学生信息列表
            if i.name == search_name:  # 查找学生是否存在
                print(
                    f'姓名：{i.name}, 性别：{i.gender}, 手机号：{i.tel}, 年龄：{i.age}, 成绩A：{i.scores[0]}, 成绩B：{i.scores[0]}')  # 打印学员信息
                break
        else:
            print('查无此⼈！')

    def show_student(self):  # 显示所有学员信息
        print('姓名\t性别\t\t手机号\t年龄\t\t学科A成绩\t\t学科B成绩')  # 打印信息名称
        for i in self.student_list:  # 遍历学生信息列表
            print(f'{i.name}\t{i.gender}\t\t{i.tel}\t\t{i.age}\t\t{i.scores[0]}\t\t\t{i.scores[0]}')  # 打印学员信息

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
            self.student_list = [Student(i['name'], i['gender'], i['tel'], i['age'], i['scores']) for i in new_list]
        finally:
            f.close()  # 关闭文件

    def data_statistic(self):
        scoresA = 0
        scoresB = 0
        sum = 0
        count = 0
        print('姓名\t\t学科A成绩\t\t学科B成绩\t\t总成绩')  # 打印信息名称
        for i in self.student_list:  # 遍历学生信息列表
            count = count + 1
            scoresA = scoresA + int(i.scores[0])
            scoresB = scoresB + int(i.scores[1])
            sum = int(i.scores[0]) + int(i.scores[1])
            print(f'{i.name}\t\t{i.scores[0]}\t\t{i.scores[1]}\t\t\t{sum}')
        print('学科A平均成绩\t\t学科B平均成绩')  # 打印信息名称
        print(f'{scoresA / count}\t\t\t{scoresB / count}')
