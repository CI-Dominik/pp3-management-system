# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

""" Import needed Python modules """

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

""" Load .env file to authenticate in database """

load_dotenv()

""" Set variables to access MySQL database """

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

""" Establish databse connection """

try:
    connection = mysql.connector.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass
    )

    """ Check if connection was successful """

    if connection.is_connected():
        print("Connection to database established.")

    """ Create cursor for usage with MySQL """

    cursor = connection.cursor()

    """ Print error if database connection was not successful """
    
except Error as e:
    
    print(f"ERROR CONNECTING TO DATABASE: {e}")