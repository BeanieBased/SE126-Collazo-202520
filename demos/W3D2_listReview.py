#W3D2 - List Review 1Dimensional Lists & Parallel Lists

#this file uses: class_grades.csv



#--Imports------------------------------------

import csv

#--Functions----------------------------------



#--Main Code----------------------------------

totalRecords = 0

with open("textFiles/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)
    
    #create a list for every potential field
    firstName = []
    lastName = []
    test1 = []
    test2 = []
    test3 = []

    for rec in file:
        #for every record in the file do the following
        #print(f"{rec[0]:10}\t{rec[1]:10}")
        
        
        #add the record data to its corresponding list
        #append --> to add to the end
        firstName.append(rec[0])
        lastName.append(rec[1])

        test1.append(int(rec[2])) #cast as intenger for easier maths later
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#DISCONNECT FROM FILE -- all file data is retained because we are using lists

#basic processing - use the 1D parallel lists to print all data to the console
#print(f"INDEX {'#':3} : {'FIRST':10} {'LAST':10} {'T1':3} {'T2':3} {'T3':3}")
#print("-------------------------------------------------------------------")
#for index in range(0, len(firstName)): #len() --> length of collection, returns # of items
    #index --> key of the list, allows access to ONE specific value
#    print(f"INDEX {index:3} : {firstName[index]:10} {lastName[index]:10} {test1[index]:3} {test2[index]:3} {test3[index]:3}")
#print("-------------------------------------------------------------------")

#create a NEW list to hold each student's test score average
avg = []

#process the current student data to find and store each student's test score avg to the avg list
for i in range(0, len(test1)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)
    #could also: avg.append((test1[i] + test2[i] + test3[i]) / 3)

print(f"INDEX {'#':3} : {'FIRST':10} {'LAST':10} {'T1':3} {'T2':3} {'T3':3} {'AVG':3}")
print("-------------------------------------------------------------------")
for index in range(0, len(firstName)): #len() --> length of collection, returns # of items
    #index --> key of the list, allows access to ONE specific value
    print(f"INDEX {index:3} : {firstName[index]:10} {lastName[index]:10} {test1[index]:3} {test2[index]:3} {test3[index]:3} {avg[index]:3.2f}")
print("-------------------------------------------------------------------")

#find current average of class by processing the avg list data

totalAvg = 0

for i in range(0, len(avg)):
    totalAvg += avg[i] #adds each avg value to the to the total value

#calculte the average
classAvg = totalAvg / len(avg)
print(f"\nThe CLASS AVERAGE of these {len(avg)} students is: {classAvg:.2f}")