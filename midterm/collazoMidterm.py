#Justyn Collazo
#SE126.02
#W5D2 - Midterm! (Choice 3)
#2-4-2025 [W5D2]


#Program Prompt: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have
#been fully populated with file data, create a new list to hold a student ID value for each student. The first
#student in the file should have an ID of 10001, each student’s ID should be unique, and the ID values
#should not exceed 10021. Once the new list is populated, process through the five lists to display all of
#the student data to the user as well as the total number of records in the file.
#Once all of the data has been displayed, write all of the list data to a new file called
#‘midterm_choice3.csv’, where each student’s information is found on one record in the file and their
#data is separated by a comma (additional empty line in resulting file is okay).
#Finally, create a sequential search program that allows a user to repeatedly search the student database information stored in the lists 

#Imports

import csv

#Variables

fName = []
lName = []
department = []
gpa = []
studentID = []
idNum = 10000
totalStudents = 0
#Main Code


#connected to file

with open ("textFiles/midterm/students.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        department.append(rec[2])
        gpa.append(rec[3])
        idNum += 1
        studentID.append(idNum)
        totalStudents += 1

#disconnected from file

#display all records
print(f"{'FIRST':10} {'LAST':15} {'DEPARTMENT':15} {'GPA':15} {'STUDENT ID':3}")
print("----------------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:10} {lName[i]:15} {department[i]:15} {gpa[i]:15} {studentID[i]:3}")
print("----------------------------------------------------------------------------")
print(f"There are {totalStudents} student records total.")
        
#WRITE SOME DATA TO A NEW FILE
#create and write all of the data to a new text file:
file = open('textFiles/midterm/midterm_choice3.csv', 'w')

for i in range(0,len(fName)):
    file.write(f"{fName[i]},{lName[i]},{department[i]},{gpa[i]},{studentID[i]}\n")

file.close()



print("\n\nWelcome to the Student Search Program!\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":

    #get search type from user
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by DEPARTMENT")
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
            print(f"Your search for {searchName} has been found!")
            print(f"{'FIRST':10} {'LAST':15} {'DEPARTMENT':15} {'GPA':15} {'STUDENT ID':3}")
            print("----------------------------------------------------------------------------")
            print(f"{fName[found]:10} {lName[found]:15} {department[found]:15} {gpa[found]:15} {studentID[found]:3}")
        else:
            print(f"Your search for {searchName} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program - check your spelling and casing and try again.")

    elif searchType == "2":
        print("SEARCH BY DEPARTMENT")
        found = [] #creates empty list to gather and store index values

        #get search item from user
        print("---------------------------------")
        print("List of Departments:\nERD\nGMW\nIT\nNUR\nDMP")
        print("---------------------------------")
        searchDep = input("Enter the DEPARTMENT of the students you are searching for: ")

        #perform search
        for i in range(0, len(department)):
            #the FOR LOOP allows for the "sequence" part -> from beginning to end
            if searchDep.upper() == department[i]:
                #the IF STATEMENT allows for the "search" part
                found.append(i) #add the current index (found), can be used later to display

        #display results 
        if not found: #list is empty
            print(f"Your search for {searchDep} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program - check your spelling and casing and try again.")

        else:
            print(f"Your search for {searchDep} was FOUND!")

            #found is a list with multiple pieces of data - must use a FOR LOOP to see all
            print(f"{'FIRST':10} {'LAST':15} {'DEPARTMENT':15} {'GPA':15} {'STUDENT ID':3}")
            print("----------------------------------------------------------------------------")
            for i in range(0, len(found)):
                print(f"{fName[found[i]]:10} {lName[found[i]]:15} {department[found[i]]:15} {gpa[found[i]]:15} {studentID[found[i]]:3}")
              
    elif searchType == "3":
        answer = "n"
        print("Exiting...")
    #build a way out of the loop
    if searchType == "1" or searchType == "2": # only when user doesn't say 3
        answer = input("Would you like to search again? ")