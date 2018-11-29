#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/19 16:22
# @Author : ly
# @File   : opencv15.py
"""
词袋（BOW）的概念最初并不是针对计算机视觉的，但计算机视觉会使用该概念的升级版本。
BOW用来在一系列文档中计算每个词出现的次数，然后，用这些次数构成向量来重新表示文档。

BOW方法的实现步骤：
1，去一个样本数据集
2，对数据集中的每幅图像取描述符（采用SIFT、SURF等方法）
3，将每一个描述符都添加到BOW训练器中
4，将描述符聚类到K簇中（聚类的中心就是视觉单词）
"""
# 汽车检测
import cv2
import numpy as np
from os.path import join

datapath = "resource/CarData/TrainImages"

def path(cls, i):
    return "%s/%s%d.pgm" % (datapath, cls, i+1)

pos, neg = "pos-", "neg-"

# 提取关键点
detect = cv2.xfeatures2d.SIFT_create()
# 提取特征
extract = cv2.xfeatures2d.SIFT_create()

# 创建特征匹配算法
flann_params = dict(algorithm=1, trees=5)
flann = cv2.FlannBasedMatcher(flann_params, {})

# 创建BOW训练器，并为BOW指定簇数为40
bow_kmeans_trainer = cv2.BOWKMeansTrainer(40)
# 初始化BOW提取器。视觉词汇将作为BOW类的输入，在测试图像中会检测这些视觉词汇。
extract_bow = cv2.BOWImgDescriptorExtractor(extract, flann)

# 从图像中提取SIFT图像特征
def extract_sift(fn):
    im = cv2.imread(fn, 0)
    return extract.compute(im, detect.detect(im))[1]

# 每个类都从数据集中读取八张图像（8个正样本，8个负样本）
for i in range(8):
    bow_kmeans_trainer.add(extract_sift(path(pos, i)))
    bow_kmeans_trainer.add(extract_sift(path(neg, i)))

# 要创建视觉单词词汇需要调用训练器上的cluster()函数，该函数执行k-means分类并返回词汇。
voc = bow_kmeans_trainer.cluster()
# 将为BOWImgDescriptorExtractor指定返回的词汇，以便他能从测试图像中提取描述符。
extract_bow.setVocabulary(voc)

# 返回基于BOW的描述符提取器计算得到的描述符
def bow_features(fn):
    im = cv2.imread(fn, 0)
    return extract_bow.compute(im, detect.detect(im))

# 创建两个数组，分别对应训练数据和标签，并用BOWImgDescriptorExtractor产生的描述符填充他们
traindata, trainlabels = [], []
for i in range(20):
    traindata.extend(bow_features(path(pos, i)))
    trainlabels.append(1)
    traindata.extend(bow_features(path(neg, i)))
    trainlabels.append(-1)

# 创建一个SVM实例
svm = cv2.ml.SVM_create()
# 通过将训练数据和标签放到Numpy数组中来进行训练
svm.train(np.array(traindata), cv2.ml.ROW_SAMPLE, np.array(trainlabels))

# 所有这些设置都是用于训练好的SVM，剩下要做的就是给SVM一些样本图像
def predict(fn):
    f = bow_features(fn)
    p = svm.predict(f)
    print(fn, "\t", p[1][0][0])
    return p

car, notcar = "resource/car.jpg", "resource/jp.jpg"
car_img = cv2.imread(car)
notcar_img = cv2.imread(notcar)

# 将图像传递给训练好的SVM
car_predict = predict(car)  # 希望结果是1.0
not_car_predict = predict(notcar)  # 希望结果-1.0

# 可视化结果
font = cv2.FONT_HERSHEY_SIMPLEX

if car_predict[1][0][0] == 1.0:
    cv2.putText(car_img, "Car Detected", (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

if not_car_predict[1][0][0] == -1.0:
    cv2.putText(notcar_img, 'Car Not Detected', (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("BOW + SVM Success", car_img)
cv2.imshow("BOW + SVM Failure", notcar_img)
cv2.waitKey()
cv2.destroyAllWindows()





