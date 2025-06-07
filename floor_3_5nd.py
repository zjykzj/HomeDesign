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
fig, ax = plt.subplots(figsize=(9, 12))
ax.set_xlim(0, 9)  # 面宽9米
ax.set_ylim(0, 12)  # 进深12米
ax.set_aspect('equal')  # 确保比例一致

# 手动设置x轴和y轴的刻度间隔为1米
ax.set_xticks(range(0, 10))  # x轴每隔1米一个刻度
ax.set_yticks(range(0, 13))  # y轴每隔1米一个刻度

# 添加标题和网格
plt.title(FLOOR_3_5_TITLE, fontsize=16, fontweight='bold', pad=20)
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# ------------------------------------- 绘制各个功能区并调整文字位置

# 楼梯：位于右侧最里面的区域
draw_wall(ax, 6.5 - wall_thickness, 8 - wall_thickness, 2.5 + wall_thickness, 4 + wall_thickness,
          exclude=['left', 'bottom'], adjacent=['left', 'bottom'])
ax.add_patch(
    patches.Rectangle((6.5 - wall_thickness, 8 - wall_thickness), 2.5, 4,
                      facecolor=colors['楼梯'], label='楼梯'))
ax.text(7.5, 10, "楼梯\n面宽2.5m", ha='center', va='center', fontsize=14)

# 储物间（楼梯左侧）
draw_wall(ax, 4, 8 - wall_thickness, 1.75 + 2 * wall_thickness, 3.75 + 2 * wall_thickness)  # 排除底部墙壁
ax.add_patch(patches.Rectangle((4 + wall_thickness, 8), 1.75, 3.75, facecolor=colors['储物间']))
ax.text(5.15, 10, f"储物间", ha='center', va='center', fontsize=14)

# 次卧（储物间旁边）
draw_wall(ax, 0, 8 - wall_thickness, 3.75 + 2 * wall_thickness, 3.75 + 2 * wall_thickness, exclude=['right'])  # 排除底部墙壁
ax.add_patch(patches.Rectangle((wall_thickness, 8), 3.75, 3.75, facecolor=colors['储物间']))
ax.text(2, 10, f"储物间", ha='center', va='center', fontsize=14)

# 楼梯平台：宽2.5米，长1.5米
draw_wall(ax, 6, 6, 3, 1.5 + wall_thickness * 2, exclude=['top', 'left', 'bottom'])
ax.add_patch(
    patches.Rectangle((6 + wall_thickness, 6 + wall_thickness), 3 - 2 * wall_thickness, 1.5,
                      facecolor=colors['楼梯平台'], label='楼梯平台'))
ax.text(7.5, 7.25, f"楼梯平台", ha='center', va='center', fontsize=14)

# 其他走廊：剩余部分
ax.add_patch(patches.Rectangle((2 + wall_thickness, 6.5 - wall_thickness), 3.75, 1.5,
                               facecolor=colors['走廊']))
ax.text(4, 7.25, f"走廊", ha='center', va='center', fontsize=14)

# 阳台：位于最前面的区域
draw_wall(ax, 0, 0, 4.75 + wall_thickness, 5.75 + 2 * wall_thickness, exclude=['top', 'right'])  # 排除顶部墙壁
ax.add_patch(patches.Rectangle((wall_thickness, wall_thickness), 4.75, 5.75, facecolor=colors['阳台'], label='阳台'))
ax.text(2.5, 3.5, f"阳台", ha='center', va='center', fontsize=14)

draw_wall(ax, 2, 0, 1 + wall_thickness, 5.75 + 2 * wall_thickness, exclude=['left', 'right'])  # 排除顶部墙壁

# 卫生间
draw_wall(ax, 0, 6, 1.75 + 2 * wall_thickness, 1.5 + 2 * wall_thickness, adjacent=['right'])
ax.add_patch(patches.Rectangle((wall_thickness, 6 + wall_thickness), 1.75, 1.5, facecolor=colors['卫生间']))
ax.text(1.13, 7.25, f"卫生间", ha='center', va='center', fontsize=14)

# 储物间（右下角）
draw_wall(ax, 5 - wall_thickness, 0, 3.75 + 2 * wall_thickness, 3.75 + 2 * wall_thickness)  # 排除顶部墙壁
ax.add_patch(patches.Rectangle((5, wall_thickness), 3.75, 3.75, facecolor=colors['储物间']))
ax.text(7, 2.25, f"储物间", ha='center', va='center', fontsize=14)

draw_wall(ax, 6, 4, 2.5 + 2 * wall_thickness, 1.75 + 2 * wall_thickness, exclude=['top', 'bottom', 'left'])
draw_wall(ax, 5 - wall_thickness, 4, 1 + 2 * wall_thickness, 1.75 + 2 * wall_thickness,
          exclude=['top', 'bottom', 'right'])

# 显示坐标轴标签
plt.xlabel("南 面宽 (米)", fontsize=12, labelpad=10)
plt.ylabel("西 进深 (米)", fontsize=12, labelpad=10)

# 显示图形
plt.tight_layout()
plt.show()
