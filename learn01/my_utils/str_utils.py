def str_revers(s):
    """
    字符串反转
    :param s: 要反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    截取字符串
    :param s: 需要截取的字符串
    :param x: 开始位置
    :param y: 结束位置
    :return: 截取后的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_revers('hello'))
    print(substr('hello', 1, 3))
