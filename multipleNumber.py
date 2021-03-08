"""A program to determine if an integer is a multiple of another integer"""

#Get user inputs for integer and multiples
n = int(input("Enter a number : "))
m = int(input("Enter a number to determine if previous number is an integer : "))


#Function takes two arguments, an integer and a multiple. If the integer divided by the multiple
# has a remainder of 0, it is a multiple and print true.
#Otherwise print false.
def is_multiple(n, m):
    if n % m==0:
        print("True")
    else:
        print("False")
        
is_multiple(n, m)