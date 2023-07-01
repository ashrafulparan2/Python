import numpy as np
x = np.loadtxt("test.txt", skiprows=1)
print(x)
x = np.loadtxt("data_file_1.csv", skiprows=9, delimiter=',')
print(x)
x = np.loadtxt("data_file_1b.csv")
print(x)

myheader = "This file contains 99 values"
a = np.arange(0, .99, 0.01).reshape(33, 3)
np.savetxt("data.txt", a, delimiter=",", header=myheader)
