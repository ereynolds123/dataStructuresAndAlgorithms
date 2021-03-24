#Take an arrary "arr". Return min and max of the array using recursion    
def findMinMax(arr):
    #Base case
    if len(arr)== 1:
        min = arr[0]
        max =arr[0]
        
  
    else:
        #Calculate the min, max of the remainder of the array. 
        recurMin, recurMax =findMinMax(arr[1:])
        

        #Calculate the min
        if arr[0]< recurMin:
            min = arr[0]
        else:
            min =recurMin
            
        #Calculate the max    
        if arr[0]> recurMax:
            max = arr[0]
        else:
            max =recurMax
            
    return min, max

#Print the min, max of the list
min, max =findMinMax([3, 2, 4, 6,8 ])
print("The min is {}, the max is {}".format(min, max))