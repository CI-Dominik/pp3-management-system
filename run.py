""" Import needed Python modules and enable autoreset of colors """

import os
import mysql.connector
import re
from mysql.connector import Error
from dotenv import load_dotenv
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

""" Load .env file to authenticate in database """

load_dotenv()

""" Set variables to access MySQL database and admin panel """

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

admin_access = os.getenv("ADMIN")

""" Establish databse connection """

try:
    connection = mysql.connector.connect(
        host=db_host, database=db_name, user=db_user, password=db_pass
    )

    """ Create cursor for usage with MySQL """

    cursor = connection.cursor(dictionary=True)

    """ Print error if database connection was not successful """

except Error:
    print(Fore.RED + "Error connecting to database. Shutting down...")
    exit()

""" Main Menu Start """


def main_menu():
    """Function to show the Main Menu of the system
    and get a choice for the next move"""

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
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print(Fore.RED + "Please only enter numbers.\n")
            continue

        if response == 1:
            os.system("cls" if os.name == "nt" else "clear")
            customer_management_menu()
            break

        elif response == 2:
            os.system("cls" if os.name == "nt" else "clear")
            bookings_tables_menu()
            break

        elif response == 3:
            os.system("cls" if os.name == "nt" else "clear")
            sales_carts_menu()

        elif response == 4:
            os.system("cls" if os.name == "nt" else "clear")
            products_menu()

        elif response == 5:
            os.system("cls" if os.name == "nt" else "clear")
            print(
                Fore.YELLOW
                + """Thank you for using Happy Life's Management"""
                """ System. Shutting down..."""
            )
            exit()

        else:
            print(Fore.RED + "Please insert a valid number.\n")


""" Main Menu End """

""" Customer Functions Start """


def customer_management_menu():
    """Display the Customer Management Menu"""

    print("You entered the Customers Management System.\n")
    print("")

    while True:

        print("+------- CUSTOMERS -------+")
        print("|                         |")
        print("| 1. Search Customer      |")
        print("| 2. Add new Customer     |")
        print("| 3. Update Customer      |")
        print("| 4. Show Customers       |")
        print("| 5. Main Menu            |")
        print("|                         |")
        print("---------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print(Fore.RED + "Please only enter numbers.\n")
            continue

        if response == 1:
            os.system("cls" if os.name == "nt" else "clear")
            search_customer_attribute()

        elif response == 2:
            os.system("cls" if os.name == "nt" else "clear")
            add_customer()

        elif response == 3:
            os.system("cls" if os.name == "nt" else "clear")
            update_customer()

        elif response == 4:
            os.system("cls" if os.name == "nt" else "clear")
            show_customers()

        elif response == 5:
            os.system("cls" if os.name == "nt" else "clear")
            main_menu()
            break

        else:
            print(Fore.RED + "Please insert a valid number.\n")


def search_customer_attribute(type=None, callable_type=None):
    """Search customer by attribute"""

    if type is None:

        """If no attribute is provided, choose one here"""

        print("")
        print("Please choose attribute to get customer by:")
        print("1. Name (Possible duplicates)")
        print("2. Email address")
        print("3. Phone number")
        print("4. Customer ID")
        print("5. Cancel")

        while True:

            try:
                search_input = int(input("Please type a number: \n"))

            except ValueError:
                print(Fore.RED + "Please only enter numbers.\n")
                continue

            if search_input == 1:
                type = "name"
                break

            elif search_input == 2:
                type = "email"
                callable_type = "email address"
                break

            elif search_input == 3:
                type = "phone_number"
                callable_type = "phone number"
                break

            elif search_input == 4:
                type = "customer_id"
                callable_type = "customer ID"
                break

            elif search_input == 5:
                os.system("cls" if os.name == "nt" else "clear")
                customer_management_menu()
                break

            else:
                print(Fore.RED + "Invalid input.")

    """ If an attribute is provided, function starts here """

    if type == "name":

        f_name = input("Please insert a first name to search by: \n")
        l_name = input("Please insert a last name to search by: \n")
        connection.ping(reconnect=True)
        cursor.execute(
            """SELECT SQL_NO_CACHE *
            FROM customers
            WHERE first_name=%s
            AND last_name=%s""",
            (f_name, l_name),
        )
        result = cursor.fetchall()

    else:

        type_input = input(f"Please insert {callable_type} to search by: \n")
        connection.ping(reconnect=True)
        cursor.execute(
            f"SELECT SQL_NO_CACHE * FROM customers WHERE {type}=%s",
            (type_input,),
        )
        result = cursor.fetchall()

    """ Return customer when exactly one entry was found """

    if len(result) == 1:
        print("")
        print(
            Fore.GREEN + f"""Result:\n
Customer ID: {result[0]["customer_id"]},
Name: {result[0]["first_name"]} {result[0]["last_name"]},
Email address: {result[0]["email"]},
Phone number: {result[0]["phone_number"]}"""
        )
        print("")

        while True:
            check = input("Is this correct? [y/n]\n")
            if check.lower() == "y":
                os.system("cls" if os.name == "nt" else "clear")
                return result[0]
            elif check.lower() == "n":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print(Fore.RED + "Please enter y or n for your answer.")

        """ Display and check when multiple values were found """

    elif len(result) > 1:

        print("")
        print(
            Fore.YELLOW
            + """Multiple entries have been found. Please use another """
            """filtering method or select by typing the ID of a """
            """result to use that entry."""
        )

        id_entries = []

        """ Cycle through results and save found IDs in list """

        for i in range(len(result)):
            print("")
            print(
                Fore.GREEN +
                f"""Result {i + 1}: """ +
                f"""Customer ID: {result[i]["customer_id"]}, """ +
                f"""Name: {result[i]["first_name"]} """ +
                f"""{result[i]["last_name"]}, """ +
                f"""Email address: {result[i]["email"]}, """ +
                f"""Phone number: {result[i]["phone_number"]}"""
            )
            id_entries.append(result[i]["customer_id"])

        """ Choice what to do when multiple entries are found """

        while True:

            print(
                """Do you want to use an ID or """
                """return to the main menu to try again?"""
            )
            print("1. Use ID")
            print("2. Back to main menu")

            try:
                choice = int(input("Please insert a number: \n"))

            except ValueError:
                print(Fore.RED + "Please only enter numbers.\n")
                continue

            if choice == 1:
                """Choice to pick entry by ID"""
                id_choice = int(
                    input(
                        Fore.YELLOW
                        + "Please insert ID of the customer to select: \n"
                    )
                )

                if id_choice in id_entries:
                    print(
                        """You have chosen the entry with """ +
                        f"""the customer ID {id_choice}:"""
                    )
                    connection.ping(reconnect=True)
                    cursor.execute(
                        """
                        SELECT SQL_NO_CACHE *
                        FROM customers
                        WHERE customer_id=%s""",
                        (id_choice,),
                    )
                    chosen_entry = cursor.fetchone()
                    print(
                        Fore.GREEN +
                        f"""Customer ID: {chosen_entry["customer_id"]}, """ +
                        f"""Name: {chosen_entry["first_name"]} """ +
                        f"""{chosen_entry["last_name"]}, """ +
                        f"""Email address: {chosen_entry["email"]}, """ +
                        f"""Phone number: {chosen_entry["phone_number"]}"""
                    )

                    while True:

                        check = input("Is this correct? [y/n]\n")
                        if check.lower() == "y":
                            os.system("cls" if os.name == "nt" else "clear")
                            return chosen_entry
                        elif check.lower() == "n":
                            os.system("cls" if os.name == "nt" else "clear")
                            main_menu()
                            break
                        else:
                            print(
                                Fore.RED
                                + "Please enter y or n for your answer."
                            )
                else:
                    print(Fore.RED + "No entry with that ID found.")
                    continue

            elif choice == 2:
                os.system("cls" if os.name == "nt" else "clear")
                main_menu()
                break

            else:
                print(Fore.RED + "Invalid input.")

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.RED + "No entries found.")
        print(Style.RESET_ALL)
        print("")
        return None


