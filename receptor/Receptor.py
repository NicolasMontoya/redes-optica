#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
from matplotlib import pyplot as plt


class Receptor:
    SIMBOL_MASK = 0xF0
    PARTITY = 0x08
    REPEAT = 0x07
    def __init__(self):
        self.images = []
    def decode(self, code):
        intDecode = int(code, 2)
        simbol = (intDecode & self.SIMBOL_MASK) >> 4
        parity = (intDecode & self.PARTITY) >> 3
        if ( bool(parity) == (bool(code[0]) ^ bool(code[1]) ^ bool(code[2]) ^ bool(code[3]))  ):
            repeat = (intDecode & self.REPEAT)
            return simbol, repeat, 1
        else:
            print("LA PARIDAD NO COINCIDE... REPIRA EL CARÁCTER")
            return None, None, 0
    def analize(self):
        size = 0;
        flag = False
        j = 0
        savedImage = []
        rowImage = []
        fulRowImage = []
        while True:
            data = input("Ingrese el dato \n")
            [sim, rep, ver] = self.decode(data)
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
                        (_, size, _) = fulRowImage.shape
                        savedImage = fulRowImage
                    else:
                        savedImage = savedImage[:,:800,:]
                        savedImage = cv2.vconcat((savedImage, fulRowImage))
                    fulRowImage = []
                    plt.imshow(savedImage)
                    plt.show()
                    flag = True
