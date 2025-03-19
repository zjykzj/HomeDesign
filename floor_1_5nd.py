# -*- coding: utf-8 -*-

"""
@date: 2025/2/16 下午10:44
@file: xxxx.py
@author: zj
@description:
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from globals import wall_thickness, colors, FLOOR_1_5_TITLE
from globals import draw_wall

# 设置中文字体以支持中文标签显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建画布并设置绘图区域比例
fig, ax = plt.subplots(figsize=(8, 12))  # 图形大小为8x12英寸
ax.set_xlim(0, 8)  # 面宽8米
ax.set_ylim(0, 12)  # 进深12米
ax.set_aspect('equal')  # 确保图形比例一致

# 手动设置x轴和y轴的刻度间隔为1米
ax.set_xticks(range(0, 9))  # x轴从0到8，每隔1米一个刻度
ax.set_yticks(range(0, 13))  # y轴从0到12，每隔1米一个刻度

# 添加标题和网格线
plt.title(FLOOR_1_5_TITLE, fontsize=16)  # 设置标题
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)  # 添加虚线网格

# 绘制各个功能区

# 客厅：位于最前面的区域，右侧与楼梯平台之间有墙
draw_wall(ax, 0, 0, 8, 6.5 - wall_thickness)  # 排除底部墙壁（大门区域）
# 注意：客厅右侧与楼梯平台之间有一堵墙，占用客厅空间
ax.add_patch(
    patches.Rectangle((wall_thickness, wall_thickness), 8 - 2 * wall_thickness, 6.5 - 3 * wall_thickness,
                      facecolor=colors['客厅'], edgecolor='black', label='客厅'))
# 调整文字位置使其居中
ax.text(4, (6.5 - 3 * wall_thickness) / 2 + wall_thickness,
        f"客厅\n面宽{8 - 2 * wall_thickness:.2f}m x 进深{6.5 - 3 * wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)
# 添加一个半透明的矩形表示阴影
shadow = patches.Rectangle((wall_thickness, wall_thickness), 8 - 2 * wall_thickness, 6.5 - 3 * wall_thickness,
                           alpha=0.3, facecolor='gray', edgecolor='none', zorder=2)
ax.add_patch(shadow)
# 使用斜线填充来强调区域
hatch_emphasis = patches.Rectangle((wall_thickness, wall_thickness), 8 - 2 * wall_thickness, 6.5 - 3 * wall_thickness,
                                   facecolor='none', hatch='///', edgecolor='gray', linewidth=1, zorder=2)
ax.add_patch(hatch_emphasis)

# 楼梯：位于右侧最里面的区域
draw_wall(ax, 5, 8 - wall_thickness, 2.5 + 2 * wall_thickness, 4 + wall_thickness,
          exclude=['bottom'])
ax.add_patch(
    patches.Rectangle((5.5 - wall_thickness, 8 - wall_thickness), 2.5, 4,
                      facecolor=colors['楼梯'], edgecolor='black', label='楼梯'))
# 调整文字位置使其居中
ax.text(6.5, 8 + 4 / 2, "楼梯\n面宽2.5m x 进深4m", ha='center', va='center', fontsize=10)

# 调整文字位置使其居中
ax.text(5.5 / 2, 9,
        f"厨房区域 = (厨房1 + 厨房2)\n中间的空白线用来对齐一楼和顶楼的墙壁\n整体面宽{5.5 - 3 * wall_thickness:.2f}m x 整体进深{5.5:.2f}m",
        ha='center', va='center',
        fontsize=14,
        fontweight='bold', linespacing=1.5)

# 厨房1（左侧）
draw_wall(ax, 0, 6, 3, 6, adjacent=['bottom', 'right'])
ax.add_patch(patches.Rectangle((wall_thickness, 6 + wall_thickness), 3 - wall_thickness, 6 - 2 * wall_thickness,
                               facecolor=colors['厨房'], edgecolor='black', label='厨房'))
# 文字水平居中
ax.text(1.5, 10, f"厨房1\n面宽{3 - wall_thickness:.2f}m x 进深{6 - 2 * wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 厨房2（中间）
draw_wall(ax, 3, 6, 2.5 - wall_thickness, 6, exclude=['left', 'right', 'bottom'])
ax.add_patch(
    patches.Rectangle((3 + wall_thickness, 6 + wall_thickness), 2.5 - 3 * wall_thickness, 6 - 2 * wall_thickness,
                      facecolor=colors['厨房'], edgecolor='black', label='厨房'))
# 文字水平居中
ax.text(4.15, 10, f"厨房2\n面宽{2.5 - 3 * wall_thickness:.2f}m x 进深{6 - 2 * wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 楼梯平台：宽2.5米，长1.5米
draw_wall(ax, 5, 6, 3, 1.5 + wall_thickness * 2,
          exclude=['top', 'left'], adjacent=['top', 'left'])
ax.add_patch(
    patches.Rectangle((5 + wall_thickness, 6 + wall_thickness), 3 - 2 * wall_thickness, 1.5,
                      facecolor=colors['楼梯平台'], edgecolor='black', label='楼梯平台'))
ax.text(6.5, 7.25, f"楼梯平台\n面宽{3 - 2 * wall_thickness}m x 进深1.5m", ha='center', va='center', fontsize=10)

# 显示坐标轴标签
plt.xlabel("南 面宽 (米)", fontsize=12)
plt.ylabel("西 进深 (米)", fontsize=12)

# 校验面宽和进深
assert ax.get_xlim() == (0, 8), "面宽应为8米"
assert ax.get_ylim() == (0, 12), "进深应为12米"

# 显示图形
plt.tight_layout()
plt.show()
