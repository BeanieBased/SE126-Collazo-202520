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
    #print("Board 1 was Picked.") #testing
    selectedBoard = boards[0]

elif whichBoard == 2:
    #print("Board 2 was Picked.") #testing
    selectedBoard = boards[1]

elif whichBoard == 3:
    #print("Board 3 was Picked.") #testing
    selectedBoard = boards[2]

elif whichBoard == 4:
    #print("Board 4 was Picked.") #testing
    selectedBoard = boards[3]

else:
    #print("Board 5 was Picked.") #testing
    selectedBoard = boards[4]

guessBoard = [['~'] * len(selectedBoard[0]) for _ in range(len(selectedBoard))]

# Count the total ships (X) on the selected board
total_ships = sum(row.count('X') for row in selectedBoard)

# Initialize hit counter
hits = 0

#Print the board (testing)
#for rec in selectedBoard:
#    for cell in rec:
#        print(cell, end=" ")  # print the rows with no brackets
#    print()  # Move to the next line after printing a row

#Actual Game
while hits < total_ships:
    row, col = map(int, input("Enter row and column [example: 1 6]: ").split())
    
    if selectedBoard[row][col] == 'X':
        print("Hit!")
        guessBoard[row][col] = 'X'
        hits += 1
    else:
        print("Miss!")
        guessBoard[row][col] = 'O'
    
    #Print the guessBoard after each move
    for rec in guessBoard:
        for cell in rec:
            print(cell, end=" ")
        print()  #Move to the next line after printing a row

print("You sank all the ships! You win!")