"""
We will use this script to teach Python to absolute beginners
The script we help u to identify the palindrome 
"""
#Enter the the word
n=int(input("Enter number:"))
#store value of n in temp var
temp=n
rev=0
while(n>0):
    number=n%10
    rev=rev*10+number
    n=n//10
if(temp==rev):
    
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
