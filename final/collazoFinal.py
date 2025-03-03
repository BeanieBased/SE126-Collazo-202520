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
    
    if whichBoard == 1:
        print("Board 1 was Picked.")

    elif whichBoard == 2:
        print("Board 2 was Picked.")
    elif whichBoard == 3:
        print("Board 3 was Picked.")
    elif whichBoard == 4:
        print("Board 4 was Picked.")
    else:
        print("Board 5 was Picked.")

