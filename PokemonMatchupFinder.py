# IMPORTANT
# DO NOT FORGET TO START MYSQL SERVER
# imports
import mysql.connector
from mysql.connector import Error
import library as li
# Pandas issue: Might not be needed, will ignore for now
# import pandas as pd

# test database connection
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

print(li.PW)

connection = create_server_connection("localhost", "root", li.PW)