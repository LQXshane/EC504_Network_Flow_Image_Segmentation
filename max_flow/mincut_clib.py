import numpy as np 
from numpy.ctypeslib import ndpointer 
import ctypes 

_intpp = ndpointer(dtype=np.int32, ndim=2, flags='C')

_dll = ctypes.CDLL('max_flow/bfs.so')

_mincut = _dll.mincut
_mincut.argtypes = [ctypes.c_int, ctypes.c_int, _intpp,ctypes.c_int,ctypes.c_int,ctypes.c_int ]
_mincut.restype = ctypes.POINTER(ctypes.c_bool)

def mincut(x,src,sink, V):
    m = ctypes.c_int(x.shape[0])
    n = ctypes.c_int(x.shape[1])
    res = _mincut(m, n, x, src,sink,V)
    # print [res[i] for i in range(6)]
    return res

# if __name__ == '__main__':
#     x = np.array([
#          [0, 16,13,0 ,0, 0 ],
#          [0, 0, 10,12,0, 0 ],
#          [0, 4, 0, 0, 14,0 ],
#          [0, 0, 9, 0, 0, 20],
#          [0, 0, 0, 7, 0, 4 ],
#          [0, 0, 0, 0, 0, 0 ]
#                             ],np.int32)
#
#     res = mincut(x)
#     #print type(res)