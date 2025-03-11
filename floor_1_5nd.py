# -*- coding: utf-8 -*-

"""
@date: 2025/2/16 下午10:44
@file: xxxx.py
@author: zj
@description:
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 设置中文字体以支持中文标签显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建画布并设置绘图区域比例
fig, ax = plt.subplots(figsize=(8, 12))  # 图形大小为8x12英寸
ax.set_xlim(0, 8)  # 面宽8米
ax.set_ylim(0, 12)  # 进深12米
ax.set_aspect('equal')  # 确保图形比例一致

# 添加标题和网格线
plt.title("厨房布局图", fontsize=16)  # 设置标题
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)  # 添加虚线网格

# 定义各功能区的颜色
colors = {
    '客厅': '#D3E4CD',  # 清新浅绿色
    '主卧': '#F9E79F',  # 温暖柠檬黄
    '次卧': '#ABEBC6',  # 舒适薄荷绿
    '楼梯': '#FAD7A0',  # 柔和杏色
    '卫生间': '#F4CCCC',  # 淡雅粉红
    '储物间': '#D7BDE2',  # 淡紫罗兰
    '车库': '#D3D3D3',  # 浅灰色
    '走廊': '#EAECEE',  # 浅灰蓝
    '楼梯平台': '#F5B041',  # 明亮橙色
    '厨房': '#F9E79F',  # 柠檬黄（厨房）
}

# 墙壁厚度
wall_thickness = 0.25


# 绘制墙壁
def draw_wall(x, y, width, height, exclude=None, adjacent=None):
    """
    绘制墙壁，排除或根据相邻区域避免重复绘制。

    参数：
    x, y: 功能区左下角坐标
    width, height: 功能区宽度和高度
    exclude: 排除的墙壁方向 ('left', 'right', 'top', 'bottom')
    adjacent: 相邻区域信息，用于避免重复绘制墙壁
    """
    if exclude is None:
        exclude = list()
    if adjacent is None:
        adjacent = list()
    if not isinstance(exclude, list):
        exclude = [exclude]

    if ('left' not in exclude) and ('left' not in adjacent):
        ax.add_patch(patches.Rectangle((x, y), wall_thickness, height, facecolor='gray', edgecolor='black'))
    if ('right' not in exclude) and ('right' not in adjacent):
        ax.add_patch(patches.Rectangle((x + width - wall_thickness, y), wall_thickness, height - wall_thickness,
                                       facecolor='gray', edgecolor='black'))
    if ('bottom' not in exclude) and ('bottom' not in adjacent):
        ax.add_patch(patches.Rectangle((x, y), width, wall_thickness, facecolor='gray', edgecolor='black'))
    if ('top' not in exclude) and ('top' not in adjacent):
        ax.add_patch(patches.Rectangle((x, y + height - wall_thickness), width, wall_thickness, facecolor='gray',
                                       edgecolor='black'))


# 绘制各个功能区

# 客厅：位于最前面的区域，右侧与楼梯平台之间有墙
draw_wall(0, 0, 8, 6.5 - wall_thickness)  # 排除底部墙壁（大门区域）
# 注意：客厅右侧与楼梯平台之间有一堵墙，占用客厅空间
ax.add_patch(
    patches.Rectangle((wall_thickness, wall_thickness), 8 - 2 * wall_thickness, 6.5 - 3 * wall_thickness,
                      facecolor=colors['客厅'], edgecolor='black', label='客厅'))
# 调整文字位置使其居中
ax.text(4, (6.5 - 3 * wall_thickness) / 2 + wall_thickness,
        f"客厅\n面宽{8 - 2 * wall_thickness:.2f}m x 进深{6.5 - 3 * wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 楼梯：位于右侧最里面的区域
draw_wall(5.5 - wall_thickness, 8 - wall_thickness, 2.5 + wall_thickness, 4 + wall_thickness,
          exclude=['left', 'bottom'], adjacent=['left', 'bottom'])
ax.add_patch(
    patches.Rectangle((5.5 - wall_thickness, 8 - wall_thickness), 2.5, 4,
                      facecolor=colors['楼梯'], edgecolor='black', label='楼梯'))
# 调整文字位置使其居中
ax.text(5.5 + 2.5 / 2, 8 + 4 / 2, "楼梯\n面宽2.5m x 进深4m", ha='center', va='center', fontsize=10)

# 厨房：重新定义颜色和文字描述
draw_wall(0, 6.5 - 2 * wall_thickness, 5.5 - wall_thickness, 5.5 + 2 * wall_thickness)
ax.add_patch(
    patches.Rectangle((wall_thickness, 6.5 - wall_thickness), 5.5 - 3 * wall_thickness, 5.5,
                      facecolor=colors['厨房'], edgecolor='black', linewidth=1.5, label='厨房'))
# 调整文字位置使其居中
ax.text(5.5 / 2, 6.5 + 5.5 / 2, f"厨房\n面宽{5.5 - 3 * wall_thickness:.2f}m x 进深{5.5:.2f}m", ha='center', va='center',
        fontsize=10,
        fontweight='bold', linespacing=1.5)

# 走廊：位于楼梯、卫生间和车库的前面
# 修改为两部分：楼梯平台和其他走廊
# 楼梯平台：宽2.75米，长1.5米
draw_wall(5, 6.5 - wall_thickness * 2, 3, 1.5 + wall_thickness * 2,
          exclude=['top', 'left'], adjacent=['top', 'left'])
ax.add_patch(
    patches.Rectangle((5, 6.5 - wall_thickness), 2.75, 1.5,
                      facecolor=colors['楼梯平台'], edgecolor='black', label='楼梯平台'))
ax.text(6.5, 7.25, "楼梯平台\n面宽2.75m x 进深1.5m", ha='center', va='center', fontsize=10)

# 绘制大门：位于正面右侧进入，使用双向大门表示
door_x_start = 4 + (4 - 1.8) / 2  # 大门起始x坐标（右半侧中央）
door_y_bottom = 0  # 大门底部y坐标
door_length = 1.8  # 大门长度

# 使用两条粗线表示双向大门
ax.plot([door_x_start, door_x_start + door_length], [door_y_bottom, door_y_bottom],
        color='black', linewidth=4, label='大门')

# 显示坐标轴标签
plt.xlabel("面宽 (米)", fontsize=12)
plt.ylabel("进深 (米)", fontsize=12)

# 校验面宽和进深
assert ax.get_xlim() == (0, 8), "面宽应为8米"
assert ax.get_ylim() == (0, 12), "进深应为12米"

# 显示图形
plt.tight_layout()
plt.show()
