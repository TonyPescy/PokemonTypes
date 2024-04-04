# ALL DATABASE FUNCTIONS WILL BE CREATED IN DatabaseFunctions.py

# imports
import sqlite3
from sqlite3 import Error
import library as lib

# Function: create_connection
# Parameters: db_file - Database file
#             user_list - Pokemon nums/names entered by user
#             case - nums that determine which case the function will use
#                   1 - first run with user inputs
# Desc: Creates a connection to the SQLite database
def create_connection(db_file, user_list, case):

    # if case == 0: # initial case
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            cur = conn.cursor()

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

    pokenames_lst = []
    data = cur.execute("""SELECT poke_name FROM pokemon ORDER BY poke_name;""")    # command gets pokemon nnames and orders them in alphabetical order for binary search
    for row in data:
        fixed_row = str(row).replace("('", "")
        fixed_row = str(fixed_row).replace("',)", "")
        pokenames_lst.append(str(fixed_row))

    # case where user entered the names instead of national dex number
    if case == 1:

        for pokemon in user_list:
            found = lib.bin_search(pokenames_lst, 0, len(pokenames_lst)-1, pokemon.lower())
            if found == -1:     # pokemon was not found
                print("Pokemon \"" + pokemon + "\" was not found, continuing with other pokemon entered...")
                return found
            else:   # pokemon was found
                print("Pokemon \"" + pokemon + "\" was found, continuing with other pokemon entered...")
                return found

    # conn.close()
