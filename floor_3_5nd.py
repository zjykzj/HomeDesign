# -*- coding: utf-8 -*-

"""
@date: 2025/2/16 下午10:44
@file: xxxx.py
@author: zj
@description: 房屋布局图绘制，包含客厅、卧室、卫生间、L型对称楼梯等区域。
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from globals import wall_thickness, colors, FLOOR_3_5_TITLE
from globals import draw_wall

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
plt.title(FLOOR_3_5_TITLE, fontsize=16, fontweight='bold', pad=20)
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# 绘制各个功能区并调整文字位置

# 楼梯：位于右侧最里面的区域
draw_wall(ax, 5.5 - wall_thickness, 8 - wall_thickness, 2.5 + wall_thickness, 4 + wall_thickness,
          exclude=['left', 'bottom'], adjacent=['left', 'bottom'])
ax.add_patch(
    patches.Rectangle((5.5 - wall_thickness, 8 - wall_thickness), 2.5, 4,
                      facecolor=colors['楼梯'], edgecolor='black', label='楼梯'))
# 文字水平居中
ax.text(6.5, 10, "楼梯\n面宽2.5m x 进深4m", ha='center', va='center', fontsize=10, color='black')

# 储物间（左侧）
draw_wall(ax, 0, 8, 3, 4, adjacent=['bottom', 'right'])
ax.add_patch(patches.Rectangle((wall_thickness, 8), 3 - wall_thickness, 4 - wall_thickness,
                               facecolor=colors['储物间'], edgecolor='black', label='储物间'))
# 文字水平居中
ax.text(1.5, 10, f"储物间\n面宽{3 - wall_thickness:.2f}m x 进深{4 - wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 储物间（中间）
draw_wall(ax, 3, 8, 2.5 - wall_thickness, 4, adjacent=['bottom'])
ax.add_patch(
    patches.Rectangle((3 + wall_thickness, 8), 2.5 - 3 * wall_thickness, 4 - wall_thickness,
                      facecolor=colors['储物间'], edgecolor='black', label='储物间'))
# 文字水平居中
ax.text(4.15, 10, f"储物间\n面宽{2.5 - 3 * wall_thickness:.2f}m x 进深{4 - wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10)

# 楼梯平台：宽2.5米，长1.5米
draw_wall(ax, 5, 6, 3, 1.5 + wall_thickness * 2,
          exclude=['top', 'left', 'bottom'], adjacent=['top', 'left'])
ax.add_patch(
    patches.Rectangle((5 + wall_thickness, 6 + wall_thickness), 3 - 2 * wall_thickness, 1.5,
                      facecolor=colors['楼梯平台'], edgecolor='black', label='楼梯平台'))
ax.text(6.5, 7.25, f"楼梯平台\n面宽{3 - 2 * wall_thickness}m x 进深1.5m", ha='center', va='center', fontsize=10)

# 走廊：剩余部分
draw_wall(ax, 2 - wall_thickness, 6.5 - 2 * wall_thickness, 3 + 2 * wall_thickness, 1.5 + 2 * wall_thickness,
          exclude=['right', 'bottom'], adjacent=['right', 'bottom'])
ax.add_patch(patches.Rectangle((2, 6.5 - wall_thickness), 3, 1.5,
                               facecolor=colors['走廊'], edgecolor='black'))
# 文字水平居中
ax.text(3.5, 7.25, f"走廊\n面宽{3}m x 进深1.5m",
        ha='center', va='center', fontsize=10, color='black')

# 客厅卫生间：位于次卧上方
draw_wall(ax, 0, 6, 2, 2)
ax.add_patch(
    patches.Rectangle((wall_thickness, 6 + wall_thickness), 2 - 2 * wall_thickness, 2 - 2 * wall_thickness,
                      facecolor=colors['卫生间'], edgecolor='black', linewidth=1.5))
ax.text(1, 7.25, f"卫生间\n面宽{1.5}m x 进深{1.5}m",
        ha='center', va='center', fontsize=10, color='black', fontweight='bold')

# 储物间（右下角）
draw_wall(ax, 4 - wall_thickness, 4, 4 + wall_thickness, 2 + wall_thickness,
          exclude=['top', 'left', 'bottom'], )  # 排除顶部墙壁
draw_wall(ax, 4 - wall_thickness, 0, 4 + wall_thickness, 4 + wall_thickness)  # 排除顶部墙壁
ax.add_patch(
    patches.Rectangle((4, wall_thickness), 4 - wall_thickness, 4 - wall_thickness,
                      facecolor=colors['储物间'], edgecolor='black', linewidth=1.5))
ax.text(6, 3.25, f"储物间\n面宽{4 - wall_thickness:.2f}m x 进深{4 - wall_thickness:.2f}m",
        ha='center', va='center', fontsize=10, color='black', fontweight='bold')

# 阳台：位于最前面的区域
draw_wall(ax, 0, 0, 4, 6.5 - wall_thickness)  # 排除底部墙壁（大门区域）
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
