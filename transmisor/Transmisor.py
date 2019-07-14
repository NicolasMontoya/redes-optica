#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Transmisor:
    
    def __init__(self, codes):
        self.repeat = []
        self.simbols = []
        self.result = ""
        for code in codes:
            info = code.split("-");
            self.simbols.append(format(int(info[0]), "b").zfill(4))
            self.repeat.append(format(int(info[1]), "b").zfill(3))
    def image(self):
        for i in range(0, len(self.simbols)):
            self.result = self.result + str(i+1) + ". " + self.simbols[i] + "- " + str(int(bool(self.simbols[i][0]) ^ bool(self.simbols[i][1]) ^ bool(self.simbols[i][2]) ^ bool(self.simbols[i][3]))) + self.repeat[i] + "\n"
        return self.result
        