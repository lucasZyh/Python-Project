import tkinter as tk  # 导入包，并取名为tk
from tkinter import messagebox  # 调用tkinter库里面的messagebox
import random  # 导入随机库

R = 20  # 行数
C = 12  # 列数
cell_size = 30  # 一个小方格的长度
height = R * cell_size  # 高
width = C * cell_size  # 宽
FPS = 300  # 设置页面刷新间隔

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


def draw_cell_by_cr(canvas, c, r, color="#CCCCCC"):  # 在画板上绘制单个俄罗斯方块的函数
    # 确定坐标
    x0 = c * cell_size
    y0 = r * cell_size
    x1 = x0 + cell_size
    y1 = y0 + cell_size
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=2)  # 在指定位置绘制矩形，填充颜色，设置边框的宽度、颜色


def draw_board(canvas, block_list):  # 在画板上绘制所有空白方块的函数
    for ri in range(R):  # 遍所有历行
        for ci in range(C):  # 遍历每一行中的每一列
            cell_type = block_list[ri][ci]  # 取出当前位置对应的值
            if cell_type:  # 如果有俄罗斯方块，按俄罗斯方块颜色绘制
                draw_cell_by_cr(canvas, ci, ri, SHAPESCOLOR[cell_type])
            else:  # 无俄罗斯方块，按默认颜色绘制
                draw_cell_by_cr(canvas, ci, ri)  # 所有闲置方格均设置默认颜色为背景


def draw_cells(canvas, c, r, cell_list, color="#CCCCCC"):  # 绘制指定形状和颜色的俄罗斯方块的函数
    for i in cell_list:  # 计算实际坐标
        cell_c, cell_r = i
        ci = cell_c + c
        ri = cell_r + r
        if 0 <= c < C and 0 <= r < R:  # 判断该位置是否在画板内
            draw_cell_by_cr(canvas, ci, ri, color)


win = tk.Tk()  # 建立一个窗口
canvas = tk.Canvas(win, width=width, height=height)  # 绘制画布
canvas.pack()  # 放置画布
block_list = []  # 创建列表，用来记录已固定的俄罗斯方块
for i in range(R):  # 制作一个R行C列的二维列表
    i_row = ['' for j in range(C)]
    block_list.append(i_row)

draw_board(canvas, block_list)


def draw_block_move(canvas, block, direction=[0, 0]):  # 绘制指定方向移动后的俄罗斯方块的函数
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


