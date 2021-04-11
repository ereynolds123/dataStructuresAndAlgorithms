#Anagram analysis

#Sort by size of string
def anagramSolution(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    
    #Sort the lists 
    alist1.sort()
    alist2.sort()
    
    #Starting position
    pos =0
    matches = True
    
    #Check for matches if the length of the two strings is the same
    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos =pos + 1
            
        else:
            matches = False
            
    return matches

print(anagramSolution("abcde", "edcba"))