def add_customer():
    """Function to add a new customer to the database"""

    while True:

        f_name_input = input(
            "Please insert the customer's first name or enter 0 to exit: \n"
        )

        if f_name_input == "0":
            break

        l_name_input = input(
            "Please insert the customer's last name or enter 0 to exit: \n"
        )

        if l_name_input == "0":
            break

        """ Check email address format """

        email_input = input(
            "Please insert the customer's email address or enter 0 to exit: \n"
        )

        if email_input == "0":
            break

        connection.ping(reconnect=True)
        cursor.execute(
            "SELECT SQL_NO_CACHE email FROM customers WHERE email=%s",
            (email_input,),
        )

        if cursor.fetchone() is None:

            email_pattern = r"^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w+$"

            if re.match(email_pattern, email_input) is None:
                print(
                    Fore.RED + "Wrong email format. Example: value@mail.com.\n"
                )
                break

        else:
            print(
                Fore.RED
                + """Customer's email address already exists. """
                """Creation cancelled.\n"""
            )
            break

        """ Check phone number format """

        phone_pattern = (
            r"^(?:\+44|0044|0)\s?7\d{3}\s?\d{6}$|"
            r"^(?:\+44|0044|0)\s?\d{2,4}\s?\d{3,4}\s?\d{4}$"
        )

        phone_number_input = input(
            """Please insert the customer's phone number """
            """(UK format, example: 055 1234 5678) or enter 0 to exit: \n"""
        )

        if phone_number_input == "0":
            break

        connection.ping(reconnect=True)
        cursor.execute(
            "SELECT SQL_NO_CACHE email FROM customers WHERE phone_number=%s",
            (phone_number_input,),
        )

        if cursor.fetchone() is None:

            if re.match(phone_pattern, phone_number_input) is None:
                print(
                    Fore.RED
                    + """Wrong phone number format. """
                    """Please use a UK formatted number.\n"""
                )
                continue

        else:
            print(
                Fore.RED
                + "Customer's phone number already exists. Cancelled.\n"
            )
            break

        connection.ping(reconnect=True)
        cursor.execute(
            """INSERT INTO customers (first_name, last_name,
            email, phone_number, bonus_points) VALUES (%s, %s, %s, %s, %s)""",
            (
                f_name_input,
                l_name_input,
                email_input,
                phone_number_input.replace(" ", ""),
                0,
            ),
        )
        connection.commit()
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.GREEN + "Customer successfully added to database.\n")

        connection.ping(reconnect=True)
        cursor.execute(
            """SELECT SQL_NO_CACHE *
            FROM customers
            ORDER BY customer_id DESC
            LIMIT 1"""
        )

        customer = cursor.fetchone()

        return customer


def update_customer():
    """Function to select customer data to change"""

    customer = search_customer_attribute()

    if customer is not None:

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
                print(Fore.RED + "Please only enter numbers.\n")
                continue

            if choice == 1:
                update_customer_data(customer, "first_name", "first name")

            if choice == 2:
                update_customer_data(customer, "last_name", "last name")

            if choice == 3:
                update_customer_data(customer, "email", "email address")

            if choice == 4:
                update_customer_data(customer, "phone_number", "phone number")

            if choice == 5:
                os.system("cls" if os.name == "nt" else "clear")
                break

    else:
        print(Fore.RED + "No customer selected.")


def update_customer_data(customer, value, callable_value):
    """Function to change actual data"""

    while True:

        value_input = input(
            f"Set a new value for the {callable_value} or 0 to cancel:\n"
        )

        if value_input == "0":
            break

        """ Check email address format """

        if value == "email" and value_input != "0":

            email_pattern = r"^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w+$"

            if re.match(email_pattern, value_input) is None:
                print(
                    Fore.RED + "Wrong email format. Example: value@mail.com.\n"
                )
                break

        """ Check phone numnber format """

        if value == "phone_number" and value_input != 0:

            phone_pattern = (
                r"^(?:\+44|0044|0)\s?7\d{3}\s?\d{6}$|"
                r"^(?:\+44|0044|0)\s?\d{2,4}\s?\d{3,4}\s?\d{4}$"
            )

            if re.match(phone_pattern, value_input) is None:
                print(
                    Fore.RED
                    + "Wrong format. Please use a UK formatted number.\n"
                )
                break

            value_input = value_input.replace(" ", "")

        connection.ping(reconnect=True)
        cursor.execute(
            "SELECT SQL_NO_CACHE email, phone_number FROM customers"
        )

        database_results = cursor.fetchall()
        database_check_email = []
        database_check_phone_number = []

        for row in database_results:
            database_check_email.append(row["email"])
            database_check_phone_number.append(row["phone_number"])

        """ Check database results for duplicates """

        if (
            value_input in database_check_email
            or value_input in database_check_phone_number
        ):
            print(
                Fore.RED + "Entry already in database. No duplicates allowed."
            )
            break

        else:
            connection.ping(reconnect=True)
            cursor.execute(
                "UPDATE customers SET " + value + "=%s WHERE customer_id=%s",
                (value_input, customer["customer_id"]),
            )
            connection.commit()
            os.system("cls" if os.name == "nt" else "clear")
            print(
                Fore.GREEN +
                f"""The new {callable_value} for """ +
                f"""{customer["first_name"]} {customer["last_name"]} """ +
                f"""was set to {value_input}."""
            )
            break


def show_customers():

    connection.ping(reconnect=True)
    cursor.execute(
        "SELECT SQL_NO_CACHE * FROM customers ORDER BY customer_id ASC"
    )
    result = cursor.fetchall()

    result_list = [result[i: i + 10] for i in range(0, len(result), 10)]
    index = 0

    while True:

        print("+------- CUSTOMER OVERVIEW -------+\n")

        print(Fore.YELLOW + f"Page {index + 1} / {len(result_list)}\n")

        for i in result_list[index]:

            print(
                Fore.GREEN
                + f"""ID: {i['customer_id']}, Name: {i['first_name']} """ +
                f"""{i['last_name']}, Email: {i['email']},""" +
                f""" Phone: {i['phone_number']}"""
            )

        scroll = input(
            "Enter '<' to scroll left, '>' to scroll right or '0' to cancel:\n"
        )

        if scroll == ">":
            index += 1
            if index > len(result_list) - 1:
                index = 0
            continue

        elif scroll == "<":
            index -= 1
            if index < 0:
                index = len(result_list) - 1
            continue

        elif scroll == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break

        else:
            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.RED + "Invalid input.\n")
            continue


