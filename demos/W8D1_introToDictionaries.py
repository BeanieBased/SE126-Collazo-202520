#W8D1 - Introduction to Dictionaries

#Dictionaries in Python are a collection set similar to associate arrays in JavaScript but also look similar to JS object builds. Most importantly, they store data in key
#and value pairs. The keys are referred to as properties and the values can be any data type.



#--Imports----------------

#--Main Executing Code-------------

#start by creating a populated dictionary
myCar = {
    #'key' : value,
    "make": "Ford",
    "model": "SE Hatchback",
    "year": 2014,
    "name": "Gwendoline",
    "color": "black",
    #keys cannot be repeated/NO DUPLICATES allowed (within the same only)
}

yourCar = {
    #'key' : value,
    "make": "GMC",
    "model": "Canyon",
    "year": 2019,
    "name": "Jolly",
    "color": "black",
    "friends": ["Ray", "Matt", "Duncan"]
}
#display the entire dictionary -> 'myCar'
print(myCar)

#display just the 'make' and 'model' values of the dictionary 'myCar'

#dictionaryName
#"keyName" will always be a STRING index, created by developer
print(f"My car is a {myCar["make"]} {myCar["model"]}")

print(f"Rob's car is a {yourCar["make"]} {yourCar["model"]}")
print(f"{yourCar["friends"][2]}")

for key in yourCar:
    print(f"{key.upper() : {yourCar[key]}}")