"""
We will use this script to teach Python to absolute beginners
The script is an example of calulation of BMI in Python
The BMI calculator: 
BMI = (Weight)%(height*height)
"""
def read_weight_height():
    try:
        #enter the weight in kgs
        weight = float(input("enter the weight"))   
        #enter the height in meters
        height = float(input("enter the height"))  
         #handling the exceptions
    except ValueError:
        #if the entered value is a string
        raise ValueError('Weight and height must be pure numbers.')
    if weight <= 0 and height <=0:
        #if the weight is less than zero below exceptions will be exceuted
        raise ValueError('Cannot compute BMI for zero or negative weight')
    if weight >= 200 and height >=20 :
        #the  20height cannot  be above 20 meters and weight cannot be more than 200
        raise ValueError('cannot  be above 20 meters and weight cannot be more than 200')
    return (weight, height)

try:
    weight, height = read_weight_height()
except Exception:
 #formula to calculate the bmi
    bmi = weight/height*2
#if no exception occur then bmi will be printed
    print(bmi)