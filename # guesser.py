import random
import time

top = input("Please type a number. ")
if top.isdigit():
    top = int(top)
    if top <= 0:
        print("Make sure your number is greater than 0")
        quit()
else:
    print("Please type a number next time")
    quit()
x = random.randint(0, top)
tries = 0

hel = input("Do you want help? ")
if hel.lower() == "yes":
    tries = 0
    while True:
        guess = input("Make a guess ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Make sure your guess is a number")
            continue
        if guess == x:
            print("You got it right! nice job")
            time.sleep(2)
            print("It took you " + str(tries) + " tries to guess it")
            break
        else:
            if guess > x:
                print("Your guess is greater than the actual number")
            if guess < x:
                print("your guess is less than the actual number")
            tries += 1
else:
    while True:
        guess = input("Make a guess ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Make sure your guess is a number")
            continue
        if guess == x:
            print("You got it right! nice job")
            time.sleep(2)
            print("It took you " + str(tries) + " tries to guess it")
            break
        else:
            print("Incorrect, try again")
            tries += 1
