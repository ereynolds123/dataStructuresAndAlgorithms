import random

choices ="abcdefghijklmnopqrstuvwxyz012345678ABCDEFGHIJKLMNOPOQRSTUVWXYZ!@#$%^&*()?"
passwordLen= 8
password ="".join(random.sample(choices, passwordLen))

print(password)
