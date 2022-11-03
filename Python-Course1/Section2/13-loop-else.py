numbers = [1, 45, 31, 16, 60]

# `else` in loop mean collection filter inexists. 
for number in numbers:
    if number % 8 == 0:
        print("The numbers are unacceptable.")
        break
else:
    print("All those numbers are fine.")

CONST = 10