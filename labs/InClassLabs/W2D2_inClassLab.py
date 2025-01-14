#Justyn Collazo
#SE126.02
#W2D2 - Text File Handling Review w/ filters!
#1-14-2025 [W2D2]

#The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room
# can accommodate, and the number of people currently registered for the event. Write a program that
# displays all rooms that are over the maximum limit of people and the number of people that have to
# be notified that they will have to be put on the wait list. After the file is completely processed the
# program should display the number of records processed and the number of rooms that are over the limit.



#Variables


#--Imports----------------------------------

import csv

#--Functions--------------------------------

def difference(people, maxCap):
    '''this function is passed 2 values and returns the difference between them.'''
    diff = maxCap - people
    return diff

#--Main Code--------------------------------

#initialize needed counting variables
totalRec = 0
roomsOver = 0

#--connected to file-----------------


print(f"{'NAME:':20}    {'MAX':4}   {'PPL':4}   {'OVER'}") #FIELD HEADERS for display
print("-------------------------------------------------------")
with open("textFiles/classLab2.csv") as csvfile:
    #we must indent one level while "connected to the file"

    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for every record (row) in the file (text file!)

        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1]) #all text data reads as a string, so cast as a num!
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display rooms that are over capacity (remaining is negative)
        if remaining < 0:
            roomsOver += 1

            print(f"{name:20}  {max:5}  {ppl:5}  {abs(remaining):5}") 

        totalRec += 1
#--connected to file-----------------

#display final data (counting vars)
print(f"\nRooms currently OVER CAPACITY: {roomsOver}")
print(f"Total rooms in file: {totalRec}\n\n")