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
plt.title("房屋一楼布局图", fontsize=16)  # 设置标题
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)  # 添加虚线网格

# 定义各功能区的颜色
colors = {
    '客厅': '#AED6F1',  # 浅蓝色
    '楼梯': '#F7DC6F',  # 浅黄色（楼梯）
    '卫生间': '#F1948A',  # 浅红色
    '储物间': '#D7BDE2',  # 淡紫色（储物间）
    '车库': '#D3D3D3',  # 浅灰色（车库）
    '走廊': '#E5E4E2',  # 浅灰色（走廊）
    '楼梯平台': '#F5B041',  # 橙色（楼梯平台）
}

# 绘制各个功能区
# 客厅：位于最前面的区域
ax.add_patch(patches.Rectangle((0, 0), 8, 6.5, facecolor=colors['客厅'], edgecolor='black', label='客厅'))
ax.text(4, 3.25, "客厅\n8m x 6.5m", ha='center', va='center', fontsize=10)

# 走廊：位于楼梯、卫生间和车库的前面
# 修改为两部分：楼梯平台和其他走廊
# 楼梯平台：宽3米，长1.5米
ax.add_patch(patches.Rectangle((5, 6.5), 3, 1.5, facecolor=colors['楼梯平台'], edgecolor='black', label='楼梯平台'))
ax.text(6.5, 7.25, "楼梯平台\n3m x 1.5m", ha='center', va='center', fontsize=10)

# 其他走廊：剩余部分
ax.add_patch(patches.Rectangle((0, 6.5), 5, 1.5, facecolor=colors['走廊'], edgecolor='black'))
ax.text(2.5, 7.25, "走廊\n5m x 1.5m", ha='center', va='center', fontsize=10)

# 楼梯：位于右侧最里面的区域
ax.add_patch(patches.Rectangle((5.5, 8), 2.5, 4, facecolor=colors['楼梯'], edgecolor='black', label='楼梯'))
ax.text(6.75, 10, "楼梯\n2.5m x 4m", ha='center', va='center', fontsize=10)

# 卫生间和储物间：水平分割
# 储物间：位于前面
ax.add_patch(patches.Rectangle((3, 8), 2.5, 2, facecolor=colors['储物间'], edgecolor='black', label='储物间'))
ax.text(4.25, 9, "储物间\n2.5m x 2m", ha='center', va='center', fontsize=10)

# 卫生间：位于后面
ax.add_patch(patches.Rectangle((3, 10), 2.5, 2, facecolor=colors['卫生间'], edgecolor='black', label='卫生间'))
ax.text(4.25, 11, "卫生间\n2.5m x 2m", ha='center', va='center', fontsize=10)

# 车库：位于左侧最里面的区域
ax.add_patch(patches.Rectangle((0, 8), 3, 4, facecolor=colors['车库'], edgecolor='black', label='车库'))
ax.text(1.5, 10, "车库\n3m x 4m", ha='center', va='center', fontsize=10)

# 绘制大门：位于正面右侧进入，使用双向大门表示
door_x_start = 4 + (4 - 1.8) / 2  # 大门起始x坐标（右半侧中央）
door_y_bottom = 0  # 大门底部y坐标
door_length = 1.8  # 大门长度

# 使用两条粗线表示双向大门
ax.plot([door_x_start, door_x_start + door_length], [door_y_bottom, door_y_bottom],
        color='black', linewidth=4, label='大门')

# # 添加图例
# handles, labels = [], []
# for label, color in colors.items():
#     handles.append(patches.Patch(color=color, label=label))
# ax.legend(handles=handles, loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10, title="功能区")

# 显示坐标轴标签
plt.xlabel("面宽 (米)", fontsize=12)
plt.ylabel("进深 (米)", fontsize=12)

# 显示图形
# plt.tight_layout()
# 显示图形
plt.show()
