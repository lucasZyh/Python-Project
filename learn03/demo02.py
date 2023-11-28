"""
    类型注解
"""

# 变量
var_1: int = 10
var_2: str = "hello"
var_3: bool = True
var_4: float = 3.14


# 类对象
class news:
    print("news")


new: news = news()

# 容器
list_1 = [1, 2, 3]  # type: list[int]
tuple_1 = (1, "hello", True)  # type: tuple[int, str, bool]
set_1 = {1, 2, 3}  # type: set[int]
dict_1 = {"a": 1, "b": 2, "c": 3}  # type: dict[str, int]


# 函数
def func_1(a: int, b: int) -> int:
    return a + b
