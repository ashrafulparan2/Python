import json
book = {}
book['paran'] = {
    'name': 'paran',
    'id': 29,
}
book['2'] = {
    'name': 'paran2',
    'id': 229,
}


s = json.dumps(book)
# print(s)
with open("D://Misc//Python//book.txt", "w") as f:
    f.write(s)
f.close()
fr = open("D://Misc//Python//book.txt", "r")
s = fr.read()
print(s)

book = json.loads(s)
print(book)
print(type(book))