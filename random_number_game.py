from random import randint

random_number = randint(1, 10)
#print random_number

guesses_left = 3

while guesses_left > 0:
  guess = int(raw_input("Guess the number: "))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."
