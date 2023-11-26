import tkinter as tk  # 导入包，并取名为tk
import random  # 导入随机库

R = 20  # 行数
C = 12  # 列数
cell = 30  # 一个小方格的长度
height = R * cell  # 高
width = C * cell  # 宽
FPS = 100  # 设置页面刷新间隔

# 创建字典，存放俄罗斯方块形状的对应坐标
SHAPES = {
    "Z": [(-1, -1), (0, -1), (0, 0), (1, 0)],
    "O": [(-1, -1), (0, -1), (-1, 0), (0, 0)],
    "S": [(-1, 0), (0, 0), (0, -1), (1, -1)],
    "T": [(-1, 0), (0, 0), (0, -1), (1, 0)],
    "I": [(0, 1), (0, 0), (0, -1), (0, -2)],
    "L": [(-1, 0), (0, 0), (-1, -1), (-1, -2)],
    "J": [(-1, 0), (0, 0), (0, -1), (0, -2)]
}

# 创建字典，存放不同俄罗斯方块对应的不同颜色
SHAPESCOLOR = {
    "O": "blue",
    "Z": "Cyan",
    "S": "red",
    "T": "yellow",
    "I": "green",
    "L": "purple",
    "J": "orange",
}


def draw_cell_by_cr(canvas, c, r, color="#CCCCCC"):  # 定义在画板上绘制单个俄罗斯方块的函数
    """
        :param canvas: 画板，用于绘制一个方块的Canvas对象
        :param c: 方块所在列
        :param r: 方块所在行
        :param color: 方块颜色，默认为#CCCCCC，轻灰色
        :return:
        """
    # 确定坐标
    x0 = c * cell
    y0 = r * cell
    x1 = x0 + cell
    y1 = y0 + cell
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=2)  # 在指定位置绘制矩形，填充颜色，设置边框的宽度、颜色


def draw_blank_board(canvas):  # 在画板上绘制所有空白方块
    for ri in range(R):  # 遍所有历行
        for ci in range(C):  # 遍历每一行中的每一列
            draw_cell_by_cr(canvas, ci, ri)  # 所有闲置方格均设置默认颜色为背景


def draw_cells(canvas, c, r, cell_list, color="#CCCCCC"):  # 绘制指定形状和颜色的俄罗斯方块
    for i in cell_list:  # 计算实际坐标
        cell_c, cell_r = i
        ci = cell_c + c
        ri = cell_r + r
        if 0 <= c < C and 0 <= r < R:  # 判断该位置是否在画板内
            draw_cell_by_cr(canvas, ci, ri, color)


def draw_block_move(canvas, block, direction=[0, 0]):  # 绘制指定方向移动后的俄罗斯方块
    shape_type = block['kind']
    c, r = block['cr']
    cell_list = block['cell_list']

    # 移动前，先清除原有位置绘制的俄罗斯方块,也就是用背景色绘制原有的俄罗斯方块
    draw_cells(canvas, c, r, cell_list)
    dc, dr = direction
    new_c, new_r = c + dc, r + dr
    block['cr'] = [new_c, new_r]

    # 在新位置绘制新的俄罗斯方块
    draw_cells(canvas, new_c, new_r, cell_list, SHAPESCOLOR[shape_type])


def generate_new_block():  # 随机生成新的俄罗斯方块
    kind = random.choice(list(SHAPES.keys()))  # 随机选择俄罗斯方块类型
    cr = [C // 2, 0]
    new_block = {
        "kind": kind,
        "cell_list": SHAPES[kind],
        "cr": cr
    }
    return new_block


def check_move(block, direction=[0, 0]):
    """
        判断俄罗斯方块是否可以朝制定方向移动
        :param block: 俄罗斯方块对象
        :param direction: 俄罗斯方块移动方向
        :return: boolean 是否可以朝制定方向移动
        """
    cc, cr = block['cr']
    cell_list = block['cell_list']

    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc + direction[0]
        r = cell_r + cr + direction[1]
        # 判断该位置是否超出左右边界，以及下边界
        # 一般不判断上边界，因为俄罗斯方块生成的时候，可能有一部分在上边界之上还没有出来
        if c < 0 or c >= C or r >= R:
            return False

    return True


def game_loop():
    win.update()
    global current_block  # 引入全局变量
    if current_block is None:  # 判断是否存在
        new_block = generate_new_block()  # 新生成一个俄罗斯方块
        draw_block_move(canvas, new_block)  # 移动俄罗斯方块
        current_block = new_block  # 当前俄罗斯方块对象为新生成的俄罗斯方块
    else:
        if check_move(current_block, [0, 1]):  # 判断能否继续向下移动
            draw_block_move(canvas, current_block, [0, 1])  # 直接向下移动俄罗斯方块
        else:
            current_block = None
    win.after(FPS, game_loop)



current_block = None

win = tk.Tk()  # 建立一个窗口
canvas = tk.Canvas(win, width=width, height=height)  # 绘制画布
canvas.pack()  # 放置画布

draw_blank_board(canvas)
current_block = None  # 定义初始值为none
game_loop()
win.mainloop()  # 维持窗口
