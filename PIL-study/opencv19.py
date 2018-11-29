#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/21 15:25
# @Author : ly
# @File   : opencv19.py
"""
在opencv中简单实现9，59的神经网络
"""
import cv2
import numpy as np

ann = cv2.ml.ANN_MLP_create()
# 设置网络结构
ann.setLayerSizes(np.array([9, 5, 9], dtype=np.uint8))
# 设置反向传播的方式
ann.setTrainMethod(cv2.ml.ANN_MLP_BACKPROP)

# 设置训练样本及标签(三个参数，samples、layout、responses)
ann.train(np.array([[1.2, 1.3, 1.9, 2.2, 2.3, 2.9, 3.0, 3.2, 3.3]], dtype=np.float32), cv2.ml.ROW_SAMPLE, np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0]], dtype=np.float32))
print(ann.predict(np.array([[1.4, 1.5, 1.2, 2., 2.5, 2.8, 3., 3.1, 3.8]], dtype=np.float32)))
