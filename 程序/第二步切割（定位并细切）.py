# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from  datetime import datetime
from PIL import Image
import os
import numpy as np
import cv2

from Object_detection_image import location
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
dir2 = 'guanfangyanmo/'
dir = 'first_step_cut/'
dir_cut = 'second_step_cut/'
# dir_cut = 'bingge/'
filelist =getFileName(dir)

for name in filelist:
    before = name.replace('.jpg','')
    img = cv2.imread(dir+name)
    objects = location(dir+name)
    # img = cv2.imread(dir2+before.split('_')[0]+'.png',0)
    for object in objects:
        # img = cv2.imread(dir2 + before.split('_')[0] + '.png')
        print(object)
        xmin = object[0]
        ymin = object[1]
        xmax = object[2]
        ymax = object[3]
        height = ymax - ymin
        width = xmax - xmin
        if int(width / height) > 1:
            beishu = int(width / height)
            if beishu > 3:
                beishu = 3
            for diji in range(beishu):
                imgs = img[ymin:ymax, int(xmin + width / (beishu) * diji):xmin + int(width / (beishu) * (diji + 1))]
                height_out,width_out = imgs.shape[:2]
                cv2.imwrite(dir_cut+before+'_'+str(xmin)+'_'+str(xmax)+'_'+str(ymin)+'_'+str(ymax)+'_w_'+str(diji+1)+'_'+str(height_out)+'_'+str(width_out)+'.jpg', imgs)

        elif int(height / width) > 1:
            beishu = int(height / width)
            if beishu > 3:
                beishu = 3
            for diji in range(beishu):
                imgs = img[int(ymin + height / (beishu) * diji):int(ymin + height / (beishu) * (diji + 1)), xmin:xmax]
                height_out,width_out = imgs.shape[:2]
                cv2.imwrite(dir_cut + before + '_' + str(xmin) + '_' + str(xmax) + '_' + str(ymin) + '_' + str(ymax) + '_h_' + str(diji + 1) + '_' + str(height_out)+'_'+str(width_out) + '.jpg', imgs)

        else:
            img1 = img[int(ymin + height / 3):ymax, int(xmin + width / 3):xmax]
            img2 = img[int(ymin + height / 3):ymax, xmin :xmin+int(width / 3*2)]
            img3 = img[ymin:int(ymin + height / 3*2), xmin:int(xmin + width / 3*2)]
            img4 = img[ymin:ymin + int(height / 3*2), xmin + int(width / 3):xmax]
            # img1 = img[ymin:ymax,xmin:xmax]
            height_out,width_out = img1.shape[:2]
            if height_out>250 and width_out>250:

                cv2.imwrite(dir_cut + before + '_' + str(xmin) + '_' + str(xmax) + '_' + str(ymin) + '_' + str(ymax) + '_z_' + str(1) + '_' + str(height_out)+'_'+str(width_out) + '.jpg', img1)
            height_out,width_out = img2.shape[:2]
            if height_out>250 and width_out>250:

                cv2.imwrite(dir_cut + before + '_' + str(xmin) + '_' + str(xmax) + '_' + str(ymin) + '_' + str(ymax) + '_z_' + str(2) + '_' + str(height_out)+'_'+str(width_out) + '.jpg', img2)
            height_out, width_out = img3.shape[:2]
            if height_out>250 and width_out>250:
                cv2.imwrite(dir_cut + before + '_' + str(xmin) + '_' + str(xmax) + '_' + str(ymin) + '_' + str(ymax) + '_z_' + str(3) + '_' + str(height_out)+'_'+str(width_out) + '.jpg', img3)
            height_out,width_out = img4.shape[:2]
            if height_out>250 and width_out>250:
                cv2.imwrite(dir_cut + before + '_' + str(xmin) + '_' + str(xmax) + '_' + str(ymin) + '_' + str(ymax) + '_z_' + str(4) + '_' + str(height_out)+'_'+str(width_out) + '.jpg', img4)
