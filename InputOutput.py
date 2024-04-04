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
        # ask for national dex number or name of pokemon they wish to know the weakness of
        try:
            pokemon_list = []
            in_db_list = []     # list of entered pokemon that are in the database
            for i in range(num_of_pokemon):
                pokemon_list.append(str(input("Please enter the pokemon you wish to know the weakness of: ")))
        except ValueError as e:
            print(e)
        except IOError as e:
            print(e)

        for pokemon in pokemon_list:
            try:    # tries to see if pokemon was entered correctly
                pokemon = int(pokemon)      # converts number to be in proper format

                if (pokemon < 1) or (pokemon > lib.POKENUM):       # checks if number entered is a valid national dex number
                    print("Please enter a valid national dex number, we currently have up to national dex number " + lib.POKENUM + " on file.")

                else:   # pokemon entered was a valid national dex number
                    in_db_list.append(pokemon)  # adds pokemon that pass all checks to the in_db_list

            except ValueError:  # if pokemon entered was not entered using national dex number
                poke_list = []
                poke_list.append(pokemon)
                found = df.create_connection(lib.POKEDB, poke_list, 1)
                    
                # COMPARE TO ALL NAMES INSIDE DATABASE
                if found == -1: # if pokemon was not found, will trigger except as error
                    print("Please enter a pokemon that is within our database, we currently have up to national dex number " + lib.POKENUM + " on file.")
                else:
                    in_db_list.append(pokemon.lower())
                    


        # gets length of list of pokemon that are in the database
        pokemon_passed_num = len(in_db_list)
        print(pokemon_passed_num)
        print(in_db_list)
        return pokemon_passed_num