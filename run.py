# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

""" Import needed Python modules """

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init
import re

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
    
    print(f"ERROR CONNECTING TO DATABASE!")

""" Main Menu Start """

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
        print("|                         |")
        print("| DEV: 6. Reset Tables    |")
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
            print("")
            bookings_tables_menu()
            break

        elif(response == 3):
            print(f"Your input was {response}\n")

        elif(response == 4):
            print(f"Your input was {response}\n")

        elif(response == 5):
            print(f"Your input was {response}\n")

            """ DEVELOPMENT COMMANDS """

        elif(response == 6):

            cursor.execute("UPDATE tables SET availability=1")
            connection.commit()
        
        else:
            print("Please insert a valid number.\n")

""" Main Menu End """

""" Customer Functions Start """

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
        print("| 4. Main Menu            |")
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
            search_customer_attribute()

        elif(response == 2):
            add_customer()

        elif(response == 3):
            update_customer()

        elif(response == 4):
            print("")
            main_menu()
            break
        
        else:
            print("Please insert a valid number.\n")

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

def add_customer():

    """ Function to add a new customer to the database """

    while True:

        f_name_input = input("Please insert the customer's first name or enter 0 to exit: \n")

        if (f_name_input == "0"):
            break

        l_name_input = input("Please insert the customer's last name or enter 0 to exit: \n")

        if (l_name_input == "0"):
            break

        """ Check email address format """
            
        email_input = input("Please insert the customer's email address or enter 0 to exit: \n")

        if (email_input == "0"):
            break

        cursor.execute("SELECT email FROM customers WHERE email=%s", (email_input,))
            
        if(cursor.fetchone() == None):
            
            email_pattern = r"^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w+$"

            if(re.match(email_pattern, email_input) == None):
                print(Fore.RED + "Wrong email format. Example: value@mail.com.\n")
                break

        else:
            print(Fore.RED + "Customer's email address already exists. Creation cancelled.\n")
            break
        
        """ Check phone number format """

        phone_pattern = r"^(?:\+44|0044|0)\s?7\d{3}\s?\d{6}$|^(?:\+44|0044|0)\s?\d{2,4}\s?\d{3,4}\s?\d{4}$"

        phone_number_input = input("Please insert the customer's phone number (UK format) or enter 0 to exit: \n")

        if (phone_number_input == "0"):
            break

        cursor.execute("SELECT email FROM customers WHERE phone_number=%s", (phone_number_input,))
            
        if(cursor.fetchone() == None):

            if (re.match(phone_pattern, phone_number_input) == None):
                print(Fore.RED + "Wrong phone number format. Please use a UK formatted number.\n")
                break

        else:
            print(Fore.RED + "Customer's phone number already exists. Creation cancelled.\n")
            break

        cursor.execute("INSERT INTO customers (first_name, last_name, email, phone_number, bonus_points) VALUES (%s, %s, %s, %s, %s)",(f_name_input, l_name_input, email_input, phone_number_input.replace(" ", ""), 0))
        connection.commit()

        print(Fore.GREEN + "Customer successfully added to database.\n")
        
        cursor.execute("SELECT * FROM customers WHERE first_name=%s AND last_name=%s AND email=%s AND phone_number=%s", (f_name_input, l_name_input, email_input, phone_number_input))

        customer = cursor.fetchone()

        return customer

def update_customer():
    customer = search_customer_attribute()

    while True:

        print("Which attribute do you want to change?")
        print("1. First name")
        print("2. Last name")
        print("3. Email address")
        print("4. Phone number")
        print(Fore.RED + "5. Cancel")

        try:

            choice = int(input("Please make a selection: \n"))

        except ValueError:
            print("Please insert only numbers.")

        
        if (choice == 1):
            update_customer_data(customer, "first_name", "first name")
        if (choice == 2):
            update_customer_data(customer, "last_name", "last name")
        if (choice == 3):
            update_customer_data(customer, "email", "email address")
        if (choice == 4):
            update_customer_data(customer, "phone_number", "phone number")
        if (choice == 5):
            break

