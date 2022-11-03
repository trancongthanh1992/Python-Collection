# < Less than
# <= Less than or equal to
# > Greater than
# >= Greater than or equal to
# == Equal to
# == Not equal to

# and, or, in, 
#
age = int(input("How old are you? "))


if 16 <= age <= 65:
    print("Have a good day at work")


if age >= 16 and age <= 65:
    print("Have a good day at work")




if age < 16 or age > 65:
    print("Have a good free time")
else:
    print("Have a good day at work")