""" Customer Functions End """


""" Booking Functions Start """


def bookings_tables_menu():
    """Display the Bookings / Table Management Menu"""

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
            print(Fore.RED + "Please only enter numbers.\n")
            continue

        if response == 1:
            os.system("cls" if os.name == "nt" else "clear")
            book_table()
            break

        elif response == 2:
            os.system("cls" if os.name == "nt" else "clear")
            tables_return = check_available_tables(0)
            if len(tables_return) > 0:

                print("The following tables are available:\n")
                for table in tables_return:
                    print(
                        Fore.GREEN
                        + f"""Table ID: {table['table_id']}, """ +
                        f"""Number of seats: {table['number_of_seats']}"""
                    )
                print("")
                continue
            else:
                print(Fore.RED + "There are currently no tables available.")
                continue

        elif response == 3:
            check_bookings()

        elif response == 4:
            os.system("cls" if os.name == "nt" else "clear")
            main_menu()
            break

        else:
            print(Fore.RED + "Please insert a valid number.\n")


def book_table():
    """Function to book a table for a specific amount of people"""

    while True:

        try:

            number_of_people = int(
                input("Please enter the number of people: \n")
            )
            break

        except ValueError:

            print(Fore.RED + "Please only enter numbers.\n")
            continue

    """ Check if enough people are added """

    if number_of_people >= 1:

        available_tables = check_available_tables(number_of_people)

        print("The following tables are available:\n")

        table_id_selection = []

        for table in available_tables:
            print(
                Fore.GREEN
                + f"""Table ID: {table['table_id']}, """ +
                f"""Number of seats: {table['number_of_seats']}"""
            )
            table_id_selection.append(table["table_id"])

        if len(available_tables) > 0:

            """Select table ID from the available tables"""

            while True:

                try:
                    table_select = int(
                        input("Please select a table ID or 0 to cancel: \n")
                    )
                    if table_select == 0:
                        os.system("cls" if os.name == "nt" else "clear")
                        break

                except ValueError:
                    print(Fore.RED + "Please only enter numbers.\n")
                    continue
                else:
                    if table_select not in table_id_selection:
                        print(
                            Fore.RED
                            + "A table with that number is not available."
                        )
                        continue
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        break

            if table_select != 0:
                while True:

                    print(
                        """Do you want to book a table for a new customer, """
                        """a registered customer or a guest?"""
                    )
                    print("1. New customer")
                    print("2. Existing customer")
                    print("3. Guest")
                    print(Fore.RED + "4. Cancel")

                    try:
                        choice = int(input("Please insert a number: \n"))

                    except ValueError:
                        print(Fore.RED + "Please only enter numbers.\n")
                        continue

                    if choice == 1:
                        customer = add_customer()

                        if customer is not None:
                            table_booking(
                                customer, table_select, number_of_people
                            )
                            break
                        else:
                            bookings_tables_menu()
                            break

                    if choice == 2:
                        os.system("cls" if os.name == "nt" else "clear")
                        customer = search_customer_attribute()
                        if customer is not None:
                            table_booking(
                                customer, table_select, number_of_people
                            )
                            break
                        else:
                            bookings_tables_menu()
                            break

                    if choice == 3:
                        table_booking("guest", table_select, number_of_people)
                        break

                    if choice == 4:
                        bookings_tables_menu()
                        break

                    else:
                        print(Fore.RED + "Invalid number.")
                        continue
            else:
                bookings_tables_menu()

        else:
            print(
                Fore.RED
                + """There are currently no tables available """
                """for your entered amount of people."""
            )
            bookings_tables_menu()

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.RED + "Number cannot be negative or 0.")
        bookings_tables_menu()


def table_booking(customer, table_select, number_of_people):

    if customer != "guest":

        connection.ping(reconnect=True)
        cursor.execute(
            """INSERT INTO bookings (customer_id, table_id,
            amount_of_people, date, active)
            VALUES (%s, %s, %s, %s, %s)""",
            (
                customer["customer_id"],
                table_select,
                number_of_people,
                datetime.today().strftime("%Y-%m-%d"),
                1,
            ),
        )
        connection.commit()
        cursor.execute(
            "UPDATE tables SET availability = 0 WHERE table_id =%s",
            (table_select,),
        )
        connection.commit()

    else:
        connection.ping(reconnect=True)
        cursor.execute(
            """INSERT INTO bookings (table_id, amount_of_people,
            date, active) VALUES (%s, %s, %s, %s)""",
            (
                table_select,
                number_of_people,
                datetime.today().strftime("%Y-%m-%d"),
                1,
            ),
        )
        connection.commit()
        cursor.execute(
            "UPDATE tables SET availability = 0 WHERE table_id=%s",
            (table_select,),
        )
        connection.commit()

    print(
        Fore.GREEN +
        f"""Booking successfully created for {number_of_people} people. """ +
        """Each guest will receive a cart for their """ +
        f"""seat at table {table_select}."""
    )

    connection.ping(reconnect=True)
    cursor.execute(
        """SELECT SQL_NO_CACHE booking_id
        FROM bookings
        ORDER BY booking_id DESC
        LIMIT 1"""
    )
    last_booking = cursor.fetchone()

    seat_counter = 1

    if customer != "guest":

        for i in range(number_of_people):

            connection.ping(reconnect=True)
            cursor.execute(
                """INSERT INTO cart (customer_id, booking_id, seat_number,
                  table_id, walk_in)
                  VALUES (%s, %s, %s, %s, %s)""",
                (
                    customer["customer_id"],
                    last_booking["booking_id"],
                    seat_counter,
                    table_select,
                    0,
                ),
            )
            seat_counter += 1
            connection.commit()

    else:
        for i in range(number_of_people):

            connection.ping(reconnect=True)
            cursor.execute(
                """INSERT INTO cart (booking_id,
                seat_number, table_id, walk_in)
                VALUES (%s, %s, %s, %s)""",
                (last_booking["booking_id"], seat_counter, table_select, 0),
            )
            connection.commit()

    bookings_tables_menu()


def check_available_tables(number_of_people):

    connection.ping(reconnect=True)
    cursor.execute(
        """SELECT SQL_NO_CACHE *
        FROM tables
        WHERE availability=%s
        AND number_of_seats >= %s""",
        (1, number_of_people),
    )
    tables_available = cursor.fetchall()

    return tables_available


