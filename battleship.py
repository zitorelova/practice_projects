board = []

for i in range(5): 
	board.append(['O'] * 5)

def print_board(board):
	for row in board:
		print " ".join(row)

print "Let's play Battleship!" 
print "You have 4 chances to guess where my battleship is."
print_board(board)
print "Rows and columns are numbered 0 to 4"

from random import randint

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(5):
	guess_row = int(raw_input("Guess Row: "))
	guess_col = int(raw_input("Guess Col: "))

	if guess_row == ship_row and guess_col == ship_col:
		print "You sank my battleship!"
		break

	if guess_row not in range(5) or guess_col not in range(5):
		print "Oops, that's not even in the ocean."
	elif board[guess_row][guess_col] == 'X':
		print "You guessed that one already."
	else: 
		print "You missed my battleship!"
		board[guess_row][guess_col] = 'X'

	print_board(board)

	if turn == 4:
		print "Game Over"
		print "My battleship was on row", ship_row, "col", ship_col
		break

	print "Turn", turn + 1, "done"


