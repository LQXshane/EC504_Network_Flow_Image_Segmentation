'__author__' == 'qiuxuan.lin'
# coding: utf-8
# Python 2.7.11

import numpy as np
from math import*


class graph_penalty():

    def __init__(self):

        self.width = 25
        self.height = 25
        self.penalty = 'man'

    def high(self, x):

        return (x-1)/self.width

    def low(self, x):

        global w

        return x-1-self.high(x)*self.width

    def fsigmoid(self, x):
        return 1 / (1 + np.exp(x))

    def euclidean_distance(self, a,b):
        return int(np.linalg.norm(a-b))

    def manhattan_distance(self, x,y):

        return sum(abs(a-b) for a,b in zip(x,y))


    def dist_penalty(self, graph):



        for i in range(len(graph)):

                for j in range(len(graph)):

                    if i == 0 or i == len(graph)-1: pass
                    elif j == 0 or j == len(graph)-1: pass
                    elif i ==j: pass
                    else:# decode i and j into x and y
                        x = (self.high(i),self. low(i))
                        y = (self.high(j),self. low(j))

                        if self.penalty == 'man':  graph[i][j] = np.int(self.fsigmoid((self.manhattan_distance(x,y)/1.0))*12)

                        if self.penalty == 'euc':  graph[i][j] = np.int(self.fsigmoid((self.euclidean_distance(x,y)/3.0))*12)