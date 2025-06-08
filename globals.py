# -*- coding: utf-8 -*-

"""
@Time    : 2025/3/14 19:24
@File    : globals.py
@Author  : zj
@Description: 
"""

VERSION = "v2.1"

FLOOR_1_TITLE = f"房屋一楼布局图 {VERSION}"
FLOOR_1_5_TITLE = f"厨房布局图 {VERSION}"
FLOOR_2_TITLE = f"房屋二楼布局图 {VERSION}"
FLOOR_3_TITLE = f"房屋三楼布局图 {VERSION}"
FLOOR_3_5_TITLE = f"房屋顶楼布局图 {VERSION}"

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

import matplotlib.patches as patches

# 墙壁厚度
wall_thickness = 0.25


# 绘制墙壁
def draw_wall(ax, x, y, width, height, exclude=None, adjacent=None):
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
        ax.add_patch(patches.Rectangle((x, y), wall_thickness, height, facecolor='gray'))
    if ('right' not in exclude) and ('right' not in adjacent):
        ax.add_patch(patches.Rectangle((x + width - wall_thickness, y), wall_thickness, height - wall_thickness,
                                       facecolor='gray'))
    if ('bottom' not in exclude) and ('bottom' not in adjacent):
        ax.add_patch(patches.Rectangle((x, y), width, wall_thickness, facecolor='gray'))
    if ('top' not in exclude) and ('top' not in adjacent):
        ax.add_patch(patches.Rectangle((x, y + height - wall_thickness), width, wall_thickness, facecolor='gray'))
