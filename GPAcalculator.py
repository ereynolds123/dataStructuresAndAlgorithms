#This program is a GPA calculator for my final Data Structures course

#Accumulator variable for grades
#totalGrades= 0

#Add all grades to dictionary.
#The first item of the key pair is the grade percentage, the second item is the possible total points
gradesList = {98:15, 45:10, 89:50}

#Function takes the accumulator variable and a dictionary
#Calculates the total points of each pair
#
def GPA_calculate( dictionary):
    
    #Loops through the dictionary to get the key and value of the key pair
    #Calculates the amount of earned points
    for key, value in dictionary.items():
        totalEarnedPoints = key * (value/100)
    
    print(totalEarnedPoints)
    
    #Finds the total potential grade points
    totalPotentialPoints = 0
    for value in dictionary.values():
        totalPotentialPoints = totalPotentialPoints +value
    
    print(totalPotentialPoints)
    
    totalGPA = (totalEarnedPoints/totalPotentialPoints) * 100
    print(totalGPA)
        
GPA_calculate( gradesList)

    
    