def update_customer_data(customer, value, callable_value):
    
    while True:

        value_input = input(f"Please enter a new value for the {callable_value} or 0 to cancel: \n")

        if (value_input == "0"):
            break

        if(value == "email" and value_input != "0"):
            
            email_pattern = r"^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w+$"

            if(re.match(email_pattern, value_input) == None):
                print(Fore.RED + "Wrong email format. Example: value@mail.com.\n")
                break

        if(value == "phone_number" and value_input != 0):

            phone_pattern = r"^(?:\+44|0044|0)\s?7\d{3}\s?\d{6}$|^(?:\+44|0044|0)\s?\d{2,4}\s?\d{3,4}\s?\d{4}$"

            if (re.match(phone_pattern, value_input) == None):
                print(Fore.RED + "Wrong phone number format. Please use a UK formatted number.\n")
                break

            value_input = value_input.replace(" ", "")

        cursor.execute("SELECT email, phone_number FROM customers")

        database_results = cursor.fetchall()
        database_check_email = []
        database_check_phone_number = []

        for row in database_results:
            database_check_email.append(row["email"])
            database_check_phone_number.append(row["phone_number"])

        if (value_input in database_check_email or value_input in database_check_phone_number):
            print(Fore.RED + "Entry already in database. No duplicates allowed.")
            break
        else:
            cursor.execute("UPDATE customers SET " + value + "=%s WHERE customer_id=%s", (value_input, customer["customer_id"]))
            connection.commit()
            print(f"The new {callable_value} for {customer["first_name"]} {customer["last_name"]} was set to {value_input}.")
            break

""" Customer Functions End """

""" Booking Functions Start """

def bookings_tables_menu():

    """ Display the Bookings / Table Management Menu """

    print("You entered the Bookings / Tables Management System.\n")
    print("")

    while True:

        print("+--------- BOOKINGS / TABLES ---------+")
        print("|                                     |")
        print("| 1. Book Table                       |")
        print("| 2. View available Tables            |")
        print("| 3. Create single purchase           |")
        print("| 4. View bookings                    |")
        print("| 5. Main Menu                        |")
        print("|                                     |")
        print("---------------------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please enter a number.\n")
            continue

        if(response == 1):
            book_table()
            break

        elif(response == 2):
            check_available_tables()
            continue

        elif(response == 3):
            pass

        elif(response == 4):
            pass

        elif(response == 5):
            print("")
            main_menu()
            break
        
        else:
            print("Please insert a valid number.\n")

def book_table():

    while True:

        try:

            number_of_people = int(input("Please enter the number of people: \n"))

        except ValueError:

            print("Please only insert numbers.")

        finally:
            break

    available_tables = check_available_tables(number_of_people)

    print("The following tables are available:\n")
    
    table_id_selection = []

    for table in available_tables:
        print(f"Table ID: {table['table_id']}, Number of seats: {table['number_of_seats']}")
        table_id_selection.append(table['table_id'])

    if(len(available_tables) > 0):

        """ Select table ID from the available tables """

        while True:

            try: 
                table_select = int(input("Please select a table ID: \n"))

            except ValueError:
                print("Please only use numbers.")
                continue
            else:
                if(table_select not in table_id_selection):
                    print("A table with that number is not available.")
                    continue
                else:
                    break
            
        # ------------------------------------------------- TODO: CHECK IF NUMBER IS USABLE AND IN LIST
        
        while True:

            print("Do you want to book a table for a new customer, a registered customer or a guest?")
            print("1. New customer")
            print("2. Existing customer")
            print("3. Guest")
            print(Fore.RED + "4. Cancel")

            try:
                choice = int(input("Please insert a number: \n"))
            
            except ValueError:
                print("Please only insert numbers.")

            if (choice == 1):
                customer = add_customer()
                table_booking(customer, available_tables, number_of_people)
            
            if (choice == 2):
                customer = search_customer_attribute()
                table_booking(customer, available_tables, number_of_people)

            if (choice == 3):
                table_booking("guest", available_tables, number_of_people)

            if (choice == 4):
                bookings_tables_menu()
                break

            else:
                print("Invalid number.")
                continue

    else:
        print("There are currently no tables available for your entered amount of people.")
        bookings_tables_menu()

def table_booking(customer, available_tables, number_of_people):
    pass

def check_available_tables(number_of_people):

    cursor.execute("SELECT * FROM tables WHERE availability=1 AND number_of_seats >= %s", (number_of_people,))
    tables_available = cursor.fetchall()

    return tables_available

""" Booking Functions End"""

""" Sale Functions Start """

def sales_carts_menu():
    pass

""" Sale Functions End """

""" Return Functions Start """

def returns_menu():
    pass

""" Return Functions End """

""" Product Functions Start """

def products_menu():
    pass

""" Product Functions End """



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

main()