def check_bookings():
    """Function to check open bookings"""

    connection.ping(reconnect=True)
    cursor.execute("SELECT SQL_NO_CACHE * FROM bookings WHERE active=%s", (1,))
    bookings = cursor.fetchall()

    if len(bookings) > 0:

        os.system("cls" if os.name == "nt" else "clear")

        print("The following bookings are currently open:\n")

        for booking in bookings:
            print(
                Fore.GREEN +
                f"""Booking ID: {booking['booking_id']}, """ +
                f"""Customer ID: {booking['customer_id']}, """ +
                f"""Table ID: {booking['table_id']}, Amount of """ +
                f"""people: {booking['amount_of_people']}"""
            )

        print("")

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.RED + "No bookings found.")


""" Booking Functions End"""

""" Sale Functions Start """


def sales_carts_menu():
    """Display the Sales / Carts Management Menu"""

    print("You entered the Sales / Carts Management System.\n")
    print("")

    while True:

        print("+------- SALES / CARTS -------+")
        print("|                             |")
        print("| 1. Add product to cart      |")
        print("| 2. Walk-in purchases        |")
        print("| 3. Remove product from cart |")
        print("| 4. Complete purchase        |")
        print("| 5. View Sales               |")
        print("| 6. Main Menu                |")
        print("|                             |")
        print("-------------------------------")
        print("")

        """ Get input and check for errors and invalid numbers """

        try:
            response = int(input("Please select a topic: \n"))

        except ValueError:
            print(Fore.RED + "Please only enter numbers.\n")
            continue

        if response == 1:

            cart = select_cart()
            if cart is not None:
                product = get_product_list()
                if product is not None:
                    if product["available_amount"] > 0:
                        add_product_to_cart(cart, product)
                    else:
                        print(Fore.RED + "Not enough products left.")
                        continue
                else:
                    continue
            else:
                print(Fore.RED + "No cart selected.")
                continue

        elif response == 2:

            while True:

                print(
                    """Do you want to create a new walk-in """
                    """cart or remove an exisiting one?"""
                )
                print("1. Create new walk-in cart")
                print("2. Remove exisiting walk-in cart")
                print("3. Cancel")

                try:
                    walk_input = int(input("Please select a number:\n"))

                except ValueError:
                    print(Fore.RED + "Please only use numbers.\n")
                    continue

                if walk_input == 1:
                    connection.ping(reconnect=True)
                    cursor.execute(
                        "INSERT INTO cart (walk_in) VALUES (%s)", (1,)
                    )
                    connection.commit()
                    cursor.execute(
                        """SELECT SQL_NO_CACHE cart_id
                        FROM cart
                        ORDER BY cart_id DESC
                        LIMIT 1"""
                    )
                    last_cart = cursor.fetchone()
                    print(
                        Fore.GREEN +
                        """Successfully created cart """ +
                        f"""{last_cart['cart_id']} for walk-in customer."""
                    )

                    add_walk_in_items(last_cart)
                    break

                elif walk_input == 2:
                    connection.ping(reconnect=True)
                    cursor.execute(
                        """SELECT SQL_NO_CACHE *
                        FROM cart
                        WHERE walk_in=%s
                        AND payed=%s""",
                        (1, 0),
                    )
                    walk_in_carts = cursor.fetchall()
                    walk_in_ids = []

                    if len(walk_in_carts) > 0:

                        print(
                            "The following walk-in carts are currently open:\n"
                        )

                        for cart in walk_in_carts:
                            print(f"Cart ID: {cart['cart_id']}")
                            walk_in_ids.append(cart["cart_id"])

                        while True:
                            try:
                                selection = int(
                                    input(
                                        """Please enter a cart ID to"""
                                        """ remove or 0 to cancel: \n"""
                                    )
                                )

                            except ValueError:
                                print(Fore.RED + "Please only use numbers.\n")
                                continue

                            if selection == 0:
                                break

                            elif selection in walk_in_ids:
                                remove_walk_in_cart(selection)
                                break

                            else:
                                print(Fore.RED + "Invalid input.")
                                continue

                    else:
                        print(
                            Fore.RED
                            + "There are currently no open walk-in carts."
                        )
                        continue

                elif walk_input == 3:
                    break

                else:
                    print(Fore.RED + "Invalid input.")
                    continue

        elif response == 3:

            cart = select_cart()
            if cart is not None:
                remove_product_from_cart(cart)
                break
            else:
                print(Fore.RED + "No cart selected.")
                continue

        elif response == 4:

            while True:

                print("Do you want to finish a booking or a walk-in purchase?")
                print("1. Booking purchase")
                print("2. Walk-in purchase")
                print("3. Cancel")

                try:
                    purchase_selection = int(
                        input("Please select a number:\n")
                    )

                except ValueError:
                    print(Fore.RED + "Please only use numbers.\n")
                    continue

                if purchase_selection == 1:
                    complete_purchase("booking")
                    break

                elif purchase_selection == 2:
                    complete_purchase("walk-in")
                    break

                elif purchase_selection == 3:
                    break

                else:
                    print(Fore.RED + "Invalid input.")
                    continue

        elif response == 5:

            get_sales()

        elif response == 6:

            os.system("cls" if os.name == "nt" else "clear")
            main_menu()
            break

        else:
            print(Fore.RED + "Please insert a valid number.\n")


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
            print(Fore.RED + "Please only enter numbers.\n")
            continue

        if selection_input == 1:
            search_type = "booking_id"
            search_value = select_cart_by_value("booking ID")
            break

        if selection_input == 2:
            search_type = "table_id"
            search_value = select_cart_by_value("table ID")
            break

        if selection_input == 3:
            search_type = "walk_in"
            search_value = 1
            break

        if selection_input == 4:
            break

        else:
            print(Fore.RED + "Invalid value.")
            continue

    if selection_input != 4:

        connection.ping(reconnect=True)
        cursor.execute(
            "SELECT SQL_NO_CACHE * FROM cart WHERE payed=0 AND "
            + search_type
            + "=%s",
            (search_value,),
        )
        open_carts = cursor.fetchall()

    else:
        sales_carts_menu()

    if len(open_carts) > 0:

        cart_ids = []

        for cart in open_carts:
            cart_ids.append(cart["cart_id"])

        while True:

            print("The following carts are currently open:\n")

            for cart in open_carts:

                print(
                    Fore.GREEN +
                    f"""Seat number: {cart['seat_number']}: """ +
                    f"""Cart ID: {cart['cart_id']}, Customer ID: """ +
                    f"""{cart['customer_id']}, Booking ID: """ +
                    f"""{cart['booking_id']}"""
                )

            try:
                cart_input = int(
                    input(
                        """Please select a cart ID to add a """
                        """product to or 0 to cancel: \n"""
                    )
                )

            except ValueError:
                print(Fore.RED + "Please only enter numbers.\n")
                continue

            if cart_input == 0:
                break

            elif cart_input in cart_ids:
                selected_cart = next(
                    cart
                    for cart in open_carts
                    if cart["cart_id"] == cart_input
                )
                return selected_cart

            else:
                print(Fore.RED + "Invalid input.")
                continue

    else:
        print(Fore.RED + "No carts found.")
        sales_carts_menu()


