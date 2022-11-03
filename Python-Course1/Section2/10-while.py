
i = 0
while i < 10:
    print(f"i is now {i}")
    i += 1

print(30 * "* " + "Break" + 30 * " *")


available_exists = ["north", "south", "east", "west"]

chose_exit = ""


while chose_exit not in available_exists:
    chose_exit = input("Please choose a direction")

print("Aren't you glad you got out of there")