def func(exp):
    total = 0
    for item in exp:
        total += item
    return total

lista = [1,2,3]
listb = [4,5,6]

print(func(lista))
print(func(listb))