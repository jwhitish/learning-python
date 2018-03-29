#the collatz sequence - user enters a number which is then run through the collatz sequence function until the output number is 1

def collatz(number):
  x = number
  while x != 1:
    if x %  2 == 0:
      print(x // 2)
      x = x // 2
    else:
      print(3 * x + 1)
      x = 3 * x + 1

def run_collatz():
  try:
    number = int(input("Enter a number:"))
    collatz(number)
  except ValueError:
    print("Error: Did not enter number.")

run_collatz()
