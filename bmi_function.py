def main():
    bmi_intro()
    

#define variables
get_height = 0.0
get_weight = 0.0
body_mass_index = 0.0


#We will start with the introduction to our program
def bmi_intro():
    print("Welcome to my BMI calculator!")
   

#From this point I will ask the user for his/her information.

get_height = float(input("Please enter your height in inches. "))
get_weight = float(input("Please enter your weight in pounds. "))
#user will enter there information above and we will then calcualte.
body_mass_index = (get_weight) / (get_height ** 2)

if body_mass_index < 18.5:
    print("Aperson with a BMI of is underwieght ")
elif body_mass_index < 24.9:
    print(" person with a BMI of is normal weight ")
else:
    print(" person with a BMI of is overweight ")