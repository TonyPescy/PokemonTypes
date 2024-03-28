# imports
import sqlite3
from sqlite3 import Error
import library as lib

# Function: create_connection
# Parameters: db_file - Database file
# Desc: Creates a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS pokemon")
            cur.execute("DROP TABLE IF EXISTS type_combos")

            # create pokemon table
            try:
                cur.execute(lib.PTC)
            except Error as e:
                print(e)

            # insert pokemon into pokemon table
            try:
                cur.execute(lib.PTI)
            except Error as e:
                print(e)
            
            # create type_combos table
            try:
                cur.execute(lib.TCC)
            except Error as e:
                print(e)

            # insert type_combos into table
            try:
                cur.execute(lib.TCI)
            except Error as e:
                print(e)

            #data = cur.execute("""SELECT * FROM pokemon""")

            #for row in data:
            #    print(row)
            conn.close()

def user_prompt():
    # first user input
    while True:
        # ask user for number of pokemon weaknesses to be found (1-6)
        try:
            num_of_pokemon = int(input("How many pokemon would you like to know the weaknesses for? (max 6) "))
            break
        except ValueError as e:
            print(e)
        except (1 > num_of_pokemon > 6):
            print("Please choose a number between and including 1 through 6.")
        
    # second user input
    while True:
        # ask for pokedex number or name of pokemon they wish to know the weakness of
        try:
            pokemon_list = []
            for i in range(num_of_pokemon):
                pokemon_list.append(str(input("Please enter the pokemon you wish to know the weakness of: ")))
        except ValueError as e:
            print(e)

        for i in pokemon_list:
            try:
                int(i)
                # CHECK AGAINST ALL POKEMON NAMES IN THE DATABASE
            except ValueError:  # if pokemon entered was entered with national dex number
                if (1 > i > lib.POKENUM):
                    print("Please enter a valid national dex number, we currently have up to " + lib.POKENUM + " on file.")
                else:
                    continue
            


if __name__ == '__main__':
    create_connection(r"PokemonTypeDatabase")
