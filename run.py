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

    """ Create cursor for usage with MySQL """

    cursor = connection.cursor(dictionary=True)

    """ Print error if database connection was not successful """
    
except Error as e:
    
    print(f"ERROR CONNECTING TO DATABASE: {e}")

def main_menu():

    """ Function to show the Main Menu of the system and get a choice for the next move """
    
    print("Welcome to Happy Life's Management System\n")
    print("")

    """ Display the Main Menu """

    while True:

        print("+------- MAIN MENU -------+")
        print("|                         |")
        print("| 1. Customer Management  |")
        print("| 2. Bookings / Tables    |")
        print("| 3. Sales / Carts        |")
        print("| 4. Returns              |")
        print("| 5. Products             |")
        print("|                         |")
        print("---------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            main_input = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please enter a number.\n")
            continue

        if(main_input == 1):
            print("")
            customer_management_menu()
            break

        elif(main_input == 2):
            print(f"Your input was {main_input}\n")

        elif(main_input == 3):
            print(f"Your input was {main_input}\n")

        elif(main_input == 4):
            print(f"Your input was {main_input}\n")

        elif(main_input == 5):
            print(f"Your input was {main_input}\n")
        
        else:
            print("Please insert a valid number.\n")

def customer_management_menu():

    """ Display the Customer Management Menu """

    print("You entered the Customers Management System.\n")
    print("")

    while True:

        print("+------- CUSTOMERS -------+")
        print("|                         |")
        print("| 1. Search Customer      |")
        print("| 2. Add new Customer     |")
        print("| 3. Update Customer      |")
        print("| 4. Delete Customer      |")
        print("| 5. Main Menu            |")
        print("|                         |")
        print("---------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            main_input = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please enter a number.\n")
            continue

        if(main_input == 1):
            customer_management_menu()
            break

        elif(main_input == 2):
            print(f"Your input was {main_input}\n")

        elif(main_input == 3):
            print(f"Your input was {main_input}\n")

        elif(main_input == 4):
            print(f"Your input was {main_input}\n")

        elif(main_input == 5):
            print("")
            main_menu()
            break
        
        else:
            print("Please insert a valid number.\n")

def bookings_tables_menu():
    pass

def sales_carts_menu():
    pass

def returns_menu():
    pass

def products_menu():
    pass

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

main()