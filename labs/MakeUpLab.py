#Justyn Collazo
#Make up Lab replacing Lab #2
#3/6/25

#Program Prompt
#In this lab, you will build a Python application that allows a user to repeatedly choose an option
#from a menu to search through the data provided in the text file: students.txt

#--Imports---------------

import csv

#--Variables-------------

id = []
lastName = []
firstName = []
class1 = []
class2 = []
class3 = []

#--Main Code-------------

with open ("textFiles\students.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        id.append(rec[0])
        lastName.append(rec[1])
        firstName.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])
        
#disconnected from file

#print the menu
print("\t--Menu--\n1. See All Student Reports\n2. Search for a Student [ID]\n3. Search for a Student [Last Name]\n4. View a Class Roster [class1, class2, and class3]\n5. Exit/Quit Program")

