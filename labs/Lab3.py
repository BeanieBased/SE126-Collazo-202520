#W4D1 - 1D & Parallel Lists
#Justyn Collazo
#SE126.02
#1-27-25 [W4D1]

#this file uses: voters_202040.csv

#Construct a program that will analyze potential voters. The program should generate the following totals:
#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.

#Variables

notEligible = 0
notRegistered = 0
eligibleNonVoters = 0
eligibleVoters = 0
recordsProcessed = 0
voterID = []
age = []
registered = []
voted = []

#Imports

import csv

#Functions

def countUP(value):
    # Increment a value by 1
    return value + 1


#Main Code

with open("textFiles/voters_202040.csv") as csvfile:
    #we must indent one level while "connected to the file"

    file = csv.reader(csvfile)

    for rec in file:
        #for every record in the file do the following
        #print(f"{rec[0]:10}\t{rec[1]:10}")
        
        
        #add the record data to its corresponding list
        #append --> to add to the end
        voterID.append(rec[0])
        age.append(int(rec[1]))
        registered.append(rec[2])
        voted.append(rec[3])
        
for i in range(0, len(voterID)):
    if age[i] < 18: #check age if they can vote
        notEligible = countUP(notEligible)
    elif registered[i] == 'N': #are they registered
        notRegistered = countUP(notRegistered)
    elif registered[i] == 'Y':
        if voted[i] == 'Y': #did they vote
            eligibleVoters = countUP(eligibleVoters)
        else:
            eligibleNonVoters = countUP(eligibleNonVoters)

#print!!
print("\nSummary:")
print("Number of individuals not eligible to register:", notEligible)
print("Number of individuals old enough to vote but not registered:", notRegistered)
print("Number of individuals eligible to vote but did not vote:", eligibleNonVoters)
print("Number of individuals who did vote:", eligibleVoters)
print("Total number of records processed:", len(voterID))
