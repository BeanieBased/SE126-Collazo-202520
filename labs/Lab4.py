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
starkNum = 99
targNum = 199
tullyNum = 299
lanNum = 399
baraNum = 499
nightNum = 599

for i in range(0, len(fName)):

    if houseAlleg[i] == "House Stark":
        department.append("Research & Development")
        starkNum += 1
        phoneExt.append(starkNum)

    
    elif houseAlleg[i] == "House Targaryen":
        department.append("Marketing")
        targNum += 1
        phoneExt.append(targNum)
    
    elif houseAlleg[i] == "House Tully":
        department.append("Human Resources")
        tullyNum += 1
        phoneExt.append(tullyNum)
    
    elif houseAlleg[i] == "House Lannister":
        department.append("Accounting")
        lanNum += 1
        phoneExt.append(lanNum)

    elif houseAlleg[i] == "House Baratheon":
        department.append("Sales")
        baraNum += 1
        phoneExt.append(baraNum)
    
    elif houseAlleg[i] == "The Night's Watch":
        department.append("Auditing")
        nightNum += 1
        phoneExt.append(nightNum)
    
    else:
        department.append("ERROR")
        phoneExt.append("ERROR")

print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
print("--------------------------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {department[i]:23} {phoneExt[i]:3}")
print("--------------------------------------------------------------------------------------")


#WRITE SOME DATA TO A NEW FILE
#create and write all of the data to a new text file:
file = open('textFiles/westeros.csv', 'w')

for i in range(0,len(fName)):
    file.write(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {department[i]:23} {phoneExt[i]:3}\n")

file.close()