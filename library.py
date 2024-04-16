# constants
POKENUM = 10    # number of pokemon that is currently entered in the database
POKEDB = "PokemonTypeDatabase" # name of pokemon database

# Function: bin_search
# Parameters: arr - array to be search through, from sqlite3 database
#             tar - what to be searched for in database
# Desc: Binary search used to look through sorted data. Will return the location of the data, -1 means it was not found 
def bin_search(arr, tar):
    # high and low pointers
    low = 0
    high = int(len(arr) - 1)

    try:
        # binary search
        # repeats until high and low meet
        while low <= high:
            # finds mid point of array
            mid = low + (high - low) // 2
            # if target is at current midpoint, return index or target
            if arr[mid] == tar:
                    return mid
                
            # the mid point is less than the target, target must be in upper half of array
            elif arr[mid] < tar:
                low = mid + 1

            # the mid point is more than the target, target must be in lower half of array
            else:
                high = mid - 1

    # error with binary search, pokemon was not in list
    except:
         return - 1

        
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