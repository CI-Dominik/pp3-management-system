# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

""" Import needed Python modules """

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from colorama import Fore, Style, init
import re
from datetime import datetime

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
    
    print(f"Error connecting to database. Shutting down...")
    exit()

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
        print("| 4. Products             |")
        print("| 5. Close program        |")
        print("|                         |")
        print("---------------------------")
        print("|                         |")
        print("| DEV: 6. Reset Tables    |")
        print("| DEV: 7. Clear Bookings  |")
        print("| DEV: 8. Clear Carts     |")
        print("|                         |")
        print("---------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please only enter numbers.\n")
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
            sales_carts_menu()

        elif(response == 4):
            products_menu()

        elif(response == 5):
            print(Fore.YELLOW + "Thank you for using Happy Life's Management System. Shutting down...")
            exit()

            """ DEVELOPMENT COMMANDS """

        elif(response == 6):

            cursor.execute("UPDATE tables SET availability=1")
            connection.commit()

        elif(response == 7):

            cursor.execute("DELETE FROM bookings")
            connection.commit()

        elif(response == 8):

            cursor.execute("DELETE FROM cart")
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
            print("Please only enter numbers.\n")
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

            except ValueError:
                print("Please only enter numbers.\n")
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
                print("Please only enter numbers.\n")
                continue

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
                continue

        else:
            print(Fore.RED + "Customer's phone number already exists. Creation cancelled.\n")
            break

        cursor.execute("INSERT INTO customers (first_name, last_name, email, phone_number, bonus_points) VALUES (%s, %s, %s, %s, %s)",(f_name_input, l_name_input, email_input, phone_number_input.replace(" ", ""), 0))
        connection.commit()

        print(Fore.GREEN + "Customer successfully added to database.\n")
        
        cursor.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1")

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
            print("Please only enter numbers.\n")
            continue
        
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
        print("| 3. View open bookings               |")
        print("| 4. Main Menu                        |")
        print("|                                     |")
        print("---------------------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please only enter numbers.\n")
            continue

        if(response == 1):
            book_table()
            break

        elif(response == 2):
            tables_return = check_available_tables(0)
            if (len(tables_return) > 0):

                print("The following tables are available:\n")
                for table in tables_return:
                    print(Fore.GREEN + f"Table ID: {table['table_id']}, Number of seats: {table['number_of_seats']}")
                print("")
                continue
            else:
                print(Fore.RED + "There are currently no tables available.")
                continue

        elif(response == 3):
            check_bookings()

        elif(response == 4):
            print("")
            main_menu()
            break
        
        else:
            print("Please insert a valid number.\n")

def book_table():

    while True:

        try:

            number_of_people = int(input("Please enter the number of people: \n"))
            break

        except ValueError:

            print("Please only enter numbers.\n")
            continue

    if(number_of_people >= 1):

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
                    table_select = int(input("Please select a table ID or 0 to cancel: \n"))
                    if (table_select == 0):
                        break

                except ValueError:
                    print("Please only enter numbers.\n")
                    continue
                else:
                    if(table_select not in table_id_selection):
                        print("A table with that number is not available.")
                        continue
                    else:
                        break
            if (table_select != 0):
                while True:

                    print("Do you want to book a table for a new customer, a registered customer or a guest?")
                    print("1. New customer")
                    print("2. Existing customer")
                    print("3. Guest")
                    print(Fore.RED + "4. Cancel")

                    try:
                        choice = int(input("Please insert a number: \n"))
                    
                    except ValueError:
                        print("Please only enter numbers.\n")
                        continue

                    if (choice == 1):
                        customer = add_customer()

                        if (customer != None):
                            table_booking(customer, table_select, number_of_people)
                            break
                        else:
                            bookings_tables_menu()
                            break
                    
                    if (choice == 2):
                        customer = search_customer_attribute()
                        if (customer != None):
                            table_booking(customer, table_select, number_of_people)
                            break
                        else:
                            bookings_tables_menu()
                            break

                    if (choice == 3):
                        table_booking("guest", table_select, number_of_people)
                        break

                    if (choice == 4):
                        bookings_tables_menu()
                        break

                    else:
                        print("Invalid number.")
                        continue
            else:
                bookings_tables_menu()

        else:
            print(Fore.RED + "There are currently no tables available for your entered amount of people.")
            bookings_tables_menu()

    else:
        print(Fore.RED + "Number cannot be negative or 0.")
        bookings_tables_menu()

