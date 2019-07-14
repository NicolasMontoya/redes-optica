#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:34:14 2019

@author: nicolas
"""
import sys
from transmisor import Transmisor
from receptor import Receptor


def main(dictionary):
    mode = dictionary['mode']
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
        rx.analize()
    else:
         raise SyntaxError("Incorrect mode.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SyntaxError("Insufficient arguments.")
    if len(sys.argv) >= 2:
        kwargs = {x.split('=')[0]: x.split('=')[1] for x in sys.argv if '=' in x}
        main(kwargs)
    