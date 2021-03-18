import sys

user1 = input("What is your name? ")
user2 = input("And what's your name? ")

user1_answer = input("%s, do you want to choose rock, paper or scissors?" %user1)
user2_answer = input ("%s, do you want to choose rock, paper or scissors?" %user2)

def compare (u1, u2):
    if u1== u2:
        return("It's a tie")
        
    elif user1 =="paper":
        if user2 == rock:
            print(user1, "you win")
            
print(compare(user1_answer, user2_answer))