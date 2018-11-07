#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/7 14:27
# @Author : ly
# @File   : PIL1.py
import PIL.Image as pil
import PIL
im = pil.open("resource/jp.jpg")
# im.show()

# PIL 在保存图像时, 会自动根据文件后缀名进行格式转化。
# im.save("resource/jp.png")

# thumbnail 方法会将图像转换为缩略图. 此方法修改图像为本身的缩略图版本, 缩略图不大于给定大小。
# im.thumbnail((160, 120))
# im.show()

# 图像的属性
# print(im.format, im.size, im.mode)

# 裁剪, 粘贴与合并图像
# 裁剪
# box = (100, 100, 400, 400)
# region = im.crop(box)
# region.show()

# 旋转裁剪的图像, 并粘贴回原位置
# region = region.transpose(pil.ROTATE_180)
# im.paste(region, box)
# im.show()
"""
当将子图像粘贴至父原图时, 子图像的大小必须与给定区域完全匹配. 此外, 该区域不能扩展到父图像之外. 但是, 子图像和父图像的模式(mode)不需要匹配. 在粘贴之前, 子图像会自动转换至父图像的模式.
"""

# 分离与合并通道
# r, g, b = im.split()
# im = pil.merge('RGB',(b, g, r))
# im.show()

# 简单几何变换
# out = im.resize((128, 128))  # 重置图像尺寸
# out.show()
# out = im.rotate(45)  # degrees counter-clockwise（逆时针旋转图像）
# out.show()
"""
resize 与 rotate 方法会返回一个新的 Image 对象.
"""

# 模式转换
# out = im.convert(mode='L')
# out.show()
"""
可选的模式包括:

1 (1-bit pixels, black and white, stored with one pixel per byte)
L (8-bit pixels, black and white)
P (8-bit pixels, mapped to any other mode using a color palette)
RGB (3x8-bit pixels, true color)
RGBA (4x8-bit pixels, true color with transparency mask)
CMYK (4x8-bit pixels, color separation)
YCbCr (3x8-bit pixels, color video format) Note that this refers to the JPEG, and not the ITU-R BT.2020, standard
LAB (3x8-bit pixels, the L*a*b color space)
HSV (3x8-bit pixels, Hue, Saturation, Value color space)
I (32-bit signed integer pixels)
F (32-bit floating point pixels)
"""

# 滤镜
# import PIL.ImageFilter as filter
# out = im.filter(filter.BLUR)
# out.show()
"""
可选的滤镜包括:

BLUR
CONTOUR
DETAIL
EDGE_ENHANCE
EDGE_ENHANCE_MORE
EMBOSS
FIND_EDGES
SMOOTH
SMOOTH_MORE
SHARPEN
"""

# 像素操作（使用 point() 方法对图像的每一个像素做相应操作.）
# 反色: 所有像素点 i 会被 255 - i 替换
# im = im.point(lambda i:255-i)
# im.show()

# 图像增强
# import PIL.ImageEnhance as enhance
# # Contrast对比度增强
# enh = enhance.Contrast(im)
# enh.enhance(1.3).show()

# 读取 GIF 动画
# gim = pil.open('resource/gi.gif')
# gim.seek(45)
# gim.show()
# # 使用迭代器读取
# import PIL.ImageSequence as sequence
# for frame in sequence.Iterator(gim):
#     print(frame)

# 关于读取图像的更多说明(大多数时候, 通过传入文件名至 open() 函数读取一张图像. 但同时你也可以使用其他方式读取图像:)
# import io
# # import numpy as np
# # # 从 fp 中读取
# # with open('resource/jp.jpg', 'rb') as fp:
# #     imfp = pil.open(fp)
# #     imfp.show()
# # # 从矩阵中读取
# # imarr = pil.fromarray(255*np.ones((100,100)))
# # imarr.show()

# 采样器
"""
PIL 支持如下 6 种采样器, 均位于 PIL.Image 包内.

NEAREST
BOX
BILINEAR
HAMMING
BICUBIC
LANCZOS
"""
# print(pil.LANCZOS)

# 显示图像(在调试过程中, 使用 im.show() 可以方便的展示图像, 但同时也可以借助一些其他方式展示图像, 如 matplotlib 和 opencv)
# import matplotlib.pyplot as plt
# plt.imshow(im)
# plt.axis('off')
# plt.show()

import cv2
import scipy.misc
cv2.imshow("im", scipy.misc.fromimage(im))
cv2.waitKey(0)
cv2.destroyAllWindows()







