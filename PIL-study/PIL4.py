#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/7 16:58
# @Author : ly
# @File   : PIL4.py
# PIL.ImageColor 包含两个将字符串转换为颜色值的函数 getrgb() 与 getcolor().
import PIL.ImageColor as color

# getrgb(color) 返回 (red, green, blue[, alpha])
print(color.getrgb('#FFCC33'))

print(color.getrgb('rgb(255, 204, 51)'))

print(color.getrgb('rgb(100%,0%,0%)'))

print(color.getrgb('rgb(70%,0%,0%)'))

print(color.getrgb('hsl(0,100%,50%)'))

# 颜色名称作为参数传入, 允许的名称定义在 PIL.ImageColor.colormap 中
print(color.getrgb('pink'))

# getcolor(color, mode) 返回 (graylevel [, alpha]) 或 (red, green, blue[, alpha])
print(color.getcolor("#FFCC33", "L"))

print(color.getcolor("#FFCC33", "RGB"))

