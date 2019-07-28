#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:39:58 2019

@author: nicolas
"""

def in_parallel(v):
    v ^= v >> 16
    v ^= v >> 8
    v ^= v >> 4
    v &= 0xf
    return (0x6996 >> v) & 1

print(in_parallel(97))