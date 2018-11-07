#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/7 15:45
# @Author : ly
# @File   : PIL2.py
# 合并图像
"""
合并图像可以使用 PIL.Image.alpha_composite, PIL.Image.blend 和 PIL.Image.composite, 这里简单演示下第一种方式:
"""
import PIL.Image as image
import numpy as np

im = image.open("resource/jp.jpg")
# # im = im.convert("RGBA")
# #
# # mask_mat = np.zeros((im.size[1], im.size[0], 4), dtype=np.uint8)
# # mask_mat[:, :, 0] = np.ones((im.size[1], im.size[0]), dtype=np.uint8) * 0xFF
# # mask_mat[:, :, 1] = np.ones((im.size[1], im.size[0]), dtype=np.uint8) * 0xCC
# # mask_mat[:, :, 2] = np.ones((im.size[1], im.size[0]), dtype=np.uint8) * 0x33
# # mask_mat[:, :, 3] = np.ones((im.size[1], im.size[0]), dtype=np.uint8) * 80
# # mask = image.fromarray(mask_mat)
# #
# # # 为原图像添加 (0xFF, 0xCC, 0x33, 80) 的蒙版
# # im = image.alpha_composite(im, mask)
# # im.show()
# -------------------------------------------------------------------------------------------
# 如果你只期望获得一个通道的 Image, 则可以使用 getchannel()
# r = im.getchannel('R')
# r.show()
# 获取图像像素数据
# mat = np.array(im.getdata())
# print(mat[0])  # (84, 70, 59)
# # 获取图像一个通道的像素数据
# mat = np.array(im.getdata(0))
# print(mat.shape) # 84
# -------------------------------------------------------------------------------------------
# 创建新的图像
# new_im = image.new('RGB', (480, 270), color=(0xFF, 0xCC, 0x33))
# new_im.show()
# -------------------------------------------------------------------------------------------
# 获取与更新像素点（使用两个方法: getpixel 与 putpixel.）
# 获取其中一个像素点
# print(im.getpixel((40, 40)))  # (87, 84, 77)
# 更新其中一个像素点
# im.putpixel((40, 40), (0, 0, 0))
# # im.show()
# -------------------------------------------------------------------------------------------
# 直方图
# import matplotlib.pyplot as plt
#
# ax = plt.subplot()
# ax.bar(np.arange(0, 256), im.getchannel('R').histogram())
# plt.show()
# -------------------------------------------------------------------------------------------
# 应用滤波器


