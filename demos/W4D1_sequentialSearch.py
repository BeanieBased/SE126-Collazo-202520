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

print("\n\nWelcome to the Student Search Program!\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":

    #get search type from user
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by LETTER GRADE")
    print("3. EXIT")

    searchType = input("Enter your search type: [1-3]: ")
    
    if searchType == "1":
        print("\tSEARCH BY LAST NAME")

        found = -1 #invalid index number, will use to check later to see if a student has been found

        #get search item from user
        searchName = input("Enter the LAST NAME of the student you are searching for: ")

        #perform search
        for i in range(0 , len(lName)):
        #the FOR LOOP allows for the "sequence" part -> from beginning to end
            if searchName.lower() == lName[i].lower():
                #the IF STATEMENT allows for the "search" part
                found = i #make found the current index ,can be used later to display

    #display results
        if found != -1:
            #last name has been found! display data!
            print(f"{fName[found]:10} {lName[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {numAvg[found]:6.2f} {letAvg[found]}")
        else:
            print(f"Your search for {searchName} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program - check your spelling and casing and try again.")

    elif searchType == "2":
        print("SEARCH BY LETTER GRADE")
        found = [] #creates empty list to gather and store index values

        #get search item from user
        searchGrade = input("Enter the LETTER GRADE of the students you are searching for: ")

        #perform search
        for i in range(0, len(letAvg)):
            #the FOR LOOP allows for the "sequence" part -> from beginning to end
            if searchGrade.upper() == letAvg[i]:
                #the IF STATEMENT allows for the "search" part
                found.append(i) #add the current index (found), can be used later to display

        #display results 
        if not found: #list is empty
            print(f"Your search for {searchGrade} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program - check your spelling and casing and try again.")

        else:
            print(f"Your search for {searchGrade} was FOUND!")

            #found is a list with multiple pieces of data - must use a FOR LOOP to see all
            for i in range(0, len(found)):
                print(f"{fName[found[i]]:10} {lName[found[i]]:10} {test1[found[i]]:3} {test2[found[i]]:3} {test3[found[i]]:3} {numAvg[found[i]]:6.2f} {letAvg[found[i]]}")
              
    elif searchType == "3":
        answer = "n"
        print("Exiting...")
    #build a way out of the loop
    if searchType == "1" or searchType == "2": # only when user doesn't say 3
        answer = input("Would you like to search again?")