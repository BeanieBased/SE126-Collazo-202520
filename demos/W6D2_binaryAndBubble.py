#W6D2 - Binary Search + Bubble Sot

#this file uses party.csv

#PROGRAM PROMPT: build a repeatable, menu driven program to access and search for data within the file


#--Imports--------------

import csv


#--Functions-----------------------

def display(x, foundList, records):

    print(f"{'CLASS':8} {'NAME':10} {'MEANING':25} {'CULTURE'}")
    print("------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{classType[x]:8} {name[x]:10} {meaning[x]:25} {culture[x]}")

    elif foundList:
        for i in range(0, records):
            print(f"{classType[foundList[i]]:8} {name[foundList[i]]:10} {meaning[foundList[i]]:25} {culture[foundList[i]]}")

    else:
        #printint multiples, based on length stored in 'records'
        for i in range(0,records):
            print(f"{classType[i]:8} {name[i]:10} {meaning[i]:25} {culture[i]}")


#--Main Code------------------------

classType = []
name = []
meaning = []
culture = []

practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]

with open ("textFiles\party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        classType.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])


display("x",0,len(classType)) #practice with function

ans = input("Would you like to enter the search program? [y/n]: ").lower()

while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]: ").lower()

#main search loop

while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by TYPE") #shows all elf or dragon 
    print("2. Search by NAME") #binary search review
    print("3. Search by MEANING") #find a part of a whole
    print("4. EXIT")

    searchType = input("\nHow would you like to search today? [1-4]: ")
    
    #using 'not in' for user validity checks
    if searchType not in ["1", "2", "3", "4"]:
        print("***INVALID ENTRY!***\nPlease try again")

    elif searchType == "1":
        print(f"You have chosen Menu Option #{searchType}")


        search = input("Which type: 'dragon or 'elf': ").lower()
        

        if search not in ["dragon", "elf"]:
            #could also be if search.title() not in class type
            print("***INVALID ENTRY!***\nPlease try again")
        else:
            found = []
            for i in range(0, len(classType)):
                if search.lower() == classType[i].lower():
                    found.append(i)

            if not found:
                print(f"Sorry, your search could not be completed :[")

            else:
                print(f"Your search for {search} is complete! Details below:")
                display("x", found, len(classType))



