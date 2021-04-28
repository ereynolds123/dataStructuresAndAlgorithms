#This program is a GPA calculator for my final Data Structures course

#Accumulator variable for grades
total_grades= 0

#Add all grades to dictionary.
#The first item of the key pair is the grade percentage, the second item is the possible total points
grades_list = {98:15, 45:10, 89:50}

def GPAcalculate(accumulator_Variable, dictionary):
    for key, value in dictionary.items():
        totalPoints = key * (value/100)
        print(totalPoints)
        
GPAcalculate(total_grades, grades_list)
    
    