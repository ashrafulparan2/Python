# f = open("D://Misc//Python//book.txt", "r")
# print(f.read())
# f.close()

# f = open("D://Misc//Python//test.txt", "w")
# f.write("Hello")
# f.close()

# f = open("D://Misc//Python//test.txt", "a")
# f.write("World")
# f.close()

f = open("D://Misc//Python//test.txt", "r")
# print(f.read())
# f.close()

# for line in f:
#     print(line)

# count no of words

for line in f:
    t=line.split(" ")
    print(len(t))