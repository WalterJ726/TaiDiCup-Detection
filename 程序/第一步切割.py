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
        if os.path.splitext(i)[1] == '.JPG' or '.jpg':
            print(i)
            filelist.append(i)
    return filelist

def one_to_five(img):
    height, width = img.shape[:2]
    img0 = img
    img1 = img[int(height/2):height,int(width/2):width]
    img2 = img[int(height/2):height,0:int(width/2)]
    img3 = img[0:int(height/2),0:int(width/2)]
    img4 = img[0:int(height/2),int(width/2):width]
    return img0,img1,img2,img3,img4

storage = 'first_step_cut/'
dir = 'JPEGImages/'
filelist = getFileName(dir)
for image in filelist:
    img = cv2.imread(dir+image)
    height,width= img.shape[:2]
    img0, img1, img2, img3, img4 = one_to_five(img)
    number = image.replace('.JPG','')
    for i in range(5):
        img = eval('img'+str(i))
        cv2.imwrite(storage+number+'_'+str(height)+'_'+str(width)+'_'+str(i)+'.jpg',img)



