#A python program to do a selection sort
def selection_sort(unsortedList):
    #Find the index length
    indexing_length = range(0, len(unsortedList)-1)
    
    #Find the lowest value in the array
    for firstNumber in indexing_length:
        min_value = firstNumber
        
        #Search through the rest of the array for the the lowest value
        for secondNumber in range(firstNumber+1, len(unsortedList)):
            if unsortedList[secondNumber] <unsortedList[min_value]:
                min_value = secondNumber

        #Swap higher values for lower values
        if min_value != firstNumber:
            unsortedList[min_value], unsortedList[firstNumber] = unsortedList[firstNumber] , unsortedList[min_value]
    
    return unsortedList

print(selection_sort([7,8,9,8,7,6,5,6,7,8,9,0]))
