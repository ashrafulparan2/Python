numbers = [1, 2, 3, 4, 5, 6]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
even = [i for i in numbers if i % 2 == 0]
print(even)
sqr = [i*i for i in numbers]
print(sqr)

s = set([1, 2, 3, 2])
print(s)
even = {i for i in numbers if i % 2 == 0}
print(even)
print(type(even))

cities = ["mumbai", "ny", "paris"]
country = ["india", "usa", "france"]
z = zip(cities, country)
for i in z:
    print(i)

d = {city: country for city, country in zip(cities, country)}
print(d)
