#Python program to bubble sort a list of values
def bubbleSort(unsortedList):
    #Get the length of your array
    indexedLength = len(unsortedList)-1
    sortedList =False
    
    #Use a while loop to sort the array where the first index is checked against the second until all values are sorted
    while not sortedList:
        for i in range(0, indexedLength):
            if unsortedList[i]> unsortedList[i+1]:
                sortedList =False
                unsortedList[i], unsortedList[i+1]= unsortedList[i+1], unsortedList[i]
            else:
                 sortedList=True
        return unsortedList
                
        
print(bubbleSort([3, 2, 9, 7, 8, 4]))


#https://www.screencast.com/t/42T51KufqIV