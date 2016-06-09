#!/usr/bin/env python
# coding:utf-8

import sys
from PIL import Image
import numpy as np

black = [0, 0, 0, 255]
im = Image.open(sys.argv[1]).convert("RGBA")
mt = np.asarray(im)
mt.flags.writeable = True
#imm = Image.fromarray(mt, mode='RGBA')
mt[0:20][0:100]=black
imm = Image.fromarray(mt)
#imm.show()
imm.save(sys.argv[2])
