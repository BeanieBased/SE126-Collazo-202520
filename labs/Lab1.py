#Justyn Collazo, Lab 1 #, 1/13/25


#It is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity
#and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal
#to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program
#announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed
#to enter and check as many rooms as they would like without exiting the program.



#Variables

maxCap = 0
people = 0
response = ""
answer = ""

#Function

def difference(people, maxCap):
    
    seatsRemaining = maxCap - people
    if seatsRemaining >= 1:
        {
            print(f"There are {seatsRemaining} seats remaining.")
        }
    elif seatsRemaining < 0:
        {
            print(f"There are more than the allowed amount of people inside the room. You need to remove {seatsRemaining} people to meet fire regulations.")
        }
    else:
        {
            print("Perfect! The room is completely full. No spots left.")
        }
    return difference

def decision(response):
    '''this function asks a user if they'd like to continue the program, checks the response for validity, and then returns a valid response back to the main program.'''

    #while loop trap - ensure user provides valid value before moving on
    while response != "y" and response != "n":
        print("***INVALID ENTRY!***")

    return response

#Main Code

maxCap = int(input("What is the max capacity of the room? "))

people = int(input("How many people are going in? "))

print(difference(people, maxCap))

response = input("\t\tWould you like to check another room? [y/n]: ").lower()

answer = (decision)


