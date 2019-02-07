"""
We will use this script to teach Python to absolute beginners
The script is an example of of guessing number

"""
import random

secret_number   =   random.randint(1,100)

print(secret_number)

gussed_number    = int(input("enter guess number"))

if(gussed_number    ==   secret_number):
    print("yes,you are right")

elif(gussed_number < secret_number):
    print("you are wrong, It is lesser than the secret number")

else:
    print(" you are wrong, guess number is greater than secret number")