def add_product_to_cart(cart, product):
    """Function to add item to cart"""

    while True:

        try:
            amount_input = int(
                input(
                    """How many items do you wish to add? """
                    """Please insert a number or 0 to cancel: \n"""
                )
            )

        except ValueError:
            print(Fore.RED + "Please only use numbers.\n")
            continue

        if amount_input == 0:
            break

        elif amount_input < 0:
            print(Fore.RED + "Amount cannot be negative.")
            continue

        elif amount_input > product["available_amount"]:
            print(
                Fore.RED +
                """Not enough items left. The amount of the product """ +
                f"""{product['name']} is {product['available_amount']}."""
            )
            continue

        else:

            products_added = []

            connection.ping(reconnect=True)
            cursor.execute(
                """SELECT SQL_NO_CACHE product_id
                FROM cart_items
                WHERE cart_id=%s""",
                (cart["cart_id"],),
            )

            product_added = cursor.fetchall()

            for i in product_added:
                products_added.append(i["product_id"])

            if product["product_id"] in products_added:

                connection.ping(reconnect=True)
                cursor.execute(
                    """UPDATE cart_items
                    SET product_amount = product_amount + %s
                    WHERE product_id=%s
                    AND cart_id=%s""",
                    (amount_input, product["product_id"], cart["cart_id"]),
                )
                connection.commit()
                cursor.execute(
                    """UPDATE products
                    SET available_amount=available_amount - %s
                    WHERE product_id=%s""",
                    (amount_input, product["product_id"]),
                )
                connection.commit()
                print(
                    Fore.GREEN
                    + f"""{product['name']} was added {amount_input} """ +
                    f"""times to cart {cart['cart_id']}."""
                )
                break

            else:

                connection.ping(reconnect=True)
                cursor.execute(
                    """INSERT INTO cart_items (cart_id, product_id,
                    product_amount)
                    VALUES (%s, %s, %s)""",
                    (cart["cart_id"], product["product_id"], amount_input),
                )
                connection.commit()
                cursor.execute(
                    """UPDATE products
                    SET available_amount=available_amount - %s
                    WHERE product_id=%s""",
                    (amount_input, product["product_id"]),
                )
                connection.commit()
                print(
                    Fore.GREEN +
                    f"""{product['name']} was added {amount_input} """ +
                    f"""times to cart {cart['cart_id']}."""
                )
                break


def remove_product_from_cart(cart):
    """Function to remove product from cart"""

    connection.ping(reconnect=True)
    cursor.execute(
        """SELECT SQL_NO_CACHE cart_items.cart_id, cart_items.product_id,
        cart_items.product_amount, products.name
        FROM cart_items
        LEFT JOIN products
        ON cart_items.product_id = products.product_id
        WHERE cart_items.cart_id=%s""",
        (cart["cart_id"],),
    )
    items_in_cart = cursor.fetchall()

    """ Check if items are in cart """

    if len(items_in_cart) > 0:

        item_ids = []

        print(f"Inside cart {cart['cart_id']}, there are the following items:")

        for item in items_in_cart:
            print(
                Fore.GREEN +
                f"""Product ID: {item['product_id']}, """ +
                """Product name: {item['name']}, Product """ +
                """amount: {item['product_amount']}"""
            )
            item_ids.append(item["product_id"])

        while True:

            try:

                remove_input = int(
                    input(
                        """Please select the item ID of the """
                        """product to remove or 0 to cancel:\n"""
                    )
                )

            except ValueError:
                print("Please use only numbers.\n")
                continue

            if remove_input == 0:
                break

            elif remove_input in item_ids:
                remove_item(cart, remove_input)
                break

            else:
                print(Fore.RED + "Invalid input.")
                continue

    else:

        print(Fore.RED + "Cart is empty.")
        sales_carts_menu()


def remove_item(cart, product_id):
    """Function to remove item from cart"""

    connection.ping(reconnect=True)
    cursor.execute(
        """SELECT SQL_NO_CACHE *
        FROM cart_items
        WHERE product_id=%s
        AND cart_id=%s""",
        (product_id, cart["cart_id"]),
    )
    product_in_cart = cursor.fetchone()

    while True:

        try:
            amount_input = int(
                input("Please enter the amount to remove or 0 to cancel:\n")
            )

        except ValueError:
            print(Fore.RED + "Please only use numbers.\n")
            continue

        if amount_input == 0:
            break

        elif amount_input < 0:
            print(Fore.RED + "Amount cannot be negative")
            continue

            """ Check the amount of products to remove """

        elif amount_input > product_in_cart["product_amount"]:
            print(
                Fore.RED
                + f"""You tried to remove {amount_input} items, """ +
                f"""but only {product_in_cart['product_amount']} """ +
                """are available."""
            )
            connection.ping(reconnect=True)
            cursor.execute(
                """UPDATE products
                SET available_amount = available_amount + %s
                WHERE product_id=%s""",
                (product_in_cart["product_amount"], product_id),
            )
            cursor.execute(
                "DELETE FROM cart_items WHERE product_id=%s AND cart_id=%s",
                (product_id, cart["cart_id"]),
            )
            connection.commit()
            print(
                Fore.GREEN +
                """Removed all products with ID """ +
                f"""{product_id} from cart {cart['cart_id']}."""
            )
            break

        elif amount_input == product_in_cart["product_amount"]:
            connection.ping(reconnect=True)
            cursor.execute(
                """UPDATE products
                SET available_amount = available_amount + %s
                WHERE product_id=%s""",
                (product_in_cart["product_amount"], product_id),
            )
            cursor.execute(
                "DELETE FROM cart_items WHERE product_id=%s AND cart_id=%s",
                (product_id, cart["cart_id"]),
            )
            connection.commit()
            print(
                Fore.GREEN +
                f"""Removed all products with ID {product_id} """ +
                f"""from cart {cart['cart_id']}."""
            )
            break

        else:
            connection.ping(reconnect=True)
            cursor.execute(
                """UPDATE products
                SET available_amount = available_amount + %s
                WHERE product_id=%s""",
                (amount_input, product_id),
            )
            cursor.execute(
                """UPDATE cart_items
                SET product_amount = product_amount - %s
                WHERE product_id=%s
                AND cart_id=%s""",
                (amount_input, product_id, cart["cart_id"]),
            )
            connection.commit()
            print(
                Fore.GREEN
                + f"""Removed item {product_id} {amount_input} """ +
                """times from cart {cart['cart_id']}."""
            )
            break


def select_cart_by_value(callable_value):
    """Function to search cart by a specific attribute"""

    while True:
        try:
            value_input = int(
                input("Please input a " + callable_value + " to search by:\n")
            )

        except ValueError:
            print(Fore.RED + "Please only enter numbers.\n")
            continue

        if value_input == 0:
            break

        else:
            return value_input


