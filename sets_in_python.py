basket = {"orange", "apple", "mango", "mango"}
print(basket)
basket.add(1)
print(basket)

numbers=[1,2,2,21,1,2]
a=set(numbers)
a.add(3)
print(a)


# cannot add extra elements
b=frozenset(numbers)
# b.add(2)
# print(b)

c=set(numbers)
c.add(4)
print(c)

print(a|c)
print(a&c)
print(a<c)

d=set(numbers)

print(d<a)