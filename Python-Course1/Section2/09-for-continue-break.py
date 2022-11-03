shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

print(30 * "* " + "Continue" + 30 * " *")

for item in shopping_list:
    if item == "spam":
        # ignore loop
        continue

    print("Buy: " + item)


print(30 * "* " + "Break" + 30 * " *")

for item in shopping_list:
    if item == "spam":
        # break whole loop
        break
    print("Buy: " + item)


x = None
print(f"x: {x}")
print(None == True)
print(None == False)


x = 10
print(f"x: {x}")