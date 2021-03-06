"""Program that calculates if a number is odd or even"""

num =int(input("Enter a number : "))
mod = num % 2

if mod > 0:
    print("Number is odd")
else:
    print("Number is even.")