from random import randint

board = []

#create a blank 5x5 board

for x in range(0, 5):
  board.append(["O"] * 5)

#remove commas and brackets from output

def print_board(board):
  for row in board:
    print " ".join(row)

#create random battleship location

def random_row(board_in):
  x = randint(0,len(board_in) - 1)
  return x

def random_col(board_in):
  y = randint(0,len(board_in) - 1)
  return y

ship_row = random_row(board)
ship_col = random_col(board)

#uncomment to display ship location for debugging
#print ship_row
#print ship_col

#to allow four guesses by the player
for turn in range(4):

#to let player guess location

  guess_row = int(raw_input("Guess Row:"))
  guess_col = int(raw_input("Guess Col:"))

#check to see if player is correct, on board, or already guessed that spot, reduce turn count by one, end game if turns up

  if guess_row == ship_row and ship_col == guess_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(5) or \
    guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
  if turn == 3:
    print "Game Over"
  else:
    print
    print "Turn", turn + 1
    print_board(board)