def table_booking(customer, table_select, number_of_people):

    if(customer != "guest"):

        cursor.execute("INSERT INTO bookings (customer_id, table_id, amount_of_people, date, active) VALUES (%s, %s, %s, %s, %s)", (customer['customer_id'], table_select, number_of_people, datetime.today().strftime('%Y-%m-%d'), 1))
        connection.commit()
        cursor.execute("UPDATE tables SET availability = 0 WHERE table_id =%s", (table_select,))
        connection.commit()

    else:
        cursor.execute("INSERT INTO bookings (table_id, amount_of_people, date, active) VALUES (%s, %s, %s, %s)", (table_select, number_of_people, datetime.today().strftime('%Y-%m-%d'), 1))
        connection.commit()
        cursor.execute("UPDATE tables SET availability = 0 WHERE table_id=%s", (table_select,))
        connection.commit()

    print(f"Booking successfully created for {number_of_people} people. Each guest will receive a cart for their seat at table {table_select}.")

    cursor.execute("SELECT booking_id FROM bookings ORDER BY booking_id DESC LIMIT 1")
    last_booking = cursor.fetchone()

    seat_counter = 1
    
    if(customer != "guest"):

        for i in range(number_of_people):

            cursor.execute("INSERT INTO cart (customer_id, booking_id, seat_number, table_id, walk_in) VALUES (%s, %s, %s, %s, %s)", (customer['customer_id'], last_booking['booking_id'], seat_counter, table_select, 0))
            seat_counter += 1
            connection.commit()

    else:
        for i in range(number_of_people):

            cursor.execute("INSERT INTO cart (booking_id, seat_number, table_id, walk_in) VALUES (%s, %s, %s, %s)", (last_booking['booking_id'], seat_counter, table_select, 0))
            connection.commit()

    bookings_tables_menu()

def check_available_tables(number_of_people):

    cursor.execute("SELECT * FROM tables WHERE availability=1 AND number_of_seats >= %s", (number_of_people,))
    tables_available = cursor.fetchall()

    return tables_available

def check_bookings():
    while True:

        print("Please specify a booking filter option.")
        print("1. By booking ID")
        print("2. By customer ID")
        print("3. By table ID")
        print("4. Cancel")

        try:
            check_input = int(input("Please enter a number: \n"))
        
        except ValueError:
            print("Please only enter numbers.\n")
            continue

        if (check_input == 1):
            check_booking_by_value("booking_id", "booking ID")
            break

        if (check_input == 2):
            check_booking_by_value("customer_id", "customer ID")
            break

        if (check_input == 3):
            check_booking_by_value("table_id", "table ID")
            break

        if (check_input == 4):
            break

def check_booking_by_value(value, callable_value):

    """ Check open bookings """

    booking_input = input(f"Please enter {callable_value} to search by: \n")
    
    cursor.execute("SELECT * FROM bookings WHERE " + value + "=%s AND active = 1", (booking_input,))
    check = cursor.fetchall()

    if (len(check) > 0):

        print("Open bookings:")

        for booking in check:
            print(Fore.GREEN + f"Booking ID: {booking['booking_id']}, Customer ID: {booking['customer_id']}, Table ID: {booking['table_id']}, Date: {booking['date']}")

    else:
        print(Fore.RED + "No entries found.")

""" Booking Functions End"""

""" Sale Functions Start """

def sales_carts_menu():

    """ Display the Sales / Carts Management Menu """

    print("You entered the Sales / Carts Management System.\n")
    print("")

    while True:

        print("+------- SALES / CARTS -------+")
        print("|                             |")
        print("| 1. Add product to cart      |")
        print("| 2. Remove product from cart |")
        print("| 3. Complete purchase        |")
        print("| 4. View Sales               |")    
        print("| 5. Main Menu                |")
        print("|                             |")
        print("-------------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please only enter numbers.\n")
            continue

        if(response == 1):
            select_cart()

        elif(response == 2):
            pass

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

