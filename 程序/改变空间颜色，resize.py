
import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image
import cv2
import os

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
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2,0.8,0])
dir = 'second_step_cut/'
dir_new = 'noguass/'
filelist = getFileName(dir)
for name in filelist:
    img_road = dir+name
        # img = plt.imread(img_road)

    width = 512
    #
    height = 512

    img = Image.open(img_road)
    img = img.resize((height,width), Image.ANTIALIAS)

    img = np.array(img)
    print(img.shape)
    sigma1 = sigma2 = 0.8
    sum = 0
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # gaussian = np.zeros([5, 5])
    # for i in range(5):
    #     for j in range(5):
    #         gaussian[i, j] = math.exp(-1 / 2 * (np.square(i - 3) / np.square(sigma1)  # 生成二维高斯分布矩阵
    #                                             + (np.square(j - 3) / np.square(sigma2)))) / (2 * math.pi * sigma1 * sigma2)
    #         sum = sum + gaussian[i, j]
    #
    # gaussian = gaussian / sum
    #
    # # step1.高斯滤波
    gray = rgb2gray(img)
    #
    # W, H = gray.shape
    # new_gray = np.zeros([W-5 , H-5 ])
    # for i in range(W - 5):
    #     for j in range(H - 5):
    #         new_gray[i, j] = np.sum(gray[i:i+5, j:j + 5] * gaussian)  # 与高斯矩阵卷积实现滤波
    #         # if new_gray[i, j] <100:
    #         #     new_gray[i, j] = 255
    #         # else:
    #         #     new_gray[i, j] = 0

    ROAD = dir_new+name
    cv2.imwrite(ROAD,gray)




# step1.高斯滤波





# a = list(np.array(new_gray.shape))
# grayRgb = np.zeros((a[0],a[1],3))
# grayRgb[:, :, 2] = new_gray/255
# grayRgb[:, :, 0] = new_gray/255
# grayRgb[:, :, 1] = new_gray/255
#
# plt.imshow(grayRgb, cmap="gray")
# plt.show()
# plt.imsave('guss1.jpg',grayRgb)
