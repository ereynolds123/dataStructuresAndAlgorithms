# Takes an array 
def listSum(numList):
    #If array is 1 number long, return the value which is the total sum of the array
    if len(numList)==1:
        return numList[0]
    #Otherwise, return the first value and recursively call for the second value in the array. 
    else:
        return numList[0]+ listSum(numList[1:])
    
print(listSum([1,3,5, 7,9]))