

n = int(input("Enter a number : "))
m = int(input("Enter a number to determine if previous number is an integer : "))


def is_multiple(n, m):
    if n % m==0:
        print("True")
    else:
        print("False")
        
is_multiple(n, m)