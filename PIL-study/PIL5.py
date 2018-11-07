#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/7 17:08
# @Author : ly
# @File   : PIL5.py
# PIL.ImageDraw 提供简单的 2D 绘图功能. 你可以使用它创建新的图像或修改已有的图像.
import PIL.Image as image
import PIL.ImageDraw as draw

# -------------------------------------------------------------------------------------------
# 绘制线段(0,0)指的是左上角，x指的是宽，y指的事高
im = image.new("RGB", (480, 270), '#333333')
imageDraw = draw.ImageDraw(im)
#
# imageDraw.line((0, 0) + im.size, fill='#FFFFFF')
# imageDraw.line((0, im.size[1], im.size[0], 0), fill='#FFFFFF')
#
# # 绘制离散的点
# imageDraw.point([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50)], fill='#FFFFFF')
#
# im.show()
# -------------------------------------------------------------------------------------------
# 绘制圆弧
# PIL.ImageDraw.Draw.arc 方法可以在给定的矩形选框内绘制一段(内切)圆弧. 绘制起点为 3 点钟位置.
# imageDraw.arc((100, 50, 379, 219), 0, 180, fill="#FFFFFF")
# im.show()

# PIL.ImageDraw.Draw.chord 方法与 PIL.ImageDraw.Draw.arc 类似, 不同的是会填充圆弧.
# imageDraw.chord((100, 50, 379, 219), 0, 180, fill='#FFFFFF')
# im.show()

# PIL.ImageDraw.Draw.ellipse 方法绘制并填充椭圆.
# 在100,50为起点，379，219为终点的矩形框内，画椭圆，并填充
# imageDraw.ellipse((100, 50, 379, 219), fill='#FFFFFF')
# im.show()

# PIL.ImageDraw.Draw.pieslice 方法绘制并填充扇形.
# 绘制起点为3点钟方向围绕起点所画的矩形框的中心，顺时针旋转
# imageDraw.pieslice((100, 50, 379, 219), 0, 90, fill='#FFFFFF')
# im.show()
# -------------------------------------------------------------------------------------------
# 绘制矩形
# imageDraw.rectangle((100, 50, 379, 219), fill='#FFFFFF')
# im.show()

# 绘制多边形
# imageDraw.polygon([(100, 50), (380, 50), (240, 250)], fill='#FFFFFF')
# im.show()
# -------------------------------------------------------------------------------------------
# 绘制文字
import PIL.ImageFont as font
image_font = font.truetype('consola', 14)
# (96, 10), 返回字符串将要占用的像素区域大小
print(imageDraw.textsize('Hello World!', image_font))
imageDraw.text((192, 130), 'Hello World!', '#FFFFFF', image_font)

im.show()
"""
与 draw.text 类似的还有一个 draw.multiline_text 方法, 不多做介绍.
"""






