a = 12
b = 3

print(a + b, "\t", type(a + b))  # int
print(a - b, "\t", type(a - b))  # int
print(a * b, "\t", type(a * b))  # int
print(a / b, "\t", type(a / b))  # float
print(a // b, "\t", type(a // b)) # 4 integer division, rounded down towards minus infinity
print(a % b, "\t", type(a % b))  # 0 modulo: the remainder after integer division.


# TypeError: 'float' object cannot be interpreted as an integer
# for i in range(1, a / b):
#     print(i)


for i in range(1, a // b):
    print(i)


# precedence
# () - [], ^, *, /, +, -
# () - [], Order, ^, *, /, +, -
# () - [], Index, ^, *, /, +, -

