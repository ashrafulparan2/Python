x=int(input())
y=int(input())
# print(type(x))
try:
    z=x/y
except Exception as e:
    print(e)
    z=None
print(z)