def add_walk_in_items(cart_id):
    """Function to add items to cart of walk-in customer / """
    """Ask repeatatly for more additions"""

    while True:

        decision = input(
            """Do you want to add a product to cart """ +
            f"""{cart_id['cart_id']}? [y/n]\n"""
        )

        if decision.lower() == "y":
            product = get_product_list()
            if product is not None:
                add_product_to_cart(cart_id, product)
            else:
                print(Fore.RED + "No product selected.")
                continue

        elif decision.lower() == "n":
            break

        else:
            print(Fore.RED + "Invalid input.")
            continue


def remove_walk_in_cart(cart_id):
    """Function to remove a walk-in cart"""

    connection.ping(reconnect=True)
    cursor.execute(
        "SELECT SQL_NO_CACHE * FROM cart_items WHERE cart_id=%s AND payed=%s",
        (cart_id, 0),
    )
    cart_data = cursor.fetchall()

    """ Check if there are still items in the cart """

    if len(cart_data) > 0:

        while True:

            choice = input(
                Fore.RED
                + f"""There are still items in cart {cart_id}. """ +
                """Do you still want to continue? [y/n]\n"""
            )

            if choice.lower() == "y":
                connection.ping(reconnect=True)
                cursor.execute(
                    "DELETE FROM cart_items WHERE cart_id=%s", (cart_id,)
                )
                cursor.execute("DELETE FROM cart WHERE cart_id=%s", (cart_id,))
                connection.commit()
                print(
                    Fore.GREEN
                    + f"""Cart {cart_id} and all of the items """ +
                    """inside have been removed."""
                )
                break

            elif choice.lower() == "n":
                print(Fore.GREEN + f"Deletion of cart {cart_id} cancelled.")
                break

            else:
                print(Fore.RED + "Invalid input.")
                continue
    else:
        connection.ping(reconnect=True)
        cursor.execute("DELETE FROM cart WHERE cart_id=%s", (cart_id,))
        connection.commit()
        print(Fore.GREEN + f"Cart {cart_id} has successfully been removed.")


def complete_purchase(purchase_type):
    """Function to complete a purchase based on the type provided"""

    if purchase_type == "walk-in":
        connection.ping(reconnect=True)
        cursor.execute(
            """SELECT SQL_NO_CACHE *
            FROM cart
            WHERE walk_in=%s
            ORDER BY cart_id ASC""",
            (1,),
        )
        walk_in_carts = cursor.fetchall()
        walk_in_ids = []

        """ Check if there are walk-in carts available """

        if len(walk_in_carts) > 0:

            print(
                """The following walk-in carts are currently """
                """open(newst entry on bottom):"""
            )

            for cart in walk_in_carts:
                print(Fore.GREEN + f"Cart ID: {cart['cart_id']}")
                walk_in_ids.append(cart["cart_id"])

            while True:

                try:
                    decision = int(
                        input(
                            """Please enter a cart ID to complete or"""
                            """ 0 to cancel:\n"""
                        )
                    )

                except ValueError:
                    print(Fore.RED + "Please only use numbers.\n")
                    continue

                if decision == 0:
                    break

                elif decision in walk_in_ids:
                    complete_purchase_by_cart_id(decision)
                    break

                else:
                    print(Fore.RED + "Invalid input.")
                    continue

        else:
            print(Fore.RED + "There are currently no walk-in carts open.")

    elif purchase_type == "booking":

        connection.ping(reconnect=True)
        cursor.execute(
            """SELECT SQL_NO_CACHE *
            FROM bookings
            WHERE active = %s
            ORDER BY table_id ASC""",
            (1,),
        )
        bookings = cursor.fetchall()
        booking_ids = []

        """ Check if there are open bookings """

        if len(bookings) > 0:

            print("The following bookings are currently open:\n")

            for booking in bookings:
                print(
                    Fore.GREEN
                    + f"""Booking ID: {booking['booking_id']}, """ +
                    f"""Customer ID: {booking['customer_id']}, """ +
                    f"""Table ID: {booking['table_id']}, """ +
                    f"""Amount of people: {booking['amount_of_people']}, """ +
                    f"""Date: {booking['date']}\n"""
                )
                booking_ids.append(booking["booking_id"])

            while True:

                try:

                    decision = int(
                        input("Please enter a Booking ID or 0 to cancel: \n")
                    )

                except ValueError:

                    print(Fore.RED + "Please only use numbers.\n")
                    continue

                if decision == 0:
                    break

                if decision in booking_ids:
                    complete_purchase_booking(decision)
                    break

                else:
                    print(Fore.RED + "Invalid input.")
                    continue

        else:
            print("There are currently no open bookings.")


def complete_purchase_by_cart_id(cart):
    """Function to complete a walk-in purchase"""

    connection.ping(reconnect=True)
    cursor.execute(
        """SELECT SQL_NO_CACHE cart_items.cart_id, cart_items.product_id,
        cart_items.product_amount, products.name, products.price
        FROM cart_items
        LEFT JOIN products
        ON cart_items.product_id = products.product_id
        WHERE cart_items.cart_id=%s""",
        (cart,),
    )
    purchase_data = cursor.fetchall()
    total_price = 0

    print(f"The following items are in cart {cart}:\n")

    for item in purchase_data:
        print(
            Fore.GREEN
            + f"""Product ID: {item['product_id']}, """ +
            f"""Product name: {item['name']}, """ +
            f"""Amount: {item['product_amount']}, """ +
            f"""Price: ${item['price']}"""
        )
        total_price += item["price"] * item["product_amount"]

    print(Fore.YELLOW + f"The total price is: ${total_price:.2f}.")

    while True:
        try:
            received = float(
                input("Please insert money received or 0 to cancel: \n")
            )

        except ValueError:
            print(Fore.RED + "Please only use numbers.\n")
            continue

        if received == 0:
            break

        elif received < 0:
            print(Fore.RED + "Amount cannot be negative.")
            continue

        elif received < total_price:
            print(Fore.RED + f"Not enough money. The sum is {total_price:.2f}")
            continue

        elif received >= total_price:
            return_amount = received - total_price
            connection.ping(reconnect=True)
            cursor.execute(
                "INSERT INTO sold_products (cart_id, date) VALUES (%s, %s)",
                (cart, datetime.today().strftime("%Y-%m-%d")),
            )
            cursor.execute("DELETE FROM cart_items WHERE cart_id=%s", (cart,))
            cursor.execute(
                "UPDATE cart SET payed=%s WHERE cart_id=%s", (1, cart)
            )
            connection.commit()
            print(
                Fore.GREEN
                + f"""Cart {cart} successfully payed. """ +
                f"""The return money is ${return_amount:.2f}."""
            )

            break

        else:
            print(Fore.RED + "Invalid input.")
            continue


