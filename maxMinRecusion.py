#Take an arrary "arr" 
def findMax(arr):
    #If the amount in the array is one, your min and max are both the array[0]
    if len(arr)== 1:
        max =arr[0]
    else:
        recurMax =findMax(arr[1:])
        
        #If the first number is greater than the second, your max because the first and the min becomes the second.
        #Recursively call the min
        if arr[0]> recurMax:
            max = arr[0]

        #If the first number is less than the second, your max because the second and the min becomes the first.
        #Recursively call the min
        else:
            max =recurMax 
    return max
    
max =findMax([3,12, 18,6])
print("The max is {}".format(max))