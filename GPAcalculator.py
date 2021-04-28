#This program is a GPA calculator for my final Data Structures course

import itertools

#Add all grades in one class to dictionary.
#The first item of the key pair is the grade percentage, the second item is the possible total points
gradesList = {98:15, 45:10, 89:50}
gradesListTwo ={97:20, 67:10, 91:50}



#List of all class GPAs
listOfGPAs = []

#Function takes the accumulator variable and a dictionary
#Calculates the total points of each pair
#Finds the total earned and potential points for the class
def GPA_calculate(dictionary):
    #List of the Potential earned points accumulator
    listOfEarnedPoints = []
    #Loops through the dictionary to get the key and value of the key pair
    #Calculates the amount of earned points
    for key, value in dictionary.items():
        totalEarnedPoints = (key/100) * value
        #Creates a list of potential earned points
        listOfEarnedPoints.append(totalEarnedPoints)
    
    sumOfEarnedPoints =sum(listOfEarnedPoints)
    
    print("This is the list of Earned Points", listOfEarnedPoints)
    print("Total Earned points", sumOfEarnedPoints)
    
    #Finds the total potential grade points
    totalPotentialPoints = 0
    for value in dictionary.values():
        totalPotentialPoints = totalPotentialPoints +value
    
    print("Total Potential points", totalPotentialPoints)
    
    #Gives the total GPA per class
    totalGPAForEachClass = (sumOfEarnedPoints/totalPotentialPoints) * 100
    print("Total GPA", totalGPAForEachClass)
    
    listOfGPAs.append(totalGPAForEachClass)
    print(listOfGPAs)


GPA_calculate( gradesList)
GPA_calculate(gradesListTwo)

    
    