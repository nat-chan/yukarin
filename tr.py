#!/usr/bin/env python
# coding:utf-8

import sys
from PIL import Image
import numpy as np

def mymap(f, mt):
    return [[f(i) for i in j] for j in mt]

def shorten(mt):
    return [zip(mt[2*k], mt[2*k+1]) for k in range(len(mt)/2)]

def rgba2hex(rgba):
    r, g, b, a = rgba
    if a == 255:
        R = r*6/256
        G = g*6/256
        B = b*6/256
        return 36*R + 6*G + B + 16
    else:
        return 0

def comp(ud):
    u,d = ud
    return "\033[38;5;"+str(u)+";48;5;"+str(d)+"m▀"

def mystr(hex):
    return "\033[48;5;"+str(hex)+"m  "

def myshow(mt):
    return "\n".join(["".join(j) for j in mt])

with open(sys.argv[1], 'r') as f:
    im = Image.open(f).convert("RGBA")
    #im.show()
    mt = np.asarray(im)
    print myshow(mymap(comp, shorten(mymap(rgba2hex, mt))))
    #print myshow(mymap(mystr, mymap(rgba2hex, mt)))
