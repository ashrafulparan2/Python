import numpy as np
n = [1, 2, 3]
print(n[0:2])
print(n[-1])

a = np.array([1, 2, 3])
print(a[0:2])

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[0:3, 1])
print(a[-1])
print(a[:, 1: 2])

for i in a.flat:
    print(i)

a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)
print(a)
print(b)
print(np.vstack((a, b)))
print(np.hstack((a, b)))

a = np.arange(30).reshape(2, 15)
print(a)
res = np.hsplit(a, 3)
for i in res:
    print(i)

res = np.vsplit(a, 2)
for i in res:
    print(i)

a = np.arange(12).reshape(3, 4)
b = a > 4
print(b)
print(a[b])
