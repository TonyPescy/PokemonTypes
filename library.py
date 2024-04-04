# constants
POKENUM = 10    # number of pokemon that is currently entered in the database
POKEDB = "PokemonTypeDatabase" # name of pokemon database

# Function: bin_search
# Parameters: arr - array to be search through, from sqlite3 database
#             low - lowest in array
#             high - highest in array
#             x - what to be searched for in database
# Desc: Binary search used to look through sorted data. Will return the location of the data, -1 means it was not found 
def bin_search(arr, low, high, x):
    # base case
    while (low <= high):

        mid = low + (high // 2)

        if arr[mid]

        if (result == 0):
            return mid - 1
        
        # if x is larger ignore left side of arr
        elif (result > 0):
                low = mid + 1
        
        # if x is smaller, ignore right half of arr
        else:
            high = mid - 1
        
    else:
         return -1
# bin_search end


# pokemon table insert command
PTI = """INSERT INTO pokemon (dex_num, poke_name, type_1, type_2, type_combo_num)
    VALUES
    (1, "bulbasaur", "grass", "poison", 60),
    (2, "ivysaur", "grass", "poison", 60),
    (3, "venusaur", "grass", "poison", 60),
    (4, "charmander", "fire", NULL, 127),
    (5, "charmeleon", "fire", NULL, 127),
    (6, "charizard", "fire", "flying", 43),
    (7, "squirtle", "water", NULL, 136),
    (8, "wartortle", "water", NULL, 136),
    (9, "blastoise", "water", NULL, 136),
    (10, "caterpie", "bug", NULL, 94)"""

# pokemon table creation command
PTC = """CREATE TABLE IF NOT EXISTS pokemon (
        dex_num integer,
        poke_name tinytext NOT NULL UNIQUE,
        type_1 tinytext NOT NULL,
        type_2 tinytext,
        type_combo_num integer NOT NULL,
        PRIMARY KEY (dex_num)
    );"""

# type_combos table creation command
TCC = """CREATE TABLE IF NOT EXISTS type_combos (
    type_combo_num integer,
    type_combo_name tinytext NOT NULL UNIQUE,
    no_effect text,
    quad_weak text,
    weak text,
    strong text,
    quad_strong text,
    PRIMARY KEY (type_combo_num)
);"""

# type_combos table insert command
TCI = """INSERT INTO type_combos (type_combo_num, type_combo_name, no_effect, quad_weak, weak, strong, quad_strong)
    VALUES
        (1, "normal", "ghost", NULL, "fighting", NULL, NULL)"""