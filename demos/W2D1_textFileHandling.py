#W2D1 - Text File Handling - Introduction

#STEP 1: import the CSV (comma separated value) library
import csv

totalRecords = 0 #the total number of records (rows) in the file

#connecting to the file's path - switch \ to /
#----connected to file-------
print(f"{'NAME':10} \t {'NUM':3} \t {'COLOR'}")
print("--------------------------------------")
with open("textFiles/simple.csv") as csvfile:
    #indent 1 level! (new block)

    #allow processor to read the file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:

        #add +1 to total_records
        totalRecords += 1

        name = record[0]
        number = record[1]
        color = record[2]

        print(f"{name:10} \t {number:3} \t {color}")
#----disconnected from file------
print("--------------------------------------")
print(f"\nTOTAL RECORDS: {totalRecords}\n")