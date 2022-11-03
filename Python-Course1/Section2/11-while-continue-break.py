print(30 * "* " + "Break" + 30 * " *")
available_exists = ["north", "south", "east", "west"]

chose_exit = ""


while chose_exit not in available_exists:
    chose_exit = input("Please choose a direction: ")
    if chose_exit.casefold() == "quit":
        print("Game over")
        break

print("Aren't you glad you got out of there")



print(30 * "* " + "Continue" + 30 * " *")
index = 0
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
while index < len(shopping_list) - 1:
    if shopping_list[index] == "spam":
        # ignore loop
        continue

    print("Buy: " + shopping_list[index])
    index += 1