def complete_purchase_booking(booking_id):
    """Function to complete a purchase from booking"""

    connection.ping(reconnect=True)
    cursor.execute(
        "SELECT SQL_NO_CACHE * FROM cart WHERE booking_id=%s", (booking_id,)
    )
    booking_carts = cursor.fetchall()

    if len(booking_carts) > 0:

        booking_carts_id = []
        price = float(0)

        """ Get cart IDs available in the current booking """

        for booking in booking_carts:
            booking["cart_id"] = int(booking["cart_id"])
            booking_carts_id.append(booking["cart_id"])

        guests = []

        """ Get a list of guests in the booking """

        for id in booking_carts_id:
            connection.ping(reconnect=True)
            cursor.execute(
                """SELECT SQL_NO_CACHE cart_items.cart_id,
                cart_items.product_id, cart_items.product_amount,
                products.name, products.price
                FROM cart_items
                LEFT JOIN products
                ON cart_items.product_id = products.product_id
                WHERE cart_id=%s""",
                (id,),
            )
            result = cursor.fetchall()
            guests.append(result)

        bought_products = []

        """ Create a list of items the guests purchased """

        for guest in guests:
            for i in guest:
                bought_products.append(i)

        """ Check if people bought items """

        if len(bought_products) > 0:

            print("The following items were purchased:\n")

            for product in bought_products:
                print(
                    Fore.GREEN
                    + f"""Cart ID: {product['cart_id']}, """ +
                    f"""{product['product_amount']}x {product['name']}, """ +
                    f"""(ID: {product['product_id']}, Price: """ +
                    f"""{product['price']})"""
                )
                price += product["price"] * product["product_amount"]

            get_money(
                price,
                booking_carts_id,
                booking_carts[0]["customer_id"],
                booking_carts[0]["table_id"],
                booking_id,
            )

        else:
            print(Fore.RED + "Nobody bought anything.")

    else:
        print(Fore.RED + "No carts found.")


def get_money(price, ids, customer_id, table_id, booking_id):
    """Function to complete purchase and enter data into """
    """table sold_products / """
    """Check if given amount of money is correct"""

    while True:

        print(f"The total price is: ${price:.2f}.")

        try:
            received = float(
                input("Please insert money received or 0 to cancel: \n")
            )

        except ValueError:
            print(Fore.RED + "Please only use numbers.\n")
            continue

        if received == 0:
            break

        elif received < 0:
            print(Fore.RED + "Amount cannot be negative.")
            continue

        elif received < price:
            print(Fore.RED + f"Not enough money. The sum is ${price:.2f}")
            continue

        elif received >= price:

            """Calculate money to give back to the customers"""

            return_amount = received - price

            """ Insert data into database and mark carts and bookings """
            """ as complete / Re-enable tables """

            for id in ids:

                connection.ping(reconnect=True)
                cursor.execute(
                    """INSERT INTO sold_products (cart_id, customer_id, date)
                    VALUES (%s, %s, %s)""",
                    (id, customer_id, datetime.today().strftime("%Y-%m-%d")),
                )
                cursor.execute(
                    "DELETE FROM cart_items WHERE cart_id=%s", (id,)
                )
                cursor.execute(
                    "UPDATE cart SET payed=%s WHERE cart_id=%s", (1, id)
                )
                connection.commit()

            connection.ping(reconnect=True)
            cursor.execute(
                "UPDATE bookings SET active=%s WHERE booking_id=%s",
                (0, booking_id),
            )
            cursor.execute(
                "UPDATE tables SET availability=%s WHERE table_id=%s",
                (1, table_id),
            )
            connection.commit()

            print(
                Fore.GREEN +
                f"""Booking {booking_id} successfully payed. """ +
                f"""The return money is ${return_amount:.2f}."""
            )
            print(
                Fore.GREEN +
                f"Table {table_id} is now again available for guests."
            )

            break

        else:
            print(Fore.RED + "Invalid input.")
            continue


def get_sales():
    """Function to get a list of all sales completed"""

    connection.ping(reconnect=True)
    cursor.execute(
        "SELECT SQL_NO_CACHE * FROM sold_products ORDER BY sale_id ASC"
    )
    sales_data = cursor.fetchall()

    """ Check if there are any sales """

    if len(sales_data) > 0:

        print("The following sales were found:")

        for sale in sales_data:
            print(
                Fore.GREEN
                + f"""Sale ID: {sale['sale_id']}, """ +
                f"""Cart ID: {sale['cart_id']}, """ +
                f"""Customer ID: {sale['customer_id']}, """ +
                f"""Date: {sale['date']}"""
            )

    else:
        print(Fore.RED + "There are no sales.")


""" Sale Functions End """


""" Product Functions Start """


def products_menu():
    """Display the Products Management Menu"""

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
            print(Fore.RED + "Please only enter numbers.\n")
            continue

        if response == 1:
            add_product()

        elif response == 2:
            product = get_product_list()
            if product is not None:
                update_product(product)
                break
            else:
                continue

        elif response == 3:
            get_product_list(True)
            continue

        elif response == 4:
            os.system("cls" if os.name == "nt" else "clear")
            main_menu()
            break

        else:
            print("Please insert a valid number.\n")


def add_product():
    """Function to add a product based on input type"""

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
            print(Fore.RED + "Please only use numbers.\n")
            continue

        if product_add_input == 1:

            add_product_by_category("cake", "cake")
            break

        if product_add_input == 2:
            add_product_by_category("cookie", "cookie")
            break

        if product_add_input == 3:
            add_product_by_category("main dish", "main dish")
            break

        if product_add_input == 4:
            add_product_by_category("drink", "drink")
            break

        if product_add_input == 5:
            break

        else:
            print(Fore.RED + "Invalid input.")
            continue


def add_product_by_category(value, callable_value):
    """Add product details and insert data into database"""

    while True:

        name_input = input(
            f"""Please insert the name of the {callable_value} to add """ +
            """or 0 to cancel: \n"""
        )

        name_input = name_input.title()

        connection.ping(reconnect=True)
        cursor.execute(
            "SELECT SQL_NO_CACHE name FROM products WHERE name=%s",
            (name_input,),
        )
        check_result = cursor.fetchall()

        """ Check if product name is already in use """

        if len(check_result) > 0:
            print(
                Fore.RED
                + "This name is already in use. Please choose another one."
            )
            continue

        if name_input == "0":
            break

        try:

            amount_input = int(
                input("Please insert the stock amount or 0 to cancel: \n")
            )

        except ValueError:
            print(Fore.RED + "Please only use numbers.\n")
            continue

        if amount_input == 0:
            break

        if amount_input < 0:
            print(Fore.RED + "Number cannot be negative.")
            continue

        pattern = r"^\d+\.\d{2}$"

        try:

            price_input = input("Please enter the price or 0 to cancel: \n")

        except ValueError:

            print(Fore.RED + "Please enter a floating-point number.")

        if price_input == "0":
            break

        """ Check if price format is correct """

        if re.fullmatch(pattern, price_input) is None:
            print(Fore.RED + "Wrong format. Example: 4.99")
            continue

        connection.ping(reconnect=True)
        cursor.execute(
            """INSERT INTO products (name, category, available_amount, price)
            VALUES (%s, %s, %s, %s)""",
            (name_input, value, amount_input, float(price_input)),
        )
        connection.commit()

        print(Fore.GREEN + "Product successfully added to database.")
        break


