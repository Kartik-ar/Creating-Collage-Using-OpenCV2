#!/usr/bin/env python
# coding: utf-8
import cv2
import numpy as np

# Loading Image
pic1 = cv2.imread('pic2')
pic2 = cv2.imread('pic3')

# Creating plain image to concate in pic1
exl = np.zeros((25,225,3), np.uint8)
n = np.concatenate((exl,pic2,exl),axis=0)
collage = np.concatenate((pic1,n),axis=1)

# Styling Collage
cv2.line(collage,(200,0),(200,300),(161,22,171),5)
cv2.line(collage,(180,0),(180,300),(161,22,171),5)
a = 0
while True:
    if a >= 300:
        break
    else:
        cv2.line(collage,(180,0+a),(200,20+a),(161,22,171),2)
        cv2.line(collage,(200,0+a),(180,20+a),(161,22,171),2)
        a += 20
for i in range(0,400,20):
    cv2.circle(collage,(10+i,280),10,(161,22,171),1)
    cv2.circle(collage,(10+i,-5),10,(161,22,171),1)
    cv2.circle(collage,(10+i,280),13,(161,22,171),2)
    cv2.circle(collage,(10+i,-5),13,(161,22,171),2)
# Resizing collage
width = int(collage.shape[1] * 500/100) 
height = int(collage.shape[0] * 500/100)  
dim = (width, height)  
# resize image  
collage_resized = cv2.resize(collage, dim, interpolation=cv2.INTER_AREA)

# Displaying Collage on Display
cv2.imshow('My_Collage', collage_resized)
cv2.waitKey(10)
cv2.destroyAllWindows()



