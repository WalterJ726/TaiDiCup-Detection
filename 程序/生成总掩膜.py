# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from  datetime import datetime
from PIL import Image
import os
import numpy as np
import cv2


def getFileName(path):
    filelist = []
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.jpg':
            print(i)
            filelist.append(i)
    return filelist
dir = 'guassss/'
dir_new = 'yanmo3/'
filelist = getFileName(dir)
start = '000'
for i in range(len(filelist)):
    information = filelist[i].replace('.jpg','').split('_')
    number = information[0]
    if number != start:
        img_back = np.zeros((int(information[1]),int(information[2])),dtype = np.uint8)

    else:
        img_back = cv2.imread(dir_new+number+'.jpg',0)

    img_use = cv2.imread(dir+filelist[i], 0)
    # img_use[img_use<125] = 0
    # img_use[img_use>=125] = 255
    img_use = cv2.resize(img_use, (int(information[11]),int(information[10])), interpolation=cv2.INTER_AREA)
    part = int(information[3])
    xmin = int(information[4])
    xmax = int(information[5])
    ymin = int(information[6])
    ymax = int(information[7])
    if part ==1:
        xmin = int(xmin+int(information[2])/2)
        xmax = int(xmax+int(information[2])/2)
        ymin = int(ymin+int(information[1])/2)
        ymax = int(ymax+int(information[1])/2)
    if part ==2:
        ymin = int(ymin + int(information[1])/2)
        ymax = int(ymax + int(information[1])/2)
    if part ==4:
        xmin = int(xmin + int(information[2])/2)
        xmax = int(xmax + int(information[2])/2)
    heigh_lo = int(ymax) - int(ymin)
    width_lo = int(xmax) - int(xmin)

    if information[8] == 'w':
        a = img_back[ymin:ymax, xmin + int(information[11]) * (int(information[9]) - 1):xmin + int(information[11]) * (int(information[9]))]
        try:
            a[img_use > 125] = img_use[img_use > 125]
        except:
            print('bug')
        img_back[ymin:ymax, xmin + int(information[11]) * (int(information[9]) - 1):xmin + int(information[11]) * (int(information[9]))] =a
    elif information[8] == 'h':

        a =img_back[ymin + int(information[10]) * (int(information[9]) - 1): ymin + int(information[9]) * int(information[10]), xmin:xmax]
        try:
            a[img_use > 125] = img_use[img_use > 125]
        except:
            print('bug')
        img_back[ymin + int(information[10]) * (int(information[9]) - 1): ymin + int(information[9]) * int(information[10]), xmin:xmax] = a
    else:
        if information[9] == '1':
             a = img_back[ymax - int(information[10]):ymax, xmax- int(information[11]):xmax]
             a[img_use > 125] = img_use[img_use > 125]
             img_back[ymax - int(information[10]):ymax, xmax - int(information[11]):xmax] = a
        elif information[9] == '2':
            a = img_back[ymax - int(information[10]):ymax, xmin:xmin + int(information[11])]
            a[img_use > 125] = img_use[img_use > 125]
            img_back[ymax - int(information[10]):ymax, xmin:xmin + int(information[11])] = a
        elif information[9] == '3':
            a = img_back[ymin:ymin + int(information[10]) , xmin:xmin + int(information[11]) ]
            a[img_use > 125] = img_use[img_use > 125]
            img_back[ymin:ymin + int(information[10]), xmin:xmin + int(information[11])] = a
        else:
            a = img_back[ymin:ymin + int(information[10]), xmax - int(information[11]):xmax]
            a[img_use > 125] = img_use[img_use > 125]
            img_back[ymin:ymin + int(information[10]), xmax - int(information[11]):xmax] = a
    cv2.imwrite(dir_new + number + '.jpg', img_back)
    start = number