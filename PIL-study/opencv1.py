#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/12 13:59
# @Author : ly
# @File   : opencv1.py
import numpy as np
import cv2
import os
# -------------------------------------------------------------------------------------------
# 每一个像素由一个8位整数来表示，现利用cv2.cvtColor函数将该图像转换成Blue-green-red
# img = np.zeros((3, 3), dtype=np.uint8)
# img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# cv2.imwrite("resource/opencv1.jpg", img)
# -------------------------------------------------------------------------------------------
# 读取一个图像，并将其保存为灰度图
# img = cv2.imread("resource/jp.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imwrite("resource/opencv2.jpg", img)
# -------------------------------------------------------------------------------------------
# 将含有随机字的bytearray转换为灰度图像和bgr图像
# randomByteArray = bytearray(os.urandom(120000))
# print(randomByteArray)
# flatNumpyArray = np.array(randomByteArray)
# print(flatNumpyArray)


# grayImage = flatNumpyArray.reshape(300, 400)
# cv2.imwrite("resource/opencv3.jpg", grayImage)

# bgrImage = flatNumpyArray.reshape(100, 400, 3)
# cv2.imwrite("resource/opencv4.jpg", bgrImage)
# -------------------------------------------------------------------------------------------
# 修改特定位置及通道上的值，三种方式
# 第一种：
# img = cv2.imread("resource/jp.jpg")
# img[0, 0] = [255, 255, 255]  # 改变0,0位置的三通道为255
# print(img)
# 第二种：
# img = cv2.imread("resource/jp.jpg")
# print(img.item(150, 120, 0))  # 打印出150*120位置，第0个通道的像素值
# 第三种：
# img.itemset((150, 120, 0), 255)  # 修改图像对应位置的通道的值
# print(img.item(150, 120, 0))  # 打印出150*120位置，第0个通道的像素值
# -------------------------------------------------------------------------------------------
# 将图像的一个感兴趣区域移动到另一个地方
# img = cv2.imread("resource/jp.jpg")
# roi = img[0:100, 0:100]
# img[100:200, 100:200] = roi
# cv2.imwrite("resource/opencv5.jpg", img)
# -------------------------------------------------------------------------------------------
# 视频读写操作
# videoCapture = cv2.VideoCapture("resource/video.mp4")
# # 复制一份该视频
# fps = videoCapture.get(cv2.CAP_PROP_FPS)  # 获取原视频的帧速度
# size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # 获取原视频的帧大小
#
# videoWriter = cv2.VideoWriter("resource/copy.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)  # 创建一个video写对象，其中的第二个参数是视频的编解码方式
#
# success, frame = videoCapture.read()  # 读取video的一帧画面
# while success:
#     videoWriter.write(frame)
#     success, frame = videoCapture.read()
# -------------------------------------------------------------------------------------------
# 图像的显示操作
# img = cv2.imread("resource/jp.jpg")
# cv2.imshow("my picture", img)
# cv2.waitKey()
# cv2.destroyAllWindows()  # 释放由opencv打开的所有窗口
# -------------------------------------------------------------------------------------------
# 实现视频的画面帧的显示
clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

videoCapture = cv2.VideoCapture("resource/video.mp4")
cv2.namedWindow("MyWindow")  # 用窗口名，创建弹出窗口
cv2.setMouseCallback("MyWindow", onMouse)

success, frame = videoCapture.read()  # 读取video的一帧画面
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow("MyWindow", frame)
    success, frame = videoCapture.read()  # 读取video的一帧画面

cv2.destroyWindow("MyWindow")
videoCapture.release()