def select_cart():

    while True:

        print("Please select a table ID or booking ID to find open carts.")
        print("1. Booking ID")
        print("2. Table ID")
        print("3. Guest payments")
        print("4. Cancel")

        try:
            selection_input = int(input("Please enter a number: \n"))

        except ValueError:
            print("Please only enter numbers.\n")
            continue

        if (selection_input == 1):
            search_type = "booking_id"
            search_value = select_cart_by_value("booking ID")
            break

        if (selection_input == 2):
            search_type = "table_id"
            search_value = select_cart_by_value("table ID")
            break

        if (selection_input == 3):
            search_type = "walk_in"
            search_value = 1
            break

        if (selection_input == 4):
            break

        else:
            print("Invalid value.")
            continue
    
    if (selection_input != 4):

        cursor.execute("SELECT * FROM cart WHERE payed=0 AND " + search_type + "=%s", (search_value,))
        open_carts = cursor.fetchall()

    else:
        sales_carts_menu()

    if(len(open_carts) > 0):

        cart_ids = []

        for cart in open_carts:
            cart_ids.append(cart['cart_id'])

        while True:

            print("The following carts are currently open:\n")

            for cart in open_carts:
                print(f"Seat number: {cart['seat_number']}: Cart ID: {cart['cart_id']}, Customer ID: {cart['customer_id'] if cart['customer_id'] is not None else "Guest booking"}, Booking ID: {cart['booking_id']}")
            try:

                cart_input = int(input("Please select a cart ID to add a product to or 0 to cancel: \n"))

            except ValueError:
                print("Please only enter numbers.\n")
                continue

            if (cart_input == 0):
                break

            if (cart_input in cart_ids):
                add_product_to_cart(cart_input)
                break

            else:
                print(Fore.RED + "Invalid input.")
                continue

    else:
        print(Fore.RED + "No carts found.")
        sales_carts_menu()

def add_product_to_cart(cart_id):

    pass # --------------------------------------- TODO: NEXT SALES / CHECK IF PRODUCT IS ALREADY IN CART -> UPDATE AMOUNT -> REMOVE AT 0

def select_cart_by_value(callable_value):

    while True:
        try:
            value_input = int(input("Please input a " + callable_value + " to search by:\n"))

        except ValueError:
            print("Please only enter numbers.\n")
            continue

        if (value_input == 0):
            break

        else:
            return value_input




    else:
        print("There are currently no open carts.")

""" Sale Functions End """

""" Product Functions Start """

