#Searches the input array "arr" for specified value "val"
def binary_search(arr, val):
    #Checks that the arr is not 0 or 1 and incorrect value
    if len(arr)== 0 or (len(arr)==1 and arr[0]!=val):
        return False
    
    #Value of the middle of the array
    mid = arr[len(arr)//2]
    
    #Found a match
    if val ==mid:
        return True
    #Return the mid point of the first half of the array
    if val < mid:
        return binary_search(arr[:len(arr)//2], val)
    
    if val > mid:
        return binary_search(arr[len(arr)//2+ 1:], val)

a= [1,2,3,4,5,6,7,8,9]
print(binary_search(a,10))