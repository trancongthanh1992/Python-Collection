# < Less than
# <= Less than or equal to
# > Greater than
# >= Greater than or equal to
# == Equal to
# == Not equal to

# and, or, in, 
#
answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Welldone, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Welldone, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")