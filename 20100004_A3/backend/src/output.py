#!/usr/bin/env python
# coding: utf-8

# ## Computer Vision(CS 436, CS5310, EE513) Programming Assignment#3 Part#1

#  Currently there are lots of professional cartoonizer applications available in the market but most of the them are not freeware, you don't need powerful rendering software or even years of experience to develop such an application(as you will see in this assignment) All you need is essentially a bilateral filter and some edge detection. You are allowed to use opencv for this assigment

#  Step#1
#  In this step we will be applying a bilateral filter on our input image. A bilateral filter is used for smoothening images and reducing noise, while preserving edges, because a bilateral filter smooths flat regions while keeping edges sharp, it is ideally suited to convert an RGB image into a cartoon. Unfortunately, bilateral filters are orders of magnitudes slower than other smoothing operators (e.g., Gaussian blur). Thus, if speed is important, it might be a good idea to operate on a down-scaled version of the original image first and then upscale it afterwards.


#required imports
import matplotlib
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import image as mpimg
from matplotlib.pyplot import figure
import cv2
import numpy as np




def cartoonifier(imagepath):
    num_down = 5 # number of downsampling steps 
    num_bilateral = 5  # number of bilateral filtering steps
    img = mpimg.imread(imagepath,0)
    img1 = img
    for i in range(num_down):
        img1 = cv2.pyrDown(img1)
    for i in range(num_bilateral):
        img1 = cv2.bilateralFilter(img1,d=9,sigmaColor=10,sigmaSpace=10) #9 is recommended for d from the documentation
    for i in range(num_down):
        img1 = cv2.pyrUp(img1)
    grayImg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    blurImg = cv2.medianBlur(grayImg,5)
    imgEdge = cv2.adaptiveThreshold(blurImg, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)
    imgEdgeRGB = cv2.cvtColor(imgEdge, cv2.COLOR_GRAY2RGB)
    imgEdgeRGB = cv2.resize(imgEdgeRGB,(img1.shape[1],img1.shape[0]))#Resizing the edges to the size of img1
    result = cv2.bitwise_and(imgEdgeRGB,img1)
    return result

def bw(imagepath):
    im_gray = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
    return im_gray


