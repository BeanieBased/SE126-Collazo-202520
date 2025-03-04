#Justyn Collazo
#Lab 7
#3/3/25

#Program Prompt
#Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and
#the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a
#user to interact with the dictionary based on the following menu

#--Imports---------------

import csv

#--Dictionary------------

ans = "y"
words = {}

#--Main Code-------------

print("Welcome to my programming dictionary program!")

with open ("textFiles/words.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        words.update({rec[0] : rec[1]})

#disconnect from file

while ans == "y": #Menu will always show up after you do something
    print("\t--Menu--\n1. Show all words\n2. Search for a word\n3. Add a word\n4. EXIT") #Menu
    menuAnswer = input("\nWhich option would you like to pick? [1-4]: ") #What Option

    while menuAnswer not in ["1", "2", "3", "4"]: #If they don't pick 1-4
        print("INVALID INPUT! Try again!")
        menuAnswer = input("\nWhich option would you like to pick? [1-4]: ")
    
    if menuAnswer == "1": #Show all words and defintions
        print("\n\nShowing all words...\n\n")
        print(f"{'WORD':10}\t{'DEFINITION'}")
        print("-" * 50)
        for key in words:
            #for every key (and value) pair found within the 'words' dictionary
            print(f"{key:10}\t{words[key]}")
        print("-" * 50)
    elif menuAnswer == "2": #Sequential Search for a word!!

        search = input("\n\nWhat word are you searching for?: ")
        found = 0

        for key in words:
            if search.lower() == key.lower():
                #store the found title's location in the dictionary -->
                found = key

        if found != 0:
            print(f"\nWORD: {found:10}\nDEFINITION: {words[found]}\n")
        else:
            print(f"\nYour search for {search} came up empty! Sorry!\n")

    elif menuAnswer == "3": #Add a word
        newWord = input("What would you like the new word to be?: ")
        if newWord in words:
            print("This word is already in the dictionary!")
        else:
            newDef = input("What is the definition of the new word?: ")
            words[newWord] = newDef

            print("Word added to the dictionary!")
            
            with open("textFiles/updated_words.csv", "w", newline="") as csvfile: #I couldn't find the program we originally used so I had to google how to do this lol
                writer = csv.writer(csvfile)
                for key, value in words.items():
                    writer.writerow([key, value])
        
    elif menuAnswer == "4": #Exiting
        print("Thank you for using my program! Have a good day!")
        ans = "n"