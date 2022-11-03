print(50 * "*" + "Slice" + 50 * "*")

parrot = "Norwegian Blue" # 0 -> 13 => 14 elements in range.

print(parrot[0:6])      # Norweg

# [start index: end index: step]    => step > 0, default = 1
print(parrot[0:6:1])    # Nre       => step default value
print(parrot[0:6:2])    # Nre       => step ignore 1 value
print(parrot[0:6:3])    # Nw        => step ignore 3 value

number = "9,223,123,043,321,123"
seperators = number[1: :4]      # ,,,,,        => step ignore 3 value
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

print(50 * "*" + "Slice Backward" + 50 * "*")
letters = "abcdefghijklmnopqrstuvwxyz"

# Reverse String

backwards = letters[25:0:-1]
print(backwards)


# challenge
# slice the string to produce "qpo"
print(letters[16:13:-1])
print(letters[-10:-13: -1])


# slice the string to produce "edcba"
print(letters[4:: -1]) 


# slice the string to produce the last 8 characters, in reverse order
print(letters[-1:-9:-1]) 
print(letters[-8:-1:1]) 
