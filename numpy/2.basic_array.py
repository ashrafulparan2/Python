import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.ndim)
print(a.shape)
b = np.array([1, 2, 3], dtype=np.float64)
print(b)
print(b.dtype)

c = np.array([1+2j, 2, 3])
print(c)
print(c.dtype)

d = np.zeros(3, dtype=int)
print(d)

d = np.ones(3)
print(d)

d = np.linspace(1, 10, 20)
print(d)

# a = np.array([[1, 2], [3, 4]], [5, 6])
print(a.shape)
x = a.reshape(2, 3)
print(x)
x = a.ravel()
print(x)
print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(np.sqrt(a))
print(np.std(a))

x = np.arange(4)
y = np.arange(4)
print(x+y)
print(x.dot(y)) #matrix multiplication
