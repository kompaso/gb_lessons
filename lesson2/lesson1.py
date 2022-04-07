x = 10
y = x

print(x, y)
print(id(x), id(y))
x = 10.0
print(x, y)
print(id(x), id(y))

x = '10.0'
print(x, y)
print(id(x), id(y))

print(help(print))
