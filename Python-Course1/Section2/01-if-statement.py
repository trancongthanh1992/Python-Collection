name = input("Please enter your name: ")
age = int(input(f"How old are you, {name}. "))
# print(f"\n hello {name},")
if age > 60:
    print(f"\n hello {name}, you're still old.")
elif age > 18:
    print(f"\n hello {name}, you're adult.")
else:
    print(f"\n hello {name}, you're still young.")
    print(f"\n Please come back in {18 - age} years")
