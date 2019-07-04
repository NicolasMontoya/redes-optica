#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:39:58 2019

@author: nicolas
"""

import cv2
from matplotlib import pyplot as plt


img = cv2.imread("receptor/1.png")
im = cv2.hconcat((img,img))
ex = cv2.hconcat((im,img))

plt.subplot(2, 2, 1), plt.imshow(im)
plt.subplot(2, 2, 1), plt.imshow(ex)

plt.show()