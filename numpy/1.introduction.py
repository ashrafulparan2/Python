import numpy as np
import time
import sys

a = np.arange(1000)
b = np.arange(1000)
print(a.size*a.itemsize)

x = range(1000)
y = range(1000)
print(sys.getsizeof(5)*len(x))

start=time.time()
result = [(i+j) for i,j in zip(a,b)]
end=time.time()
print((end-start)*1000)

start=time.time()
result = [(i+j) for i,j in zip(x,y)]
end=time.time()
print((end-start)*1000)
