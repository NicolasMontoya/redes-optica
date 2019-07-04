#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:34:14 2019

@author: nicolas
"""
import sys
from transmisor import Transmisor
from receptor import Receptor
import cv2
from matplotlib import pyplot as plt


def main(dictionary):
    mode = dictionary['mode']
    flag = False
    j = 0
    savedImage = []
    rowImage = []
    fulRowImage = []
    if (mode == '1'):
        file = open("transmisor/data.txt", "r")
        data = file.read()
        t = Transmisor.Transmisor(data.split("\n"))
        printInfo = t.image()
        file = open("transmisor/sendInfo.txt", "a")
        file.write(printInfo)
        file.close()
    elif (mode == '2'):
        rx = Receptor.Receptor()
        while True:
            data = input("Ingrese el dato \n")
            [sim, rep, ver] = rx.decode(data)
            if ver == 1:
                if sim != 8:
                    if not flag:
                        flag = True
                        loadImage = cv2.imread("receptor/" + str(sim) + ".png")
                        print("receptor/" + str(sim) + ".png")
                    else:
                        loadImage = cv2.imread("receptor/" + str(sim) + ".png")
                    for i in range(0, rep):
                        if len(rowImage) > 0:
                            rowImage = cv2.hconcat((rowImage, loadImage))
                        else:
                            rowImage = loadImage
                    if len(fulRowImage) > 0:
                        fulRowImage = cv2.hconcat((fulRowImage, rowImage))
                        rowImage = []
                    else:
                        fulRowImage = rowImage
                        rowImage = []
                else:
                    j += 1
                    if len(savedImage) == 0:
                        savedImage = fulRowImage
                    else:
                        savedImage = cv2.vconcat((savedImage, fulRowImage))
                    fulRowImage = []
                    plt.imshow(savedImage)
                    plt.show()
                    flag = True
    else:
         raise SyntaxError("Incorrect mode.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SyntaxError("Insufficient arguments.")
    if len(sys.argv) >= 3:
        kwargs = {x.split('=')[0]: x.split('=')[1] for x in sys.argv if '=' in x}
        main(kwargs)
    