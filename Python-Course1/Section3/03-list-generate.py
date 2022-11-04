empty = []
even = [0, 2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9, 11]

print(30 * "* " + "Concat" + 30 * " *")
print(even + odd)

num = sorted(even + odd)


print(30 * "* " + "Concat" + 30 * " *")

num1 = [1, 2, 3, 4, 5]
num2 = [1, 2, 3, 4, 5]
num3 = num1
num4 = num3.copy()

print(f"id num1 {id(num1)}")
print(f"id num2 {id(num2)}")
print(f"id num3 {id(num3)}")
print(f"id num4 {id(num4)}")

print(num1 == num2) # True
print(num1 is num2) # False
print(num1 is num3) # True, Compare refference


print(num1 == num4) # True
print(num1 is num4) # True


print(30 * "* " + "Replace" + 30 * " *")

# Replace and remain rest item.
num1 = [1, 2, 3, 4, 5]
num2[0 : 4] = [6, 7, 8, 9, 10, 11]
print(num2)



num3 = [1, 2, 3, 4, 5]
num4[0 : ] = [6, 7, 8, 9, 10, 11]
print(num4)


num3 = [1, 2, 3, 4, 5]
num4[0 : ] = [6, 7]
print(num4)