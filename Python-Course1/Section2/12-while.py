
# print("Please guess number between 1 and 10: ")
# guess = int(input())

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Welldone, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Welldone, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


import random
from telnetlib import BRK

highest = 10
answer = random.randint(1, highest)
print(f"Answer {answer}")
guess = 0
print(f"Please guess number between 1 and {highest}")

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Answer must be greater 0.")
        break

    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")