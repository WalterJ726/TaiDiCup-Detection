import cv2
import numpy as np



def draw_contours(img, cnts):  # conts = contours
    img = np.copy(img)
    img = cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
    return img


def draw_min_rect_circle(img, cnts):  # conts = contours  你可以打印出contours出来看看坐标
    img = np.copy(img)
    height,width =img.shape[:2]
    img2 = np.zeros((height,width))
    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        print(x,y,w,h)
        if (w/h>1.3 or h/w>1.5) and (h>100 or w>100):
            img2[y:y+h,x:x+w] = img[y:y+h,x:x+w]
            cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)  # blue  正常的蓝色框
        # if w*h<=1000:
        #     print(w,h)
        #     img[y:y+h,x:x+w] = [0,0,0]
        # min_rect = cv2.minAreaRect(cnt)  # min_area_rectangle
        # print(min_rect)
        # min_rect = np.int0(cv2.boxPoints(min_rect))
        # print(min_rect)
        # cv2.drawContours(img, [min_rect], 0, (0, 255, 0), 2)  # green 最小的框
        # (x, y), radius = cv2.minEnclosingCircle(cnt)
        # center, radius = (int(x), int(y)), int(radius)  # center and radius of minimum enclosing circle
        # img = cv2.circle(img, center, radius, (0, 0, 255), 2)  # red  圆圈
    return img2

#021
image = cv2.imread('yanmo_1/021.jpg',0)
thresh = cv2.Canny(image, 128, 256)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  ## contours是返回坐标
img = draw_min_rect_circle(image, contours)
cv2.imwrite('x1.jpg', img)

