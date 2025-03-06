#Justyn Collazo
#SE126.02
#W9D1 - Final
#3-3-2025 [W9D1]


#Program Description: It's battleship.

#--Imports------------

import csv
import random

#--Variables----------------

whichBoard = (random.randint(1, 5))

#--Functions-------


#--Main Code-----

with open("textFiles/battleship.csv") as csvfile:
    file = csv.reader(csvfile)

    boards = []  #List storing all the boards
    current_board = [] #Opponents selected board

    for rec in file:
        if rec:  #If the line isn't empty, add it to the current board.
            current_board.append(rec)
        else:  #Empty line means new board
            if current_board:
                boards.append(current_board)
                current_board = []

    if current_board:  #Add the last board if there's no blank line after
        boards.append(current_board)

#Selecting a board
if whichBoard == 1:
    print("Board 1 was Picked.") #testing
    selected_board = boards[0]

elif whichBoard == 2:
    print("Board 2 was Picked.") #testing
    selected_board = boards[1]

elif whichBoard == 3:
    print("Board 3 was Picked.") #testing
    selected_board = boards[2]

elif whichBoard == 4:
    print("Board 4 was Picked.") #testing
    selected_board = boards[3]

else:
    print("Board 5 was Picked.") #testing
    selected_board = boards[4]

# Print the board (testing)
for row in selected_board:
    print(row)
