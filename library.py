# constants
POKENUM = 10    # number of pokemon that is currently entered in the database

# pokemon table insert command
PTI = """INSERT INTO pokemon (dex_num, poke_name, type_1, type_2, type_combo_num)
    VALUES
    (1, "Bulbasaur", "grass", "poison", 60),
    (2, "Ivysaur", "grass", "poison", 60),
    (3, "Venusaur", "grass", "poison", 60),
    (4, "Charmander", "fire", NULL, 127),
    (5, "Charmeleon", "fire", NULL, 127),
    (6, "Charizard", "fire", "flying", 43),
    (7, "Squirtle", "water", NULL, 136),
    (8, "Wartortle", "water", NULL, 136),
    (9, "Blastoise", "water", NULL, 136),
    (10, "Caterpie", "bug", NULL, 94)"""

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