def generate_new_block():  # 随机生成新的俄罗斯方块的函数
    kind = random.choice(list(SHAPES.keys()))  # 随机选择俄罗斯方块类型
    cr = [C // 2, 0]
    new_block = {
        "kind": kind,
        "cell_list": SHAPES[kind],
        "cr": cr
    }
    return new_block  # 返回新生成的俄罗斯方块对象


def check_move(block, direction=[0, 0]):  # 判断俄罗斯方块是否可以向指定位置移动的函数
    cc, cr = block['cr']  # 当前俄罗斯方块对象的位置
    cell_list = block['cell_list']  # 相对自身的位置列表
    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc + direction[0]
        r = cell_r + cr + direction[1]
        if c < 0 or c >= C or r >= R:  # 判断俄罗斯方块移动后是是否会越界
            return False  # 返回值为假
        if r >= 0 and block_list[r][c]:
            return False  # 返回值为假
    return True  # 返回值为真


def save_block_to_list(block):  # 将无法移动的俄罗斯方块记录下来的函数
    shape_type = block['kind']
    cc, cr = block['cr']
    cell_list = block['cell_list']

    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc
        r = cell_r + cr
        block_list[r][c] = shape_type


def horizontal_move_block(event):  # 控制俄罗斯方块左右移动的函数
    direction = [0, 0]
    # 接收判断键盘输入的命令
    if event.keysym == 'Left':  # 是否向左
        direction = [-1, 0]
    elif event.keysym == 'Right':  # 是否向右
        direction = [1, 0]
    else:  # 无指令
        return

    global current_block  # 获取当前的俄罗斯方块对象
    if current_block is not None and check_move(current_block, direction):  # 判断是否为空且能否移动
        draw_block_move(canvas, current_block, direction)  # 移动绘制这个俄罗斯方块


def rotate_block(event):  # 让俄罗斯方块旋转的函数
    global current_block  # 获取当前俄罗斯方块
    if current_block is None:  # 判断是否为空
        return
    cell_list = current_block['cell_list']
    rotate_list = []
    for cell in cell_list:  # 对该俄罗斯方块的所有方格进行旋转变换
        cell_c, cell_r = cell
        rotate_cell = [cell_r, -cell_c]
        rotate_list.append(rotate_cell)

    # 生成一个旋转后的俄罗斯方块对象
    block_after_rotate = {
        'kind': current_block['kind'],  # 对应俄罗斯方块的类型
        'cell_list': rotate_list,
        'cr': current_block['cr']
    }

    if check_move(block_after_rotate):  # 判断旋转后的俄罗斯方块能否移动
        cc, cr = current_block['cr']
        draw_cells(canvas, cc, cr, current_block['cell_list'])  # 清楚旧的俄罗斯方块
        draw_cells(canvas, cc, cr, rotate_list, SHAPESCOLOR[current_block['kind']])  # 绘制新的俄罗斯方块
        current_block = block_after_rotate  # 更改变量


def check_row_complete(row):
    for cell in row:
        if cell == '':
            return False
    return True


score = 0  # 给成绩变量赋初值
win.title("SCORES: %s" % score)  # 在标题上显示分数


def check_and_clear():  # 检查并且清楚排满的行的函数
    has_complete_row = False
    for ri in range(len(block_list)):
        if check_row_complete(block_list[ri]):  # 判断有没有可以删除的行
            has_complete_row = True
            if ri > 0:  # 判断是否为第一行
                for cur_ri in range(ri, 0, -1):  # 从下往上遍历，让当前行等于上一行
                    block_list[cur_ri] = block_list[cur_ri - 1][:]
                block_list[0] = ['' for j in range(C)]
            else:  # 如果为第一行，建立一个空行
                block_list[ri] = ['' for j in range(C)]
            global score  # 读取分数
            score += 10  # 加分
    if has_complete_row:  # 判断是否有清楚的行，有的话加分
        draw_board(canvas, block_list)
        win.title("SCORES: %s" % score)


def land(event):  # 让俄罗斯方块立即着陆的函数
    global current_block  # 获取当前俄罗斯方块
    if current_block is None:  # 判断是否为空
        return
    cell_list = current_block['cell_list']
    cc, cr = current_block['cr']
    min_height = R
    for cell in cell_list:
        cell_c, cell_r = cell
        c, r = cell_c + cc, cell_r + cr
        if block_list[r][c]:  # 判断是否冲突
            return
        h = 0
        for ri in range(r + 1, R):  # 遍历该指令的方格
            if block_list[ri][c]:  # 判断下面是否有固定的物体
                break  # 如果有，跳出循环
            else:  # 如果没有
                h = h + 1  # 行数加一
        if h < min_height:  # 判断大小
            min_height = h  # 更新最小值
    down = [0, min_height]
    if check_move(current_block, down):  # 判断是否能移动
        draw_block_move(canvas, current_block, down)


def game_loop():
    win.update()
    global current_block  # 引入全局变量
    if current_block is None:  # 判断是否存在
        new_block = generate_new_block()  # 新生成一个俄罗斯方块
        draw_block_move(canvas, new_block)  # 移动俄罗斯方块
        current_block = new_block  # 当前俄罗斯方块对象为新生成的俄罗斯方块
        if not check_move(current_block, [0, 0]):  # 判断能否继续向下生成俄罗斯方块
            messagebox.showinfo("Game Over!", "Your Score is %s" % score)  # 跳出弹窗，游戏结束
            win.destroy()
            return
    else:
        if check_move(current_block, [0, 1]):  # 判断能否继续向下移动
            draw_block_move(canvas, current_block, [0, 1])  # 直接向下移动俄罗斯方块
        else:
            save_block_to_list(current_block)  # 将不能移动的俄罗斯方块存入列表
            current_block = None
    check_and_clear()
    win.after(FPS, game_loop)


canvas.focus_set()  # 聚焦到canvas画板对象上
# 绑定方向键
canvas.bind("<KeyPress-Left>", horizontal_move_block)
canvas.bind("<KeyPress-Right>", horizontal_move_block)
canvas.bind("<KeyPress-Up>", rotate_block)
canvas.bind("<KeyPress-Down>", land)

current_block = None  # 定义初始值为none
game_loop()  # 调用函数，定时刷新页面
win.mainloop()  # 维持窗口
