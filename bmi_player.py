import os
def enter_input_to_calcluate_bmi():
    "This function gets the input from the user"  
   
    # Get the weight of the player
    weight_of_the_player=  float(input("Enter the weight of the user in kg"))
   
    # Get the height of the player
    height_of_the_player=  float(input("Enter the height of the user in meters"))
    
    return weight_of_the_player,height_of_the_player
def calculate_bmi(weight_of_the_player,height_of_the_player):
    bmi_of_the_player = round(weight_of_the_player/(height_of_the_player * 2),1)
    return bmi_of_the_player
def catogory_of_the_player(body_mass_index):
    if body_mass_index <= 18.5:
         print("The user is considered as underweight")
    elif body_mass_index > 18.5 and body_mass_index < 24.9:
         print("The user is considered as normal weight")
    elif body_mass_index > 25 and body_mass_index <= 29.9:
        print("The user is considered as overweight")
    elif body_mass_index >=30:
        print("The user is considered as obese")
def compare_user_bmi_with_player_csv(bmi_value):
    # To read the CSV file we have to join the path where it's located   
    filename = os.path.abspath(os.path.join('..',"all_players_data.csv"))
    matched_player = []    
    with open(filename,"r") as fp:
        all_lines = fp.readlines()              

        for each_line in all_lines:            

            # Fetch the player name from the file           

            player_name = each_line.split(',')[0]                       

            # Fetch the player BMI from the file          

            player_bmi = each_line.split(',')[-1].split('\n')[0]            

            # Checks player BMI and user BMI are equal 

            if float(player_bmi) == bmi_value:

                matched_player.append({player_name:player_bmi})

                         

        if not matched_player:

            print("Your BMI is not matching with any of the players dataset which is used here")

        else:

            print("Your BMI is matching with")

            print ("matched_player") 

       

# Program starts here

if __name__ == "__main__":

    # This calling function gets the input from the user

    weight_of_the_user,height_of_the_user = enter_input_to_calcluate_bmi()
    

    # This calling function calculates the BMI of the user

    bmi_value = calculate_bmi(weight_of_the_user,height_of_the_user)

    print("BMI of the user is :", bmi_value)



    # This function is used to calculate the user's criteria

    catogory_of_the_player(bmi_value)



    # This function is used to read the csv file and compare the BMI value

    compare_user_bmi_with_player_csv(bmi_value)  