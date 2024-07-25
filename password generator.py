import random

print("Welcome to your password generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$*-0123456789"
number = input("Input amount of passwords to generate: ")
number = int(number)
length = input("Input your password length: ")
length = int(length)

print("Here are your passwords: ")

for pwd in range(number):
    passwords = " "
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)



