import numpy as np
from numpy.ctypeslib import ndpointer
import ctypes
# from IPython import embed

_intpp1 = ndpointer(dtype=np.int64, ndim=1, flags='C', shape=None)
# _intpp2 = ndpointer(dtype=np.int32, ndim=1)

_dll = ctypes.CDLL('image_process/dist_penalty.so')

_dist_penalty = _dll.penalty
_dist_penalty.argtypes = [ctypes.c_int, ctypes.c_int, _intpp1, ctypes.c_int ]
_dist_penalty.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))

def dist_penalty(sp, V, w):
    # m = ctypes.c_int(len(sp))
    # **penalty(int len, int len2, int sp[len2], int w)
    res = _dist_penalty(V, len(sp), sp, w)
    res2 = np.zeros(shape=(V,V))
    res2.dtype = np.int64
    for i in range(V):
        for j in range(V):
            res2[i][j] = res[i][j]
    res3 = res2 + res2.transpose()
    return res3

# if __name__ == '__main__':
#
#     sp = np.array([2, 3, 6], np.int32)
#     print type(sp.shape)
#     graph = dist_penalty(sp,12, 2)
#
#
#     embed()
#     # print type(res)