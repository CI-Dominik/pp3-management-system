# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

""" Import needed Python modules """

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init

init(autoreset=True)

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
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please enter a number.\n")
            continue

        if(response == 1):
            print("")
            customer_management_menu()
            break

        elif(response == 2):
            print(f"Your input was {response}\n")

        elif(response == 3):
            print(f"Your input was {response}\n")

        elif(response == 4):
            print(f"Your input was {response}\n")

        elif(response == 5):
            print(f"Your input was {response}\n")
        
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
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please enter a number.\n")
            continue

        if(response == 1):
            search_customer()
            break

        elif(response == 2):
            print(f"Your input was {response}\n")

        elif(response == 3):
            result = search_customer_attribute()

        elif(response == 4):
            print(f"Your input was {response}\n")

        elif(response == 5):
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

def search_customer():

    """ Search customer menu """

    while True:

        print("+------- SEARCH CUSTOMER -------+")
        print("|                               |")
        print("| By which parameter do you     |")
        print("| want to search?               |")
        print("|                               |")
        print("| 1. Name (possible duplicates) |")
        print("| 2. By email address           |")
        print("| 3. By phone number            |")
        print("| 4. By ID                      |")
        print("| 5. Customer Management        |")
        print("|                               |")
        print("---------------------------------")

        try:

            response = int(input("Please select a way to search: \n"))

        except ValueError:

            print("Please enter a number.\n")
            continue

        if(response == 1):
            search_customer_attribute("name")
            
        elif(response == 2):
            search_customer_attribute("email", "email address")

        elif(response == 3):
            search_customer_attribute("phone_number", "phone number")

        elif(response == 4):
            search_customer_attribute("customer_id", "customer ID")

        elif(response == 5):
            customer_management_menu()
            break

def search_customer_attribute(type=None, callable_type=None):

    """ Search customer by attribute """

    if(type == None):

        """ If no attribute is provided, choose one here """

        print("")
        print("Please choose attribute to get customer by:\n")
        print("1. Name (Possible duplicates)\n")
        print("2. Email address\n")
        print("3. Phone number\n")
        print("4. Customer ID\n")
        print("5. Back to main menu\n")

        while True:

            try:
                search_input = int(input("Please type a number: \n"))
            except TypeError:
                print("Please only insert numbers.")
                continue
            if(search_input == 1):
                type = "name"
                break
            elif(search_input == 2):
                type="email"
                callable_type="email address"
                break
            elif(search_input == 3):
                type="phone_number"
                callable_type="phone number"
                break
            elif(search_input == 4):
                type="customer_id"
                callable_type="customer ID"
                break
            elif(search_input == 5):
                main_menu()
                break
            else:
                print(Fore.RED + "Invalid input.")

    """ If an attribute is provided, function starts here """

    if(type == "name"):
                
        f_name = input("Please insert a first name to search by: \n")
        l_name = input("Please insert a last name to search by: \n")
        cursor.execute("SELECT * FROM customers WHERE first_name=%s AND last_name=%s", (f_name, l_name))
        result = cursor.fetchall()

    else:
                
        type_input = input(f"Please insert {callable_type} to search by: \n")
        cursor.execute(f"SELECT * FROM customers WHERE {type}=%s", (type_input,))
        result = cursor.fetchall()

    """ Return customer when exactly one entry was found """

    if(len(result) == 1):
        print("")
        print(Fore.GREEN + f"Result:\nCustomer ID: {result[0]["customer_id"]}, Name: {result[0]["first_name"]} {result[0]["last_name"]}, Email address: {result[0]["email"]}, Phone number: {result[0]["phone_number"]}")
        print("")

        while True:
            check = input("Is this correct? [y/n]\n")
            if(check.lower() == "y"):
                return result[0]         
            elif(check.lower() == "n"):
                break
            else:
                print("Please enter y or n for your answer.")

        """ Display and check when multiple values were found """

    elif (len(result) > 1):

        print("")
        print(Fore.YELLOW + f"Multiple entries have been found. Please use another filtering method or select by typing the ID of a result to use that entry.")

        id_entries = []

        """ Cycle through results and save found IDs in array """

        for i in range(len(result)):
            print("")
            print(Fore.GREEN + f"Result {i + 1}:\nCustomer ID: {result[i]["customer_id"]}, Name: {result[i]["first_name"]} {result[i]["last_name"]}, Email address: {result[i]["email"]}, Phone number: {result[i]["phone_number"]}")
            id_entries.append(result[i]["customer_id"])
            print(id_entries)
            print("")
        
        print(Fore.YELLOW + "Do you want to use another attribute or use an ID?")
        print(Fore.YELLOW + "1. Use ID")
        print(Fore.YELLOW + "2. Use another attribute")
        print(Fore.RED + "0. Cancel")

        """ Choice what to do when multiple entries are found """
        
        while True:

            try:
                choice = int(input("Please insert a number: \n"))
            except ValueError:
                print("please only use numbers.")
            if (choice == 1):
                """ Choice to pick entry by ID """
                id_choice = int(input(Fore.YELLOW + "Please insert ID of the customer to select: \n"))

                if(id_choice in id_entries):
                    print(f"You have chosen the entry with the customer ID {id_choice}:")
                    cursor.execute("SELECT * FROM customers WHERE customer_id=%s", (id_choice,))
                    chosen_entry = cursor.fetchone()
                    print(Fore.GREEN + f"Customer ID: {chosen_entry["customer_id"]}, Name: {chosen_entry["first_name"]} {chosen_entry["last_name"]}, Email address: {chosen_entry["email"]}, Phone number: {chosen_entry["phone_number"]}")

                    while True:

                        check = input("Is this correct? [y/n]\n")
                        if(check.lower() == "y"):
                            return chosen_entry
                        elif(check.lower() == "n"):
                            break
                        else:
                            print("Please enter y or n for your answer.")
                else:
                    print("No entry with that ID found.")
                    continue

            if(choice == 2):
                search_customer_attribute()
                break

            if(choice == 0):
                break

            else:
                print(Fore.RED + "Invalid input.")

    else:
        print("")
        print(Fore.RED + "No entries found.")
        print(Style.RESET_ALL)
        print("")
        return None

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

main()