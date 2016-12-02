'__author__' == 'qiuxuan.lin'
# coding: utf-8
# Python 2.7.11

from datetime import datetime
from IPython import embed
import gc
import sys
sys.path.append('/Users/Shane/Documents/EC504_Network_Flow_Image_Segmentation/')
from image_process.GMM.proba import proba_gmm
from max_flow.mincut_fordfulkerson import mincut
from image_process.graph_utils import graph_penalty
from sklearn import decomposition
import cv2
import numpy as np
from math import*
from skimage.measure import block_reduce



# functions used to normalize and cal. scores
def sigmoid_array(x):
  return 1 / (1 + np.exp(-x))

if __name__ == '__main__':

    if len(sys.argv[1]) < 3:
        print "Please specify the name of your image!"
        exit()
    # Read file, currently we only support square images n*n
    image_in = sys.argv[1]
    img = cv2.imread(image_in)
    Z = img.reshape((-1,3))
    Z = np.float32(Z)

    original_width, original_height = img.shape[:2]

    print "Your image is in size %d * %d" %(original_width, original_height)

    # if original_width != original_height:
    #     print "Only support N-by-N images at this time... "
    #     exit()


    print "Getting likelihood scores: ", datetime.now()

    # Step 1. utilize Gaussian Mixture Model, using RGB as feature  and choose K = 16
    # Step 2. we will then perform dimensionality reduction, PCA, feature matrix using the probabilities generated by GMM
    centroid, pixel_proba, model = proba_gmm(Z,16, 'diag')
    pca = decomposition.PCA(2, whiten= True)
    reduced_proba = pca.fit_transform(pixel_proba)
    reduced_proba = sigmoid_array(reduced_proba) # map PCA results into (0,1) space
    label = reduced_proba.argmax(axis = 1)
    center = centroid[1:3]

    res = center[label.flatten()] # original picture
    res2 = res.reshape((img.shape)) # likelihood calculated, visualize at the end

    # Step3. Down-sampling: due to the limits of our current algorithm,
    # we scale it into 25*25 and "merged" the corresponding likelihood scores
    # MinCut takes about 30s
    # however, 50*50 image would take much longer.
    scalestring = input("Enter your desired scale ratio: ")
    scale_ratio = int(scalestring)
    w = int(original_width/scale_ratio  )
    h = int(original_height/scale_ratio  )
    new_proba_a = [[0 for col in range(w)] for row in range(h)]
    tmp = reduced_proba[:,0].reshape(original_width,original_height)
    for i in range(0,len(tmp), scale_ratio):
        for j in range(0,len(tmp),scale_ratio):
           new_proba_a[i/scale_ratio][j/scale_ratio] =  tmp[i][j] + tmp[i][j+1] + tmp[i+1][j] + tmp[i+1][j+1]

    new_proba_b = [[0 for col in range(w)] for row in range(h)]
    tmp = reduced_proba[:,1].reshape(original_width,original_height)
    for i in range(0,len(tmp), scale_ratio):
        for j in range(0,len(tmp),scale_ratio):
           new_proba_b[i/scale_ratio][j/scale_ratio] =  tmp[i][j] + tmp[i][j+1] + tmp[i+1][j] + tmp[i+1][j+1]

    a = np.ceil(np.array(new_proba_a)*7).reshape(w*h)
    b = np.ceil(np.array(new_proba_b)*7).reshape(w*h)

    # Ai and Bi's are obtained, generating adjacency matrix ...

    n = len(a) #total number of pixels - internal "nodes"
    V = n+2 # including source and sink, V is the dim. of the input matrix
    graph = [[0 for col in range(V)] for row in range(V)]

    gp = graph_penalty()

    gp.width, gp.height     = w, h
    gp.dist_penalty(graph)

    for i in range(1,n+1):
        graph[0][i], graph[i][n+1] = int(a[i-1]), int(b[i-1])

    embed()



    src = 0  # source node
    sink = n + 1  # sink node

    print "Matrix dimension:  V = ",V, ", finding a minimum cut...", datetime.now()

    # print " Depending on your image size, this will take approximatly %d min. " %
    # call mincut
    visited_nodes = mincut(graph, src, sink, V)

    print "Reconstructing Image, mouse over to check the images and hit 'return' to quit program ...", datetime.now()


    final_label = np.array(visited_nodes[1:w*h +1])
    final_label = final_label * 1
    center[0] , center[1]= [0,0,0] , [255,255,255]
    res_new = center[final_label.flatten()]
    res2_new = res_new.reshape((w,h,3))
    # embed()
    # res2_new = cv2.pyrUp(res2_new,dstsize = (original_width,original_height))
    from scipy.misc import imresize

    res2_new = imresize(res2_new, (original_width, original_height, 3))


    cv2.imshow('Original Image', img)
    cv2.imshow('GMMed with PCA', res2)
    cv2.imshow('MinCut result', res2_new)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gc.collect()

