#A python program to do an insertion sort
#Compare the first number to the rest of the list

def insertionSort(arr):
    #Find the length of the array
    indexLen = range(1, len(arr))
    
    #For every value
    for i in indexLen:
        valueToSort = arr[i]
        
        #If value at the next position is higher than the value to sort, switch position
        while arr[i-1]> valueToSort and i> 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            #Step down the list to compare. Get value to sort, compare to item to the left, check next item
            i = i-1
            
    return arr

print(insertionSort([1, 5, 4, 2, 7]))

#https://www.screencast.com/t/OTnyHRszka