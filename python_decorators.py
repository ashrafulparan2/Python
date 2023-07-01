import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__+str(end-start)+"s")
        print("hi")
        return result
    return wrapper


@timeit
def area(a, b):
    a = 2
    b = 2
    return a*b


print(area(2,3))