#W4D1 - Sequential Search


#PROGRAM PROMPT: We will continue to work with the class_grades.csv file, as used in the W3D2 demo.
#We will practice connecting to a file, storing the file data into parallel lists, and creating new 
#data for each student record based on these lists. We will then build a sequential search program which will allow us to 
#find students in the file, and write data regarding them to a newly created file in our repository.





#this file uses class_grades.csv

#--Imports-----------------------------------------------

import csv

#--Functions---------------------------------------------

def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"
    
    return let #'let' value replaces the function call in the main executing code

#--Main Executing Code-----------------------------------

#create empty lists to hold the file data

fName = []
lName = []
test1 = []
test2 = []
test3 = []

with open("textFiles/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnected from file -- can still access the stored data via the lists

#process the list data to calc an avg score for each student, and find a letter grade equivalent

numAvg = [] #will hold each student's numeric average of test scores
letAvg = [] #will hold each student's letter average of test scores

for i in range(0, len(fName)):

    #calculate average of current student
    a = (test1[i] + test2[i] + test3[i]) / 3
    #add average to numAvg list
    numAvg.append(a) #can also do: numAvg.append((test1[i] + test2[i] + test3[i]) / 3)

    l = letter(a) #return value of letter() stored to l
    letAvg.append(l)    #can also do: letAvg.append(letter(a))

#process the lists to display all student data back to the user
print(f"{'FNAME':10} {'LNAME':10} {'T1':3} {'T2':3} {'T3':3} {'# AVG':6} {'L AVG'}")
print("----------------------------------------------------------------------------")

for i in range(0, len(fName)):
    print(f"{fName[i]:10} {lName[i]:10} {test1[i]:3} {test2[i]:3} {test3[i]:3} {numAvg[i]:6.2f} {letAvg[i]}")

print("----------------------------------------------------------------------------")

print(f"There are {len(fName)} students in the file.")