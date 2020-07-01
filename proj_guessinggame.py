from random import randint

rand_num = randint(1, 10)
guess = None

while guess != rand_num:
    guess = int(input("Guess a number (1-10): "))
    if guess < rand_num:
        print("You were too low...")
    elif guess > rand_num:
        print("You were too high...")
    else:
        print("That's it!")
        if input("Want to play again? ") == "y":
            rand_num = randint(1, 10)
            guess = None
        else:
            print("Thanks for playing!")
            break