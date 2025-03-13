# -*- coding: utf-8 -*-

"""
@date: 2025/2/16 下午10:44
@file: xxxx.py
@author: zj
@description: 房屋布局图绘制，包含客厅、卧室、卫生间、L型对称楼梯等区域。
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布
fig, ax = plt.subplots(figsize=(8, 12))
ax.set_xlim(0, 8)  # 面宽8米
ax.set_ylim(0, 12)  # 进深12米
ax.set_aspect('equal')  # 确保比例一致

# 手动设置x轴和y轴的刻度间隔为1米
ax.set_xticks(range(0, 9))  # x轴从0到8，每隔1米一个刻度
ax.set_yticks(range(0, 13))  # y轴从0到12，每隔1米一个刻度

# 添加标题和网格
plt.title("房屋顶楼布局图", fontsize=16, fontweight='bold', pad=20)
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

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
    '阳台': '#D5E8D4',  # 浅薄荷绿（阳台）
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
        exclude = []
    if adjacent is None:
        adjacent = []

    if 'left' not in exclude and 'left' not in adjacent:
        ax.add_patch(patches.Rectangle((x, y), wall_thickness, height, facecolor='gray', edgecolor='black'))
    if 'right' not in exclude and 'right' not in adjacent:
        ax.add_patch(patches.Rectangle((x + width - wall_thickness, y), wall_thickness, height - wall_thickness,
                                       facecolor='gray', edgecolor='black'))
    if 'bottom' not in exclude and 'bottom' not in adjacent:
        ax.add_patch(patches.Rectangle((x, y), width, wall_thickness, facecolor='gray', edgecolor='black'))
    if 'top' not in exclude and 'top' not in adjacent:
        ax.add_patch(patches.Rectangle((x, y + height - wall_thickness), width, wall_thickness, facecolor='gray',
                                       edgecolor='black'))


# 绘制各个功能区并调整文字位置

# 楼梯：位于右侧最里面的区域
draw_wall(5.5 - wall_thickness, 8 - wall_thickness, 2.5 + wall_thickness, 4 + wall_thickness,
          exclude=['left', 'bottom'], adjacent=['left', 'bottom'])
ax.add_patch(
    patches.Rectangle((5.5 - wall_thickness, 8 - wall_thickness), 2.5, 4,
                      facecolor=colors['楼梯'], edgecolor='black', label='楼梯'))
# 文字水平居中
ax.text(6.75, 10, "楼梯\n面宽2.5m x 进深4m", ha='center', va='center', fontsize=10, color='black')

# 储物间（左侧）
draw_wall(0, 8, 3, 4, adjacent=['bottom', 'right'])
ax.add_patch(patches.Rectangle((wall_thickness, 8), 3 - wall_thickness, 4 - wall_thickness,
                               facecolor=colors['储物间'], edgecolor='black', label='储物间'))
# 文字水平居中
ax.text(1.5, 10, f"储物间\n面宽{3 - wall_thickness:.2f}m x 进深{4 - wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 储物间（中间）
draw_wall(3, 8, 2.5 - wall_thickness, 4, adjacent=['bottom'])
ax.add_patch(
    patches.Rectangle((3 + wall_thickness, 8), 2.5 - 3 * wall_thickness, 4 - wall_thickness,
                      facecolor=colors['储物间'], edgecolor='black', label='储物间'))
# 文字水平居中
ax.text(4.25, 10, f"储物间\n面宽{2.5 - 3 * wall_thickness:.2f}m x 进深{4 - wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 楼梯平台：宽2.75米，长1.5米
draw_wall(5 - wall_thickness, 6.5 - wall_thickness * 2, 3 + wall_thickness, 1.5 + wall_thickness * 2,
          exclude=['top', 'left'], adjacent=['top', 'left'])
ax.add_patch(
    patches.Rectangle((5, 6.5 - wall_thickness), 2.75, 1.5,
                      facecolor=colors['楼梯平台'], edgecolor='black', label='楼梯平台'))
ax.text(6.5, 7.25, "楼梯平台\n面宽2.75m x 进深1.5m", ha='center', va='center', fontsize=10, color='black')

# 走廊：剩余部分
draw_wall(0, 6.5 - 2 * wall_thickness, 5 + wall_thickness, 1.5 + 2 * wall_thickness,
          exclude=['right', ], adjacent=['right', ])
ax.add_patch(patches.Rectangle((wall_thickness, 6.5 - wall_thickness), 5 - wall_thickness, 1.5,
                               facecolor=colors['走廊'], edgecolor='black'))
# 文字水平居中
ax.text(2.5, 7.25, f"走廊\n面宽{5 - wall_thickness :.2f}m x 进深1.5m",
        ha='center', va='center', fontsize=10, color='black')

# 储物间（右下角）
draw_wall(4 - wall_thickness, 0, 4 + wall_thickness, 6 + wall_thickness)  # 排除顶部墙壁
ax.add_patch(
    patches.Rectangle((4, wall_thickness), 4 - wall_thickness, 6 - wall_thickness,
                      facecolor=colors['储物间'], edgecolor='black', linewidth=1.5))
ax.text(6, 3.25, f"储物间\n面宽{4 - wall_thickness:.2f}m x 进深{6 - wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10, color='black', fontweight='bold')

# 阳台：位于最前面的区域
draw_wall(0, 0, 4, 6.5 - wall_thickness)  # 排除底部墙壁（大门区域）
ax.add_patch(
    patches.Rectangle((wall_thickness, wall_thickness), 4 - 2 * wall_thickness, 6.5 - wall_thickness * 3,
                      facecolor=colors['阳台'], edgecolor='black', label='阳台'))
# 文字水平居中
ax.text(2, 3.25, f"阳台\n面宽{4 - 2 * wall_thickness:.2f}m x 进深{6.5 - wall_thickness * 3:.2f}m",
        ha='center', va='center', fontsize=10)

# 显示坐标轴标签
plt.xlabel("南 面宽 (米)", fontsize=12, labelpad=10)
plt.ylabel("西 进深 (米)", fontsize=12, labelpad=10)

# # 添加图例
# handles, labels = [], []
# for region, color in colors.items():
#     handles.append(patches.Patch(color=color, label=region))
# plt.legend(handles=handles, loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# 显示图形
plt.tight_layout()
plt.show()
