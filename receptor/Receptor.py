#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Receptor:
    SIMBOL_MASK = 0xF00
    PARTITY = 0x080
    REPEAT = 0x070
    CHECK = 0x00F
    def __init__(self):
        self.images = []
    def decode(self, code):
        intDecode = int(code, 2)
        simbol = (intDecode & self.SIMBOL_MASK) >> 8
        parity = (intDecode & self.PARTITY) >> 7
        check = (intDecode & self.CHECK)
        if (parity == 1 and (check + simbol) == 15):
            repeat = (intDecode & self.REPEAT) >> 4
            return simbol, repeat, 1
        else:
            print("LA PARIDAD NO COINCIDE... REPIRA EL CARÁCTER")
            return None, None, 0

