import random
secretNumber = random.randint(1, 20)

print("I'm thinking of a number between 1-20.")

for i in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break
if guess == secretNumber:
    print("Good job! You guessed my number in " + str(i) + "guesses!")
else:
    print("Nope! The number I was thinking of was " + str(secretNumber))                
