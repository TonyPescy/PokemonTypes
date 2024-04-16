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


    # case where user entered the names instead of national dex number
    if case == 1:

        # ordered list for binary search
        ordered_list = order_by_name(cur)
        # list to hold the index at which pokemon were found\
        ind_lst = []

        # searches for pokemon in ordered list one by one
        for i in range(user_list):
            # found is the index at which the pokemon was found
            found = lib.bin_search(ordered_list, user_list[i].lower())
            ind_lst.append(found)

            if found == -1:     # pokemon was not found
                print("Pokemon \"" + user_list[i] + "\" was not found, continuing with other pokemon entered...")

            else:   # pokemon was found
                print("Pokemon \"" + user_list[i] + "\" was found, continuing with other pokemon entered...")

        # PLAN: 
        # USING THE INDEX LIST WE WILL KNOW WHICH POKEMONS TO SKIP
        # THEN USING THE NAMES OF POKEMON THE USER INPUTTED WE WILL
        # SEARCH THE DATABASE AND GET THE TYPE_COMBO_NUMS OF THOSE POKEMON
        # THEN SEARCH THE TYPE_COMBO DATABASE AND RETURN THE TYPES THE POKEMON
        # WILL RESIST AND WILL BE WEAK TO TO
        return ind_lst

    # conn.close()

# Function: order_by_name
# Parameters: cursor - cursor being used in current connection
# Desc: creates a list of all pokemon names that are alphabetical order for binary search
# Returns: ordered lost of pokemon
def order_by_name(cursor):
    # list to hold pokemon names in order
    pokenames_lst = []
    data = cursor.execute("""SELECT poke_name FROM pokemon ORDER BY poke_name;""")    # command gets pokemon nnames and orders them in alphabetical order for binary search
    # cleans up all of the pokemon names so that they can be compared in binary search
    for row in data:
        fixed_row = str(row).replace("('", "")
        fixed_row = str(fixed_row).replace("',)", "")
        pokenames_lst.append(str(fixed_row))
    
    return pokenames_lst