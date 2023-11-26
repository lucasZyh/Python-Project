from my_utils import file_util
import my_utils.str_utils

s1 = my_utils.str_utils.str_revers('hello')
print(s1)
s2 = my_utils.str_utils.substr('hello', 1, 3)
print(s2)

file_util.print_file_inof('iodic.txt')