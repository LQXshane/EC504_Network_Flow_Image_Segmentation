
# coding: utf-8
# __author__ = qiuxuan.lin


import cv2
import numpy as np
from sklearn import mixture
from sklearn import decomposition
# from IPython import embed
# import matplotlib.pyplot as plt

def proba_gmm(Z, K = '' , type = ''):

    g = mixture.GMM(n_components=K, covariance_type= type, random_state= 2500) # tried 'full' or 'spherical' no improvememts
    g.fit(Z)
    center = g.means_ # centroid RGB values
    center = np.uint8(center)
    proba = g.predict_proba(Z)

    return center, proba, g



