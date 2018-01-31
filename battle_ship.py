"""
    This is "my" code from the CodeAcademy Battleship project.
"""

from random import randint

def random_row(ocean):
    return randint(0, len(ocean) - 1)

def random_col(ocean):
    return randint(0, len(ocean[0]) - 1)

def print_board(ocean):
    for row in ocean:
        print(" ".join(row))

board = []

for x in range(5):
    board.append(["O"] * 5)

print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

for turn in range(4):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    if turn == 3:
        print("Game Over")
    else:
        print("Turn", turn + 1, "\n")
        print_board(board)
