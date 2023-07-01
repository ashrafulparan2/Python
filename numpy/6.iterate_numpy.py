import numpy as np
a = np.arange(12).reshape(3, 4)
for i in a:
    for j in i:
        print(a)

# flatten it

for i in a.flatten():
    print(i)

# nditer

for i in np.nditer(a, order='C'):  # C order
    print(i)
for i in np.nditer(a, order='F'):  # Fortran order
    print(i)

for i in np.nditer(a, order='F', flags=['external_loop']):
    print(i)

for i in np.nditer(a, op_flags=['readwrite']):
    i[...] = i*i
print(a)

b = np.arange(3, 15, 4).reshape(3, 1)
print(b)

for i, j in np.nditer([a, b]):
    print(i, j)