def get_product_list(view_only=False):
    """Get a list of products based on category"""

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
            print(Fore.RED + "Please only use numbers.\n")
            continue

        if product_input == 1:
            product = get_product_by_category("cake", "cake", view_only)
            if product is not None:
                return product
            else:
                return None

        elif product_input == 2:
            product = get_product_by_category("cookie", "cookie", view_only)
            if product is not None:
                return product
            else:
                return None

        elif product_input == 3:
            product = get_product_by_category(
                "main dish", "main dish", view_only
            )
            if product is not None:
                return product
            else:
                return None

        elif product_input == 4:
            product = get_product_by_category("drink", "drink", view_only)
            if product is not None:
                return product
            else:
                return None

        elif product_input == 5:
            break

        else:
            print(Fore.RED + "Invalid input.")


def get_product_by_category(value, callable_value, view_only):
    """Function to select a product based on given values /
    Check if item will be used or just viewed with view_only"""

    connection.ping(reconnect=True)
    cursor.execute(
        "SELECT SQL_NO_CACHE * FROM products WHERE category=%s", (value,)
    )
    result = cursor.fetchall()
    product_ids = []

    for product in result:
        product_ids.append(product["product_id"])

    if len(result) > 0:

        result_list = [result[i: i + 10] for i in range(0, len(result), 10)]
        index = 0

        while True:

            print("+------- PRODUCT OVERVIEW -------+\n")

            print(Fore.YELLOW + f"Page {index + 1} / {len(result_list)}\n")

            for i in result_list[index]:

                print(
                    Fore.GREEN
                    + f"""ID: {i['product_id']}, """ +
                    f"""Name: {i['name']}, """ +
                    f"""Available amount: {i['available_amount']}, """ +
                    f"""Price: {i['price']}"""
                )

            scroll = input(
                """Enter '<' to scroll left, '>' to scroll right """
                """or '0' to continue:\n"""
            )

            if scroll == ">":
                index += 1
                if index > len(result_list) - 1:
                    index = 0
                continue

            elif scroll == "<":
                index -= 1
                if index < 0:
                    index = len(result_list) - 1
                continue

            elif scroll == "0":
                break

            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(Fore.RED + "Invalid input.\n")
                continue

        if view_only is False:

            while True:

                try:
                    selection = int(
                        input(
                            "Please select a product by ID or 0 to cancel: \n"
                        )
                    )

                except ValueError:
                    print(Fore.RED + "Please only use numbers.\n")
                    continue

                if selection == 0:
                    break

                elif selection in product_ids:
                    connection.ping(reconnect=True)
                    cursor.execute(
                        """SELECT SQL_NO_CACHE *
                        FROM products
                        WHERE product_id=%s""",
                        (selection,),
                    )
                    product_return = cursor.fetchone()
                    print(
                        Fore.GREEN + f"You selected {product_return['name']}."
                    )
                    return product_return

                else:
                    print(Fore.RED + "No product with that number available.")
                    continue

    else:
        print(Fore.RED + "No product has been found in that category.")
        return None


def update_product(product):
    """Function to change a product based on input"""

    while True:
        print(
            f"""Which attribute of {product['name']} """ +
            f"""(ID: {product['product_id']}) do you want to change?"""
        )
        print("1. Name")
        print("2. Category")
        print("3. Price")
        print("4. Amount")
        print("5. Cancel")

        try:
            update_input = int(input("Please select a number: \n"))

        except ValueError:
            print(Fore.RED + "Please only use numbers.\n")
            continue

        if update_input == 1:
            update_product_by_value(product, "name", "name")
            break

        if update_input == 2:
            update_product_by_value(product, "category", "category")
            break

        if update_input == 3:
            update_product_by_value(product, "price", "price")
            break

        if update_input == 4:
            update_product_by_value(product, "available_amount", "amount")
            break

        if update_input == 5:
            products_menu()
            break


def update_product_by_value(product, value, callable_value):
    """Function to change product values"""

    categories = ["cake", "cookie", "main dish", "drink"]

    while True:

        update_input = input(
            f"""Please enter the new {callable_value} for """ +
            f"""{product['name']} or type cancel to cancel:\n"""
        )

        if update_input == "cancel":
            products_menu()
            break

        if value == "name":

            connection.ping(reconnect=True)
            cursor.execute(
                "UPDATE products SET name=%s WHERE product_id=%s",
                (update_input.title(), product["product_id"]),
            )
            connection.commit()
            print(
                Fore.GREEN
                + f"""Name of {product['name']} was successfully changed """ +
                f"""to {update_input.title()}."""
            )
            break

        elif value == "category":

            if update_input.lower() in categories:
                connection.ping(reconnect=True)
                cursor.execute(
                    "UPDATE products SET category=%s WHERE product_id=%s",
                    (update_input.lower(), product["product_id"]),
                )
                connection.commit()
                print(
                    Fore.GREEN +
                    f"""Product {product['name']}'s {callable_value} """ +
                    f"""was successfully changed to {update_input}."""
                )
                break

            else:

                print(
                    Fore.RED +
                    """Please only use the categories cake, """
                    """cookie, main dish or drink."""
                )
                continue

        elif value == "price":

            """Check for price pattern"""

            pattern = r"^-?(0|\d+)\.\d{2}$"

            if re.fullmatch(pattern, update_input) is None:
                print(Fore.RED + "Wrong format. Example: 4.99")
                continue

            float(update_input)

            if float(update_input) <= 0:
                print(Fore.RED + "The value cannot be 0 or negative.")
                continue

            else:
                connection.ping(reconnect=True)
                cursor.execute(
                    "UPDATE products SET price=%s WHERE product_id=%s",
                    (update_input, product["product_id"]),
                )
                connection.commit()
                print(
                    Fore.GREEN
                    + f"""Price of {product['name']} successfully """ +
                    f"""updated to ${update_input}."""
                )
                break

        elif value == "available_amount":

            try:
                update_input = int(update_input)
            except ValueError:
                print(Fore.RED + "Please only use whole numbers.\n")
                continue

            if update_input < 0:
                print(Fore.RED + "A negative amount is not allowed.")

            else:
                connection.ping(reconnect=True)
                cursor.execute(
                    """UPDATE products
                    SET available_amount=%s
                    WHERE product_id=%s""",
                    (update_input, product["product_id"]),
                )
                connection.commit()
                print(
                    Fore.GREEN
                    + f"""Available amount of {product['name']} """ +
                    """successfully updated to {update_input}."""
                )
                break


""" Product Functions End """


""" Main Cycle Start """


def main():
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        pw_input = input(
            Fore.YELLOW
            + "Please enter password to access management program:\n"
        )
        print("")

        if pw_input == admin_access:
            main_menu()
            break
        else:
            print(Fore.RED + "Wrong password.")
            continue


""" Main Cycle End """


""" Call Main Cycle """


main()
