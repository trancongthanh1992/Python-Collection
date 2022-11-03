
print(50 * "*" + "String Operators" + 50 * "*")

str1 = "he's "
str2 = "probably "
str3 = "pining "
str4 = "for the "
str5 = "fjords "

print(str1 + str2 + str3 + str4 + str5)

# multiple string.
print("hello " * 5)

# multiple string.
# TypeError: can only concatenate str (not "int") to str
# print("hello " * 5 + 5)

print("hello " * (5 + 5))

print("hello " * 5 + "4")


today = "friday"
print("day" in today)   # True
print("fri" in today)   # True

print("thur" in today)  # False

age = 30
print(50 * "*" + "String Replacement" + 50 * "*")
print("My age is {0}".format(age))

format = "There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec")
print(format)

print("""
Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}
""".format(28, 30, 31)
)





# {0:2} = {value for replace : tab spacing} = right spacing
# {0:<3} = {value for replace : tab spacing} = left spacing
for i in range (1, 10):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))


print()

for i in range (1, 10):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))

print()

print("Pi is approximately {0:<12}".format(22 / 7), type(22/7))
print("Pi is approximately {0:<12f}".format(22 / 7), type(22/7))
print("Pi is approximately {0:<12.50f}".format(22 / 7), type(22/7))
print("Pi is approximately {0:<52.50f}".format(22 / 7), type(22/7))
print("Pi is approximately {0:<62.50f}".format(22 / 7), type(22/7))
print("Pi is approximately {0:<72.50f}".format(22 / 7), type(22/7))
print("Pi is approximately {0:<72.54f}".format(22 / 7), type(22/7))


for i in range (1, 10):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))

print(50 * "*" + "String Interpolation" + 50 * "*")

# format string
name = "Thanh"
age_in_words = "5 years"

# interpolation string
greeting = name + f" is {age} years old"
# print(name + f" is {age} years old")
print(greeting)
print(type(greeting))
print(type(age_in_words))

print(f"Pi is approximately {22 / 7 : 12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi : 12.50f}")