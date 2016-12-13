
'__author__' == 'qiuxuan.lin'
# coding: utf-8
# Python 2.7.11

import numpy as np
from edge_detect.gen_edge_mat import edges


def euclidean_distance(a, b, w):
    # decode i and j into x and y

    x = (high(a,w), low(a,w))

    y = (high(b,w), low(b,w))

    return int(np.linalg.norm(x-y))


def manhattan_distance(a, b, w):
    # decode i and j into x and y

    x = (high(a, w), low(a, w))

    y = (high(b, w), low(b, w))

    return sum(abs(i - j) for i, j in zip(x, y))


def high(x, w):
    return (x - 1) / w


def low(x, w):
    return x - 1 - high(x, w) * w


def fsigmoid(x):
    return 1 / (1 + np.exp(x))


def dist_penalty(df, w, h, penalty='', file = ''):
    df_fill = df
    sp = edges(w, h, file)
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if i == 0 or i == len(df) - 1: pass
            elif j == 0 or j == len(df) - 1: pass
            elif i in sp:
                df_fill[i][j] = np.int(fsigmoid((manhattan_distance(i, j, w) / 0.90)) * 6.5)
            else:
                if penalty == 'man':
                    df_fill[i][j] = np.int(fsigmoid((manhattan_distance(i, j, w) / 0.995)) * 14)
                if penalty == 'euc':
                    df_fill[i][j] = np.int(fsigmoid((euclidean_distance(i, j, w) / 3.0)) * 12)
    df_new = (df_fill + df_fill.transpose())
    return df_new, sp
