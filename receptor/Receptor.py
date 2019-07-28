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
    def in_parallel(v):
        v ^= v >> 16
        v ^= v >> 8
        v ^= v >> 4
        v &= 0xf
        return (0x6996 >> v) & 1
    def decode(self, code):
        intDecode = int(code, 2)
        code = intDecode & 0xF7
        simbol = (intDecode & self.SIMBOL_MASK) >> 4
        repeat = (intDecode & self.REPEAT)
        parity = (intDecode & self.PARTITY) >> 3
        if (self.in_parallel(code) == parity):
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
                if sim > 8:
                    print("El simbolo no existe, repita de nuevo")
                elif sim != 8:
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
                        (_, sizeRow, _) = fulRowImage.shape
                        if sizeRow < size:
                            for p in range(0, (size - sizeRow), 100):
                                fulRowImage = cv2.hconcat((fulRowImage, self.BLACK))
                        else:         
                            fulRowImage = fulRowImage[:,:size+0,:]
                        savedImage = cv2.vconcat((savedImage, fulRowImage))
                    fulRowImage = []
                    plt.imshow(savedImage)
                    plt.show()
                    flag = True
                    
