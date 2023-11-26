def print_file_inof(file_name):
    """
    打印文件信息
    :param file_name: 文件名
    :return: None
    """
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        print(f.read())
    except Exception as e:
        print("程序出现异常，异常信息如下：")
        print(e)
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    追加数据到文件
    :param file_name: 文件名
    :param data: 数据
    :return: None
    """
    f = open(file_name, 'a', encoding='utf-8')
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    # print_file_inof('../iodic.txt')
    append_to_file('aaa.txt', 'hello')
