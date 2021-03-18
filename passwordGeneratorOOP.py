import string
import random

def pwgen(size=8, chars = string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.choice(chars) for _ in range(size))

print(pwgen (int(input("How many characters are in your password?"))))
    