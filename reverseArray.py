#Take an array and reverse the array
def reverse(arr):
    fragment = ""
    #First base case
    if len(arr)==0:
        return []
    
    elif len(arr)==1:
        return arr[0]
    
    elif len(arr) > 1:
        reverseFragment = reverse(arr[1:])
        fragment = str(reverseFragment) + " " + str(arr[0])
        return fragment
    
print(reverse([45, 56, 77, 98]))