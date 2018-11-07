#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/7 18:47
# @Author : ly
# @File   : PIL7.py
# PIL.ImageOps 包含一些预定义的图像处理操作, 大多数只工作于 L 和 RGB 模式下.
import PIL.Image as image
import PIL.ImageOps as ops
im = image.open("resource/jp.jpg")

# -------------------------------------------------------------------------------------------
# 自动调整对比度(im = PIL.ImageOps.autocontrast(image, cutoff=0, ignore=None))
# im = ops.autocontrast(im, cutoff=0.5)
# im.show()
"""
该函数计算图像的直方图, 移除最大和最小的 cutoff 百分比像素, 并将像素范围拉伸到 0 - 255.
"""
# -------------------------------------------------------------------------------------------
# 灰度图着色(im = PIL.ImageOps.colorize(image, black, white)))
# im = ops.colorize(im.convert("L"), (-200, -150, -100), (1000, 1500, 2000))
# im.show()
"""
着色一幅灰度图. 参数中的 black 和 white 需要为 RGB 颜色.
"""
# -------------------------------------------------------------------------------------------
# 移除或添加指定像素的边框(im = PIL.ImageOps.colorize(image, black, white)))
# 移除边框(im = PIL.ImageOps.crop(image, border=0))
# im = ops.crop(im, border=100)
# im.show()
# 添加边框(im = PIL.ImageOps.expand(image, border=0, fill=0))
# im = ops.expand(im, border=100, fill='red')
# im.show()
"""
移除图像上下左右 border 像素.
"""
# -------------------------------------------------------------------------------------------
# 直方图均衡化(im = PIL.ImageOps.equalize(image, mask=None))
# im = ops.equalize(im)
# im.show()
# -------------------------------------------------------------------------------------------
# 翻转图像
# 上下翻转(im =  PIL.ImageOps.flip(image))
# im = ops.flip(im)
# # im.show()
# 左右翻转(im = PIL.ImageIps.mirror(image))
# im = ops.mirror(im)
# im.show()
# -------------------------------------------------------------------------------------------
# 反色(im = PIL.ImageOps.invert(image))
# im = ops.invert(im)
# im.show()
# -------------------------------------------------------------------------------------------
# 降低颜色位数(im = PIL.ImageOps.posterize(image, bits))
im = ops.posterize(im, bits=2)
im.show()
"""
bits 为每个通道保留的颜色位数, 范围 (1-8).
"""

