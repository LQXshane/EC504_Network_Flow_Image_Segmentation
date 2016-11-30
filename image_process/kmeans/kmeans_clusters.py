import numpy as np
import cv2
from IPython import embed

img = cv2.imread('examples/kitten.jpg')
Z = img.reshape((-1,3))
Z = np.float32(Z)
# embed()
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# embed()
# Now convert back into uint8, and m
# ake original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
# embed()
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()