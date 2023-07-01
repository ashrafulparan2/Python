import numpy as np

x = np.arange(1, 10).reshape(3, 3)

print(x)

np.savetxt("test.txt", x)

y = np.loadtxt("test.txt")
print(y)
