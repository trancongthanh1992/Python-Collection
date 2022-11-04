shop_list = [
    "milk",
    "pasta",
    "eggs",
    "spam",
    "bread",
    "rice"
]

another_list = shop_list

print(f"shop_list - id {id(shop_list)}")
print(f"another_list - id {id(another_list)}")

shop_list += ["cookie"]

print(shop_list)
print(another_list)

print(f"shop_list - id {id(shop_list)}")
print(f"another_list - id {id(another_list)}")

another_list += ["apple pie"]

print(shop_list)
print(another_list)

print(f"shop_list - id {id(shop_list)}")
print(f"another_list - id {id(another_list)}")

print(30 * "* " + "Mutable Sequence Types" + 30 * " *")



shopping_list = [
    "milk",
    "pasta",
    "eggs",
    "spam",
    "bread",
    "rice"
]
print(shopping_list)


print(30 * "* " + "Append, Range, Delete" + 30 * " *")
# replace at 0 and 1, append 3, 4, 5 and the rests.
shopping_list[0:2] = [1, 2, 3, 4, 5]
print(shopping_list)

# remove index from 0 to 4 
del shopping_list[0:5]
print(shopping_list)

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# remove index from 0 to 4 step 2
del num_list[0:5:2]
print(num_list)

# Append 1 item.
num_list.append(21)

# Append more items.
num_list += [22, 23]
print(num_list)

print()
print(30 * "* " + "Copy" + 30 * " *")
num1_list = num_list.copy()
print(num_list)
print(num1_list)

num1_list += [24]

print(num_list, f" id: {id(num_list)}")
print(num1_list, f" id: {id(num1_list)}")

print()
print(30 * "* " + "Enumerate" + 30 * " *")
for index, item in enumerate(num1_list):
    print(f"index = {index} , item = {item}")

    
for index, char in enumerate("abcdefghjk"):
    print(f"index = {index} , item = {char}")
    
    
val = [str(i) for i in range (0, 10)]
print(f"val = {val}")


print(30 * "* " + "Copy" + 30 * " *")
numeric_list = [1, 2, 3, 4, 5, 6, 7]

# IndexError: list assignment index out of range
# del numeric_list[7]

# ValueError: list.remove(x): x not in list
# numeric_list.remove(8)


# numeric_list += [10,9,8,7]
numeric_list.extend([10,9,8,7])
print(numeric_list)


print(numeric_list.sort(reverse=True))
print(numeric_list)


print(sorted(numeric_list))
print(numeric_list)