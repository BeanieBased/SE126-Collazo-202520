#Justyn Collazo
#Lab 6
#2/24/25

#Program Prompt
#For Lab #6, you must use lists to create the airplane seating chart - either 1D or 2D lists.
#You may either create a file to read the data in for the seats, or you can hand-populate your own 1/2D lists.
#If you choose to create your own file, please upload along with your completed Lab #6 .py file. 


#Variables

ans = "y"

#Functions

def display():
    print("Row")
    print(f"{row1[0]}    {row1[1]}  {row1[2]}      {row1[3]}  {row1[4]}")
    print(f"{row2[0]}    {row2[1]}  {row2[2]}      {row2[3]}  {row2[4]}")
    print(f"{row3[0]}    {row3[1]}  {row3[2]}      {row3[3]}  {row3[4]}")
    print(f"{row4[0]}    {row4[1]}  {row4[2]}      {row4[3]}  {row4[4]}")
    print(f"{row5[0]}    {row5[1]}  {row5[2]}      {row5[3]}  {row5[4]}")
    print(f"{row6[0]}    {row6[1]}  {row6[2]}      {row6[3]}  {row6[4]}")
    print(f"{row7[0]}    {row7[1]}  {row7[2]}      {row7[3]}  {row7[4]}")

def prompt():
    ans = input("Would you like to pick another seat? [y/n]: ").lower()
    while ans != "y" and ans != "n":
        print("INVALID INPUT! Try again.")
        ans = input("Would you like to pick another seat? [y/n]: ").lower()
    return ans


#Populate the rows
row1 = [1, "A", "B", "C", "D"]
row2 = [2, "A", "B", "C", "D"]
row3 = [3, "A", "B", "C", "D"]
row4 = [4, "A", "B", "C", "D"]
row5 = [5, "A", "B", "C", "D"]
row6 = [6, "A", "B", "C", "D"]
row7 = [7, "A", "B", "C", "D"]

#display the chart
display()


while ans == "y":
    #pick a seat
    seatToReserve = input("\nWhich seat would you like to reserve? (Row, then letter. Example: 1B) ")


    #make seat reserved
    if seatToReserve == "1A":
        if row1[1] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row1[1] = "X"
    elif seatToReserve == "1B":
        if row1[2] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row1[2] = "X"
    elif seatToReserve == "1C":
        if row1[3] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row1[3] = "X"
    elif seatToReserve == "1D":
        if row1[4] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row1[4] = "X"
    elif seatToReserve == "2A":
        if row2[1] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row2[1] = "X"
    elif seatToReserve == "2B":
        if row2[2] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")        
        else:
            row2[2] = "X"
    elif seatToReserve == "2C":
        if row2[3] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row2[3] = "X"
    elif seatToReserve == "2D":
        if row2[4] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row2[4] = "X"
    elif seatToReserve == "3A":
        if row3[1] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row3[1] = "X"
    elif seatToReserve == "3B":
        if row3[2] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row3[2] = "X"
    elif seatToReserve == "3C":
        if row3[3] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row3[3] = "X"
    elif seatToReserve == "3D":
        if row3[4] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row3[4] = "X"
    elif seatToReserve == "4A":
        if row4[1] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row4[1] = "X"
    elif seatToReserve == "4B":
        if row4[2] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row4[2] = "X"
    elif seatToReserve == "4C":
        if row4[3] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row4[3] = "X"
    elif seatToReserve == "4D":
        if row4[4] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row4[4] = "X"
    elif seatToReserve == "5A":
        if row5[1] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row5[1] = "X"
    elif seatToReserve == "5B":
        if row5[2] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row5[2] = "X"
    elif seatToReserve == "5C":
        if row5[3] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row5[3] = "X"
    elif seatToReserve == "5D":
        if row5[4] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row5[4] = "X"
    elif seatToReserve == "6A":
        if row6[1] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row6[1] = "X"
    elif seatToReserve == "6B":
        if row6[2] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row6[2] = "X"
    elif seatToReserve == "6C":
        if row6[3] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row6[3] = "X"
    elif seatToReserve == "6D":
        if row6[4] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row6[4] = "X"
    elif seatToReserve == "7A":
        if row7[1] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row7[1] = "X"
    elif seatToReserve == "7B":
        if row7[2] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row7[2] = "X"
    elif seatToReserve == "7C":
        if row7[3] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row7[3] = "X"
    elif seatToReserve == "7D":
        if row7[4] == "X":
            print("Sorry! That seat is already reserved! Pick a new one.")
        else:
            row7[4] = "X"

    print("\nHere is the updated seating chart.")
    display()
    ans = prompt()

