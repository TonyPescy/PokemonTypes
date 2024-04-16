# ALL I/O FUNCTIONS ARE CREATED IN InputOutput.py

# imports
import library as lib
import DatabaseFunctions as df

# Function: user_prompt
# Parameters: 
# Desc: Prompts user for number of pokemon they wish to enter, the pokemon names/nation dex numbers, and 
def user_prompt():
    # first user input
    while True:
        valid_num = False
        cont = False

        # ask user for number of pokemon weaknesses to be found (1-6)
        try:
            while valid_num == False:
                num_of_pokemon = int(input("How many pokemon would you like to know the weaknesses for? (max 6) "))
                
                if (num_of_pokemon < 1) or (num_of_pokemon > 6):  # checks for invalid number
                    valid_num = False
                    print("Please choose a number between and including 1 through 6.")
                else:   # valid number was entered
                    cont = True
                    valid_num = True
        except ValueError or TypeError as e:
            print(e)
        if cont == True:
            break

    # second user input
    while True:
        # ask for name of pokemon they wish to know the weakness of
        # adds all names entered to a list
        try:
            pokemon_list = []
            for i in range(num_of_pokemon):
                pokemon_list.append(str(input("Please enter the name of the pokemon you wish to know the weakness of: ")))
        except ValueError as e:
            print(e)
        except IOError as e:
            print(e)

        df.create_connection()