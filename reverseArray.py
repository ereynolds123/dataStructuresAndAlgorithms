#Take an array and reverse the array
def reverse(arr):
    fragment = ""
    #First base case if there is nothing in the array
    if len(arr)==0:
        return []
    
    #Second base case if array has one item
    elif len(arr)==1:
        return arr[0]
    
    #Recursively adds the final element of the fragment to the reversed fragment
    #Turn fragment into a string to allow concatenation
    elif len(arr) > 1:
        reverseFragment = reverse(arr[1:])
        fragment = str(reverseFragment) + " " + str(arr[0])
        return fragment
    
print(reverse([45, 56, 77, 98]))