import cv2
import numpy as np
from scipy.misc import imresize
# from IPython import embed


def edges(width, height, filename = ''):

    img = cv2.imread(filename, 0)
    img = imresize(img, (width, height))
    ed = cv2.Canny(img,100,200)
    ed = ed.flatten()
    specs = []
    for i in range(len(ed)):
        if ed[i] > 0:
            specs.append(i)
    return specs

#
# e  = edges('../../kitten.jpg')
# embed()



