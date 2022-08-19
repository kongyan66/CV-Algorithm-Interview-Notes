# 题目：通过双线性插值实现对图像的resize

# 实现  代码还是有些问题
import numpy as np
import cv2
import math 

def bi_linear(src, dst, target_size):
    pic = cv2.imread(src)
    th, tw = target_size[0], target_size[1]
    scale_x, scale_y = th / pic.shape[0], tw / pic.shape[1]
    emptyImage = np.zeros(target_size, np.uint8)

    for c in range(3):
        for i in range(th):
            for j in range(tw):
                # 1.求新图该点在原图的位置坐标，可以用等比法
                corr_x = (i + 0.5) / scale_x - 0.5 
                corr_y = (j + 0.5) / scale_y - 0.5
                
                # 2.求原图中相邻四个点的坐标
                point1 = (math.floor(corr_x), math.floor(corr_y)) 
                point2 = (point1[0], point1[1] + 1)
                point3 = (point1[0] + 1, point1[1])
                point4 = (point1[0] + 1, point1[1] + 1)

                a, b = corr_x - point1[0], corr_y - point1[1]
                emptyImage[i, j, c] = int((1 - a) * (1 - b) * point1 + a * (1 - b) * point3 + (1 - a) * b * point2 + a * b * point4)

    cv2.imwrite(dst, emptyImage)

def main():
    src = 'test.png'
    dst = 'new_1.png'
    target_size = (600, 600, 3)     # 变换后的图像大小

    bi_linear(src, dst, target_size)   

if __name__ == '__main__':
    main()

