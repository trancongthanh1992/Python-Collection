parrot = "Norwegian Blue"

# sequence char in string.
for character in parrot:
    print(character)


number = "9,123,423,876,423,423"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

# ","
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()

print(values) 
print([int(val) for  val in values])


