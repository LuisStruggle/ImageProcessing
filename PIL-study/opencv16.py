#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/20 13:43
# @Author : ly
# @File   : opencv16.py
"""
背景分割器：KNN、MOG2、GMG。opencv提供了一个称为BackgroundSubtractor的类，在分割前景和背景时很方便。

BackgroundSubtractor类的另一个基本特征（也是相当惊人的特征）是它可以计算阴影。这对于精确读取视频帧绝对至关重要的。
通过检测阴影，可排除检测图像的阴影区域（采用阈值方式），从而能关注实际特征。
"""

"""
注意阴影检测并非绝对完美，但它有助于将目标轮廓按原始形状进行还原。
"""
import numpy as np
import cv2

bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)

camera = cv2.VideoCapture("resource/video.mp4")

while True:
    ret, frame = camera.read()
    # 获取前景掩码
    fgmask = bs.apply(frame)
    fgmask_copy = fgmask
    # 设定阈值：前景掩码含有前景的白色值以及阴影的灰色值。因此，在阈值化图像中，将非纯白色（244-255）的所有像素都设为0，而不是1
    th = cv2.threshold(fgmask_copy, 244, 255, cv2.THRESH_BINARY)[1]

    # 识别目标
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
    # 检测轮廓
    image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 绘图
    for c in contours:
        if cv2.contourArea(c) > 1600:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("mog", fgmask)
    cv2.imshow("thresh", th)
    cv2.imshow("detection", frame)
    if cv2.waitKey(30) & 0xff == 27:
        break

camera.release()
cv2.destroyAllWindows()

