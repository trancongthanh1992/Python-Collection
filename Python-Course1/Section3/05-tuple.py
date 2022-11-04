# Tuple is immutable
# Tuple support to spread.

name, age = ("Thanh", 30)
print(name)
print(age)

tuple1 = "Meo", 8
print(tuple1[0])
print(tuple1[1])

print(len(tuple1))

# TypeError: 'tuple' object does not support item assignment
# tuple[0] = "Meo Mun"

# print(tuple[0])
# print(tuple[1])

# Convert tuple to list
list = list(tuple1)
print(list)

tuple = tuple(tuple1)
print(tuple)

# tuple spread out
a, b = 10, 100
print(a)
print(b)

x, y, z = 100, 200, [1, 2 ,3]
print(x)
print(y)
print(z)

# python support single assignment
# x, y, z = 100
# print(x)
# print(y)
# print(z)

# # python 
# head, tail = [1, 2, 3, 4]
# print(head)
# print(tail)


for t in enumerate("abcdefg"):
    index, char = t
    print(f"index: {index} - value {char}")