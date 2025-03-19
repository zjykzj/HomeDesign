# -*- coding: utf-8 -*-

"""
@date: 2025/2/16 下午10:44
@file: xxxx.py
@author: zj
@description:
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from globals import wall_thickness, colors, FLOOR_1_TITLE
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
plt.title(FLOOR_1_TITLE, fontsize=16)  # 设置标题
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)  # 添加虚线网格

# 绘制各个功能区

# 客厅：位于最前面的区域，右侧与楼梯平台之间有墙
draw_wall(ax, 0, 0, 8, 6 + wall_thickness, exclude=['top'])  # 排除底部墙壁（大门区域）
# 注意：客厅右侧与楼梯平台之间有一堵墙，占用客厅空间
ax.add_patch(
    patches.Rectangle((wall_thickness, wall_thickness), 8 - 2 * wall_thickness, 6 - wall_thickness,
                      facecolor=colors['客厅'], edgecolor='black', label='客厅'))
ax.text(4, 3.25, f"客厅\n面宽{8 - 2 * wall_thickness:.2f}m x 进深{6 - wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 楼梯：位于右侧最里面的区域
draw_wall(ax, 5, 8 - wall_thickness, 2.5 + 2 * wall_thickness, 4 + wall_thickness,
          exclude=['bottom'], adjacent=['bottom'])
ax.add_patch(
    patches.Rectangle((5 + wall_thickness, 8 - wall_thickness), 2.5, 4,
                      facecolor=colors['楼梯'], edgecolor='black', label='楼梯'))
ax.text(6.5, 10, f"楼梯\n面宽2.5m x 进深{4}m", ha='center', va='center', fontsize=10)

# 车库：位于左侧最里面的区域
draw_wall(ax, 0, 8 - wall_thickness, 3 + wall_thickness, 4 + wall_thickness, adjacent=[])
ax.add_patch(patches.Rectangle((wall_thickness, 8), 3 - wall_thickness, 4 - wall_thickness,
                               facecolor=colors['车库'], edgecolor='black', label='车库'))
ax.text(1.5, 10, f"车库\n面宽{3 - wall_thickness:.2f}m x 进深{4 - wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 卫生间
draw_wall(ax, 3, 9, 2.5 - wall_thickness, 3, adjacent=['left', 'right'])
ax.add_patch(
    patches.Rectangle((3 + wall_thickness, 9 + wall_thickness), 2.5 - 3 * wall_thickness, 3 - 2 * wall_thickness,
                      facecolor=colors['卫生间'], edgecolor='black', label='卫生间'))
ax.text(4.15, 10, f"卫生间\n面宽{2.5 - 3 * wall_thickness:.2f}m x 进深{3 - 2 * wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 走廊：位于楼梯、卫生间和车库的前面
# 修改为两部分：楼梯平台和其他走廊
# 楼梯平台：宽2.5米，长1.5米
draw_wall(ax, 5, 6, 3, 1.5 + wall_thickness * 2,
          exclude=['top', 'left'], adjacent=['top', 'left'])
ax.add_patch(
    patches.Rectangle((5 + wall_thickness, 6 + wall_thickness), 3 - 2 * wall_thickness, 1.5,
                      facecolor=colors['楼梯平台'], edgecolor='black', label='楼梯平台'))
ax.text(6.5, 7.25, f"楼梯平台\n面宽{3 - 2 * wall_thickness}m x 进深1.5m", ha='center', va='center', fontsize=10)

# 其他走廊：剩余部分
draw_wall(ax, 0, 6.5 - wall_thickness, 5 + wall_thickness, 1.5 + wall_thickness,
          exclude=['top', 'right', 'bottom'], adjacent=['top', 'right', 'bottom'])
ax.add_patch(patches.Rectangle((wall_thickness, 6.5 - wall_thickness), 5 - wall_thickness, 1.5,
                               facecolor=colors['走廊'], edgecolor='black'))
ax.text(2.5, 7.25, f"走廊\n面宽{5 - wall_thickness :.2f}m x 进深1.5m",
        ha='center', va='center', fontsize=10)

# # 新增: 绘制大门
# door_width = 1.8  # 大门宽度
# door_height = wall_thickness  # 假设大门高度等于墙体厚度
# door_x = 4 + (4 - door_width) / 2  # 计算大门中心点x坐标以使其居中
# door_y = 0  # 大门位于底部
#
# ax.add_patch(
#     patches.Rectangle((door_x, door_y), door_width, door_height,
#                       facecolor='blue', edgecolor='black', label='大门'))  # 蓝色表示大门
# ax.text(door_x + door_width / 2, door_y + door_height / 2, "大门", ha='center', va='center', fontsize=8, color='white')
#
# # 注意：客厅右侧与楼梯平台之间有一堵墙，占用客厅空间
# ax.add_patch(
#     patches.Rectangle((wall_thickness, wall_thickness), 8 - 2 * wall_thickness, 6.5 - wall_thickness * 2,
#                       facecolor=colors['客厅'], edgecolor='black', label='客厅'))
# ax.text(4, 3.25, f"客厅\n面宽{8 - 2 * wall_thickness:.2f}m x 进深{6.5 - wall_thickness * 3:.2f}m",
#         ha='center', va='center', fontsize=10)

# 显示坐标轴标签
plt.xlabel("南 面宽 (米)", fontsize=12)
plt.ylabel("西 进深 (米)", fontsize=12)

# 显示图形
plt.tight_layout()
plt.show()
