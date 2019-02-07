"""
We will use this script to teach Python to absolute beginners
The script is an example of calulation of BMI in Python
The BMI calculator: 
BMI = (Weight)%(height*height)
"""


#Enter the weight of the User
print("Enter the weight in KGs")

#raw_input gets the input of kyboard through the user
weight=float(input())

#Enter the height of  the User
print("Enter the height Meters")

#raw_input gets the input of kyboard through the user
height=float(input())

#BMI of the USer is
bmi = weight / (height*height)
print("BMI of the user",bmi)