#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/7 18:26
# @Author : ly
# @File   : PIL6.py.py
# PIL.ImageEnhance 包含一系列的图像增强算法.
import PIL.Image as image
import PIL.ImageEnhance as enhance
im = image.open("resource/jp.jpg")

# -------------------------------------------------------------------------------------------
# 色彩平衡度(PIL.ImageEnhance.Color)
# enhancer = enhance.Color(im)
# # 从灰度图逐渐恢复到原图
# for i in range(11):
#     enhancer.enhance(i / 10.0).show()
# -------------------------------------------------------------------------------------------
# 对比度(PIL.ImageEnhance.Contrast)
# enchancer = enhance.Contrast(im)
# enchancer.enhance(0.5).show()
# enchancer.enhance(0.2).show()
# -------------------------------------------------------------------------------------------
# 亮度(PIL.ImageEnhance.Brightness)
# enchancer = enhance.Brightness(im)
# enchancer.enhance(0.5).show()
# enchancer.enhance(0.2).show()
# -------------------------------------------------------------------------------------------
# 锐化(PIL.ImageEnhance.Sharpness)
enchancer = enhance.Sharpness(im)
# 低于 1 时模糊, 高于 1 时锐化
enchancer.enhance(0.1).show()
enchancer.enhance(2.0).show()



