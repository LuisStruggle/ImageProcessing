#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/16 21:11
# @Author : ly
# @File   : opencv8.py
import cv2

filename = "resource/face.jpg"

def detect(filename):
    face_cascade = cv2.CascadeClassifier("resource/haarcascade_frontalface_default.xml")

    img = cv2.imread(filename)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("face", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

detect(filename)



