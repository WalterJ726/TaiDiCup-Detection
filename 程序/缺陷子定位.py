# -*- coding: UTF-8 -*-
from quexian_detection_image import find_quexian
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from datetime import datetime
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
dir = 'test_quexian/'
dir_cut = 'model5_6/'
# dir_cut = 'bingge/'
filelist =getFileName(dir)

for name in filelist:
    information = name.replace('_predict.jpg', '').split('_')
    number = information[0]
    yuantu = cv2.imread('JPEGImages/'+number+'.jpg')

    objects = find_quexian(dir+name,0.5)
    if objects!=[]:
        print(name)
        quexian_posi = []
        # img = cv2.imread(dir2+before.split('_')[0]+'.png',0)
        for object in objects:
            # img = cv2.imread(dir2 + before.split('_')[0] + '.png')
            print('obj',object)
            xmin_yanmo = int(object[0]/256*int(information[11]))
            ymin_yanmo = int(object[1]/256*int(information[10]))
            xmax_yanmo = int(object[2]/256*int(information[11]))
            ymax_yanmo = int(object[3]/256*int(information[10]))

            information = name.replace('.jpg', '').split('_')
            number = information[0]



            part = int(information[3])
            xmin = int(information[4])
            xmax = int(information[5])
            ymin = int(information[6])
            ymax = int(information[7])
            if part == 1:
                xmin = int(xmin + int(information[2]) / 2)
                xmax = int(xmax + int(information[2]) / 2)
                ymin = int(ymin + int(information[1]) / 2)
                ymax = int(ymax + int(information[1]) / 2)
            if part == 2:
                ymin = int(ymin + int(information[1]) / 2)
                ymax = int(ymax + int(information[1]) / 2)
            if part == 4:
                xmin = int(xmin + int(information[2]) / 2)
                xmax = int(xmax + int(information[2]) / 2)
            heigh_lo = int(ymax) - int(ymin)
            width_lo = int(xmax) - int(xmin)

            if information[8] == 'w':
                    xmin_final = xmin + int(information[11]) * (int(information[9]) - 1)+ xmin_yanmo
                    xmax_final = xmin + int(information[11]) * (int(information[9]) - 1)+ xmax_yanmo
                    ymin_final = ymin_yanmo + ymin
                    ymax_final = ymax_yanmo + ymin
            elif information[8] == 'h':
                    ymin_final = ymin + int(information[10]) * (int(information[9]) - 1) + ymin_yanmo
                    ymax_final = ymin + int(information[10]) * (int(information[9]) - 1) + ymax_yanmo
                    xmin_final = xmin_yanmo + xmin
                    xmax_final = xmax_yanmo + xmin

            else:
                if information[9] == '1':
                    ymin_final = ymax - int(information[10])+ymin_yanmo
                    ymax_final = ymax - int(information[10])+ymax_yanmo
                    xmin_final = xmax - int(information[11])+xmin_yanmo
                    xmax_final = xmax - int(information[11])+xmax_yanmo

                elif information[9] == '2':
                    ymin_final = ymax - int(information[10])+ymin_yanmo
                    ymax_final = ymax - int(information[10]) + ymax_yanmo
                    xmin_final = xmin+xmin_yanmo
                    xmax_final = xmin+xmax_yanmo

                elif information[9] == '3':
                    ymin_final = ymin + ymin_yanmo
                    ymax_final = ymin + ymax_yanmo
                    xmin_final = xmin+xmin_yanmo
                    xmax_final = xmin+xmax_yanmo
                else:
                    ymin_final = ymin + ymin_yanmo
                    ymax_final = ymin + ymax_yanmo
                    xmin_final = xmax - int(information[11]) + xmin_yanmo
                    xmax_final = xmax - int(information[11]) + xmax_yanmo

            quexian_posi.append([xmin_final,ymin_final,xmax_final,ymax_final])

        for i in quexian_posi:
            cv2.rectangle(yuantu, (i[0],i[3]), (i[2], i[1]), (0, 0, 255), 10);
        cv2.imwrite(dir_cut+number+'.jpg',yuantu)