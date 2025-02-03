#Justyn Collazo
#Lab 4
#2/2/25

#Program Prompt
#This is a two-part program where you will work on creating and populating parallel lists based on file data, then create
#and write data to a file.

#imports

import csv

#Variables

fName = []
lName = []
age = []
screenName = []
houseAlleg = []
email = []
department = []
phoneExt = []


#Main Code

#connected to file

with open ("textFiles/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        screenName.append(rec[3])
        houseAlleg.append(rec[4])
        email.append(f"{rec[3]}@westeros.net")

#disconnected from file

for i in range(0, len(fName)):

    if houseAlleg[i] == "House Stark":
        department.append("Research & Development")
        phoneExt.append()

    
    elif houseAlleg[i] == "House Targaryen":
        department.append("Marketing")
        phoneExt.append()
    
    elif houseAlleg[i] == "House Tully":
        department.append("Human Resources")
        phoneExt.append()
    
    elif houseAlleg[i] == "House Lannister":
        department.append("Accounting")
        phoneExt.append()

    elif houseAlleg[i] == "House Baratheon":
        department.append("Sales")
        phoneExt.append()
    
    elif houseAlleg[i] == "The Night's Watch":
        department.append("Auditing")
        phoneExt.append()
    
    else:
        department.append("ERROR")
        phoneExt.append("ERROR")

print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
print("-------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {department[i]:23}")
print("-------------------------------------------------------------------")

