#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/7 16:37
# @Author : ly
# @File   : PIL3.py
# PIL.ImageChops 包含一系列的图像算术操作.
import PIL.Image as image
import PIL.ImageChops as chops
# -------------------------------------------------------------------------------------------
# 加法
im1 = image.new('RGB', (480, 270), (0, 255, 0))
# im1.show()
im2 = image.new('RGB', (480, 270), (255, 0, 0))
# im2.show()
# # 计算公式，防止越界255：out = ((image1 + image2) / scale + offset)
# im = chops.add(im1, im2)
# im.show()
#
# # 计算公式，防止越界255：out = ((image1 + image2) % MAX)
# im = chops.add_modulo(im1, im2)
# im.show()
# -------------------------------------------------------------------------------------------
# 减法
# # 计算公式，防止越界255：out = ((image1 - image2) / scale + offset)
# im = chops.subtract(im1, im2)
# im.show()
#
# # 计算公式，防止越界255：out = ((image1 - image2) % MAX)
# im = chops.subtract_modulo(im1, im2)
# im.show()
# -------------------------------------------------------------------------------------------
# 乘法
# # out = image1 * image2 / MAX
# im = chops.multiply(im1, im2)
# im.show()
# -------------------------------------------------------------------------------------------
# 最大值
# # out = max(image1, image2)
# im = chops.lighter(im1, im2)
# im.show()
# -------------------------------------------------------------------------------------------
# 最小值
# # out = min(image1, image2)
# im = chops.darker(im1, im2)
# im.show()
# -------------------------------------------------------------------------------------------
# 差异
# # out = abs(image1 - image2)
# im = chops.difference(im1, im2)
# im.show()
# -------------------------------------------------------------------------------------------
# 反色
# # out = MAX - image
# im = chops.invert(im1)
# im = chops.invert(im2)
# im.show()
# -------------------------------------------------------------------------------------------
# 逻辑操作
# out = ((image1 and image2) % MAX)
im = chops.logical_and(im1.convert("1"), im2.convert("1"))
im.show()

# out = ((image1 or image2) % MAX)
im = chops.logical_or(im1.convert("1"), im2.convert("1"))
im.show()
"""
逻辑操作的参数图像模式必须是 1.
"""


