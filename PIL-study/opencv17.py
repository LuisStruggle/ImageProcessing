#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/20 15:03
# @Author : ly
# @File   : opencv17.py
"""
背景分割是一种非常有效的技术，但并不是进行视频中目标跟踪唯一可用的技术。均值漂移（Meanshift）是一种目标跟踪算法，
该算法寻找概率函数离散样本的最大密度（例如，感兴趣的图像区域），并且重新计算在下一帧中的最大密度，该算法给出了目标的移动方向。

重复进行该计算，直到与原始中心匹配，或者在连续迭代计算后中心保持不变。这一最后匹配称为收敛。
"""

"""
calcHist和calcBackProject，它们与彩色直方图有关。
calcHist函数用来计算图像的彩色直方图。所谓的彩色直方图是指图像的颜色分布。它的x轴是色彩值，有轴是相应色彩值的像素数量。

它所表述的彩色直方图，每列的取值范围在0到180之间。

calcBackProject函数在均值漂移算法中发挥着至关重要的作用。之所以叫作直方图反向投影是因为它可得到直方图并将其投影到一幅图像上，
其结果是概率，即每个像素属于起初纳福生成直方图的图像的概率。
"""
import numpy as np
import cv2
cap = cv2.VideoCapture("resource/video.mp4")
ret, frame = cap.read()

# 标记ROI的区域
r, h, c, w = 130, 200, 500, 300
track_window = (c, r, w, h)

# 提取ROI，并将其转换为HSV色彩空间
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# 创建一个包含具有hsv值的ROI所有像素的掩码，hsv值在上界与下届之间
mask = cv2.inRange(hsv_roi, np.array((100., 30., 32.)), np.array((180., 120., 255.)))

# 计算ROI的直方图
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
# 在计算直方图后，相应的值被归一化到0-255范围内
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# 均值漂移在达到收敛之前会迭代多次，但不能保证一定收敛。因此，opencv允许指定停止条件，这是一种指定均值漂移终止一系列计算行为的方式
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
"""
这里的停止条件为：均值漂移迭代10次后或者中心移动至少1个像素时，均值漂移就停止计算中心移动。
第一个标志（EPS或CRITERIA_COUNT）表示将使用这两个条件的任意一个
"""
# 设置无线循环来从视频中获取当前帧，然以后开始处理，首先要切换到hsv色彩空间
while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 执行直方图反向投影(dst中的每个像素以概率的形式表示)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # 最后，计算窗口的新坐标，绘图
        x, y, w, h = track_window
        img2 = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
        cv2.imshow("img2", img2)

        if cv2.waitKey(3000) & 0xff == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
