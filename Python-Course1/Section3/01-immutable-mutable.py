# immutable always change new id when you change data in variable, copy on write
# int
# float
# bool (True or False) - a subclass of int
# str
# tuple
# frozenset
# bytes

# mutable doesn't change id when you change data in variable, refference
# object
# list
# dict
# set
# bytearray

print(30 * "* " + "Immutable" + 30 * " *")

result = True
another_result = result
print(30 * "* " + "Bool" + 30 * " *")

print(f"result -> id = {id(result)}")
print(f"another_result -> id = {id(another_result)}")

print()

# renew variable because of `result` is immutable
# id of `result` always change when data is changed.
result = False

print("after changed result = False")
print(f"result -> id = {id(result)}")
print(f"another_result -> id = {id(another_result)}")

print(30 * "* " + "String" + 30 * " *")

result_str = "result"
result_str1 = result_str

print(f"result_str -> id = {id(result_str)}")
print(f"result_str1 -> id = {id(result_str1)}")
print()
print("after changed result_str += \"abc\" ")

# id of `result_str` always change when data is changed.
result_str += "abc"
print(f"result_str -> id = {id(result_str)}")
print(f"result_str1 -> id = {id(result_str1)}")

print()
print(30 * "* " + "Mutable" + 30 * " *")

list1 = [1,2,3,4]
list2 = list1

print(f"list1 -> id = {id(list1)}")
print(f"list2 -> id = {id(list2)}")

# mutable refference
list1[0] = 10

# id of `result_str` always change when data is changed.
print(f"list1 -> id = {id(list1)} - {list1}")
print(f"list2 -> id = {id(list2)} - {list2}")