def products_menu():

    """ Display the Products Management Menu """

    print("You entered the Products Management System.\n")
    print("")

    while True:

        print("+---------- PRODUCTS ----------+")
        print("|                              |")
        print("| 1. Add product               |")
        print("| 2. Update product            |")
        print("| 3. Check wares               |")
        print("| 4. Main menu                 |")
        print("|                              |")
        print("--------------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print("Please only enter numbers.\n")
            continue

        if(response == 1):
            add_product()

        elif(response == 2):
            product = get_product_list()
            if (product != None):
                update_product(product)
                break
            else:
                continue
        
        elif(response == 3):
            get_product_list(True)
            continue

        elif(response == 4):
            print("")
            main_menu()
            break
        
        else:
            print("Please insert a valid number.\n")

def add_product():

    while True:

        print("Please select the category of product you want to add.")
        print("1. Cakes")
        print("2. Cookies")
        print("3. Main dishes")
        print("4. Drinks")
        print("5. Cancel")

        try:

            product_add_input = int(input("Please choose a category: \n"))

        except ValueError:
            print("Please only use numbers.\n")
            continue

        if (product_add_input == 1):

            add_product_by_category("cake", "cake")
            break

        if (product_add_input == 2):
            add_product_by_category("cookie", "cookie")
            break

        if (product_add_input == 3):
            add_product_by_category("main dish", "main dish")
            break

        if (product_add_input == 4):
            add_product_by_category("drink", "drink")
            break

        if (product_add_input == 5):
            break

        else:
            print(Fore.RED + "Invalid input.")
            continue

def add_product_by_category(value, callable_value):

    while True:

        name_input = input(f"Please insert the name of the {callable_value} to add or 0 to cancel: \n")

        if (name_input == "0"):
            break

        try:

            amount_input = int(input("Please insert the stock amount or 0 to cancel: \n"))

        except ValueError:
            print("Please only use numbers.\n")
            continue

        if(amount_input == 0):
            break

        if (amount_input < 0):
            print("Number cannot be negative.")
            continue

        pattern = r"^\d+\.\d{2}$"

        try:
        
            price_input = input("Please enter the price or 0 to cancel: \n")

        except ValueError:

            print("Please enter a floating-point number.")

        if(price_input == "0"):
            break

        if(re.fullmatch(pattern, price_input) == None):
            print(Fore.RED + "Wrong format. Example: 4.99")
            continue

        cursor.execute("INSERT INTO products (name, category, available_amount, price) VALUES (%s, %s, %s, %s)", (name_input, value, amount_input, float(price_input)))
        connection.commit()

        print("Product successfully added to database.")
        break

def get_product_list(view_only=False):

    while True:

        print("Please select the category of items you want to show.")
        print("1. Cakes")
        print("2. Cookies")
        print("3. Main dishes")
        print("4. Drinks")
        print("5. Cancel")

        try:
            product_input = int(input("Please insert a number: \n"))

        except ValueError:
            print("Please only use numbers.\n")
            continue
                # -------------------------------------------------------- TODO: Write if condition if product != None and save in variable for another function to use
        if (product_input == 1):
            product = get_product_by_category("cake", "cake", view_only)
            if(product != None):
                return product
            else:
                return None

        if (product_input == 2):
            product = get_product_by_category("cookie", "cookie", view_only)
            if(product != None):
                return product
            else:
                return None

        if (product_input == 3):
            product = get_product_by_category("main dish", "main dish", view_only)
            if(product != None):
                return product
            else:
                return None

        if (product_input == 4):
            product = get_product_by_category("drink", "drink", view_only)
            if(product != None):
                return product
            else:
                return None

        if (product_input == 5):
            break

def get_product_by_category(value, callable_value, view_only):

    cursor.execute("SELECT * FROM products WHERE category=%s",(value,))
    product_result = cursor.fetchall()
    product_ids = []

    if (len(product_result) > 0):

        print(f"The following items have been found in the category {callable_value}:\n")

        for product in product_result:
            print(Fore.GREEN + f"Product ID: {product['product_id']}, Product name: {product['name']}, Available amount: {product['available_amount']}, Price: {product['price']}\n")
            product_ids.append(product['product_id'])

        if (view_only == False):

            while True:

                try:
                    selection = int(input("Please select a product by ID or 0 to cancel: \n"))

                except ValueError:
                    print("Please only use numbers.\n")
                    continue

                if (selection == 0):
                    break

                if (selection in product_ids):
                    cursor.execute("SELECT * FROM products WHERE product_id=%s", (selection,))
                    product_return = cursor.fetchone()
                    print(Fore.GREEN + f"You selected {product_return['name']}.")
                    return product_return

                else:
                    print(Fore.RED + "No product with that number available.")
                    continue

    else:
        print(Fore.RED + "No product has been found in that category.")
        return None

def update_product(product):
    
    while True:
        print(f"Which attribute of {product['name']} (ID: {product['product_id']}) do you want to change?")
        print("1. Name")
        print("2. Category")
        print("3. Price")
        print("4. Amount")
        print(Fore.RED + "5. Cancel")

        try:
            update_input = int(input("Please select a number: \n"))

        except ValueError:
            print("Please only use numbers.\n")
            continue

        if (update_input == 1):
            update_product_by_value(product, "name", "name")
            break

        if (update_input == 2):
            update_product_by_value(product, "category", "category")
            break

        if (update_input == 3):
            update_product_by_value(product, "price", "price")
            break

        if (update_input == 4):
            update_product_by_value(product, "available_amount", "amount")
            break

        if (update_input == 5):
            products_menu()
            break    

def update_product_by_value(product, value, callable_value):

    categories = ["cake", "cookie", "main dish", "drink"]

    while True:

        update_input = input(f"Please enter the new {callable_value} for {product['name']} or 0 to cancel:\n")

        if (update_input == "0"):
            products_menu()
            break

        if (value == "name"):

            cursor.execute("UPDATE products SET name=%s WHERE product_id=%s", (update_input, product['product_id']))
            connection.commit()
            print(Fore.GREEN + f"Name of {product['name']} was successfully changed to {update_input}.")
            break

        if (value == "category"):

            if (update_input.lower() in categories):
                cursor.execute("UPDATE products SET category=%s WHERE product_id=%s", (update_input.lower(), product['product_id']))
                connection.commit()
                print(Fore.GREEN + f"Product {product['name']}'s {callable_value} was successfully changed to {update_input}.")
                break

            else:

                print(Fore.RED + "Please only use the categories cake, cookie, main dish or drink.")
                continue

        if (value == "price"):

            pattern = r"^-?\d+\.\d{2}$"

            if(re.fullmatch(pattern, update_input) == None):
                print(Fore.RED + "Wrong format. Example: 4.99")
                continue

            float(update_input)

            if (float(update_input) < 0):
                print(Fore.RED + "The value cannot be negative.")
                continue

            else:
                cursor.execute("UPDATE products SET price=%s WHERE product_id=%s", (update_input, product['product_id']))
                connection.commit()
                print(Fore.GREEN + f"Price of {product['name']} successfully updated to ${update_input}.")
                break

        if (value == "available_amount"):
            pass # ------------------- TODO: CHECK FOR NEGATIVE

def select_another_product():
    pass # ---------------------------------------------- TODO: FOR SALES

""" Product Functions End """

""" Main Cycle Start """

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

""" Main Cycle End """

""" Call Main Cycle """

main()