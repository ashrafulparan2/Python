def remote():
    yield "cnn"
    yield "espn"


itr = remote()
print(itr)
print(next(itr))
print(next(itr))

for i in remote():
    print(i)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for f in fib():
    if f > 133:
        break
    print(f)