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

# 添加标题和网格
plt.title("房屋二楼布局图", fontsize=16, fontweight='bold')
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# 定义颜色（调整部分颜色以增强对比度）
colors = {
    '客厅': '#AED6F1',  # 浅蓝色
    '主卧': '#F9E79F',  # 柠檬黄
    '次卧1': '#ABEBC6',  # 浅绿色
    '次卧2': '#D7BDE2',  # 浅紫色
    '卫生间': '#EC7063',  # 草莓红
    '楼梯': '#F4D03F',  # 明亮黄色
    '走廊': '#EBF5FB',  # 浅灰蓝
    '楼梯平台': '#F39C12',  # 橙色
}

# 绘制各个区域
# 客厅（左下角）
ax.add_patch(patches.Rectangle((0, 0), 4, 6.5, facecolor=colors['客厅'], edgecolor='black', linewidth=1.5))
ax.text(2, 3.25, "客厅\n4m x 6.5m", ha='center', va='center', fontsize=10, fontweight='bold')

# 主卧（右下角）
ax.add_patch(patches.Rectangle((4, 0), 4, 4.5, facecolor=colors['主卧'], edgecolor='black', linewidth=1.5))
ax.text(6, 2.25, "主卧\n4m x 4.5m", ha='center', va='center', fontsize=10, fontweight='bold')

# 卫生间（主卧上方）
ax.add_patch(patches.Rectangle((4, 4.5), 4, 2, facecolor=colors['卫生间'], edgecolor='black', linewidth=1.5))
ax.text(6, 5.5, "卫生间\n4m x 2m", ha='center', va='center', fontsize=10, fontweight='bold')

# 楼梯平台（调整位置和尺寸）
ax.add_patch(patches.Rectangle((5, 6.5), 3, 1.5, facecolor=colors['楼梯平台'], edgecolor='black', linewidth=1.5))
ax.text(6.5, 7.25, "楼梯平台\n3m x 1.5m", ha='center', va='center', fontsize=10, fontweight='bold')

# 走廊（调整为整体区域）
ax.add_patch(patches.Rectangle((0, 6.5), 5, 1.5, facecolor=colors['走廊'], edgecolor='black', linewidth=1.5))
ax.text(2.5, 7.25, "走廊\n5m x 1.5m", ha='center', va='center', fontsize=10, fontweight='bold')

# 楼梯区域（调整位置和尺寸）
ax.add_patch(patches.Rectangle((5.5, 8), 2.5, 4, facecolor=colors['楼梯'], edgecolor='black', linewidth=1.5))
ax.text(6.75, 10, "楼梯\n2.5m x 4m", ha='center', va='center', fontsize=10, fontweight='bold')

# 次卧1（次卧2左侧）
ax.add_patch(patches.Rectangle((3, 8), 2.5, 4, facecolor=colors['次卧1'], edgecolor='black', linewidth=1.5))
ax.text(4.25, 10, "次卧1\n2.5m x 4m", ha='center', va='center', fontsize=10, fontweight='bold')

# 次卧2（楼梯左侧）
ax.add_patch(patches.Rectangle((0, 8), 3, 4, facecolor=colors['次卧2'], edgecolor='black', linewidth=1.5))
ax.text(1.5, 10, "次卧2\n3m x 4m", ha='center', va='center', fontsize=10, fontweight='bold')

# 绘制进户门（调整位置和长度）
door_x = 4 + 1  # 进户门的x坐标
door_y_bottom = 6.5 + (1.5 - 0.95) / 2  # 进户门底部y坐标
door_length = 0.95  # 进户门长度

ax.plot([door_x, door_x], [door_y_bottom, door_y_bottom + door_length],
        color='black', linewidth=4, label='进户门', solid_capstyle='round')

# 绘制次卧2门（调整位置和长度）
door_x = 3 - 1 + (1 - 0.8) / 2  # 次卧2门的x坐标
door_y_bottom = 8  # 次卧2门底部y坐标
door_length = 0.8  # 次卧2门长度

ax.plot([door_x, door_x + door_length], [door_y_bottom, door_y_bottom],
        color='black', linewidth=4, label='次卧2门', solid_capstyle='round')

# 绘制次卧1门（调整位置和长度）
door_x = 3 + (1 - 0.8) / 2  # 次卧1门的x坐标
door_y_bottom = 8  # 次卧1门底部y坐标
door_length = 0.8  # 次卧1门长度

ax.plot([door_x, door_x + door_length], [door_y_bottom, door_y_bottom],
        color='black', linewidth=4, label='次卧1门', solid_capstyle='round')

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
plt.show()
