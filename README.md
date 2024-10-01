# Restaurant Management System
This restaurant management system was designed to manage the data of customers, products, sales, bookings and tables of a client's business.

The live system can be viewed here: [Link to the Restaurant Management System](https://pp3-management-system-30090303934b.herokuapp.com/ "Link to the live website")

---

## **TABLE OF CONTENTS**

[**BRIEFING**](#briefing)
  * [Happy Life's Management System](#happy-lifes-management-system)
  * [Management of customers](#management-of-customers)
  * [Bookings](#bookings)
  * [Sales](#sales)
  * [Products](#products)

<br>

[**PLANNING**](#planning)
  * [The needs for Happy Life's management system](#the-needs-for-happy-lifes-management-system)

<br>

[**USER EXPERIENCE**](#user-experience)
  * [Easy access and clear division](#easy-access-and-clear-division)
    
<br>

[**FEATURES**](#features)
  * [Main Menu](#main-menu)
  * [Customers Menu](#customers-menu)
  * [Bookings / Tables Menu](#bookings--tables-menu)
  * [Sales / Carts Menu](#sales--carts-menu)
  * [Products Menu](#products-menu)

[**STRUCTURING**](#structuring)
  * [Database Structure](#database-structure)
  * [Flowchart Structure](#flowchart-structure)
    
<br>

[**TECHNOLOGIES**](#technologies)
  * [Python](#python)
  * [MySQL](#mysql)
  * [MySQL Connector](#mysql-connector)
  * [Pycodestyle (Former PEP8)](#pycodestyle-former-pep8)
  * [Flake8](#flake8)
  * [Black](#black)
  * [OS module](#os-module)
  * [RE module](#re-module)
  * [dotenv](#dotenv)
  * [Colorama](#colorama)
  * [datetime](#datetime)
  * [Visual Studio Code](#visual-studio-code)
  * [GitHub](#github)
  * [All-Inkl](#all-inkl)
    
<br>

[**TESTING**](#testing)
  * [General Testing](#general-testing)
  * [Main Menu Testing](#main-menu-testing)
  * [Customer Management Menu Testing](#customer-management-menu-testing)
  * [Tables / Bookings Menu Testing](#tables--bookings-menu-testing)
  * [Sales / Carts Menu Testing](#sales--carts-menu-testing)
  * [Products Menu Testing](#products-menu-testing)
    
<br>

[**VALIDATOR TESTING**](#validator-testing)
  * [Pycodestyle (Former PEP8)](#pycodestyle-former-pep8-1)

<br>

[**BUGS**](#bugs)
  * [Unfixed bugs](#unfixed-bugs)

<br>

[**DEPLOYMENT**](#deployment)
  * [GitHub](#github-1)
    * [Visual Studio Code connection](#visual-studio-code-connection)
    * [Cloning, committing and pushing via Visual Studio Code](#cloning-committing-and-pushing-via-visual-studio-code)
    * [Deployed page on GitHub](#deployed-page-on-github)
  * [Heroku](#heroku)
    * [Creating a new app](#creating-a-new-app)
    * [Naming the app](#naming-the-app)
    * [Deploy the app](#deploy-the-app)
    * [Configure possible Config Vars](#configure-possible-config-vars)
    * [Add buildpacks to the project](#add-buildpacks-to-the-project)
    * [Select a branch to deploy](#select-a-branch-to-deploy)
    * [Waiting for the project to deploy](#waiting-for-the-project-to-deploy)
    
<br>

[**CREDITS**](#credits)
  * [Pycodestyle (Former PEP8)](#pycodestyle-former-pep8-2)
  * [Black](#black-1)
  * [drawsql](#drawsql)
  * [Lucidchart](#lucidchart)
  * [W3Schools](#w3schools)
  * [YouTube](#youtube)
  * [ChatGPT](#chatgpt)
  * [Visual Studio Code](#visual-studio-code-1)
  * [All-Inkl](#all-inkl-1)

---

## **BRIEFING**

## Happy Life's Management System
* Happy Life, a local coffee shop reached out regarding their plan to implement a management system for their business. As their business is growing, they want to decrease their workload for bureaucratic affairs. Several topics were mentioned that needed improvement.

### Management of customers
* People regularly contact Happy Life to book tables and the company wants to simplify the process. When a potential customer contacts them, they want to be able to register a new customer and edit their information. It should also be possible to assign a person to a table and give the process a booking ID.

### Bookings
* Happy Life's booking system should be able to book a table for a registered customer or guests. It should also take the amount of customers in consideration and reply with open tables for the given amount. The team should always be able to get an overview over the amount of tables available and the bookings made in their system that are not yet finished.

### Sales
* The employees should be able to add a product to a cart that each of their visitors gets assigned, either through a booking or a direct purchase. The removal of said products should also be possible to manage returns and unwanted or unusable items. The purchase should be finished through their system, taking into account the table ID, booking ID and the visitor's carts.

### Products
* Happy Life's product catalog is changing from time to time, so a flexible system should adapt to their needs. It should be possible to add a product to the system, update it, update the stock or check on the amount that is left in their storage.

---

## **PLANNING**

## The needs for Happy Life's management system
* The company has needs that need to be fulfilled, so a strategical planning process was made. The platform will be used by coffee staff only, so the interface should include only management topics as customers will not operate the system. Several categories will simplify and divide the menu into controllable, user-friendly chunks.<br>
A database will save all needed pieces of information as a reliable and secure source. MySQL will be used, as it provides the ability to separate the data into clear columns that have the ability of being nullable or not.<br>
A password should protect the system, in case a customer gets access to the terminal.

---

## **USER EXPERIENCE**

## Easy access and clear division
* The user will immediately be able to complete their needed task without unnecessary pieces of information. A menu with all categories welcomes them. With the help of numbers, the user will be able to navigate through the several menus.<br>
The structure is divided into management for customers, bookings, sales and products. Each of those menus will have their own set of bullet points. For example, in the customer panel, it is possible to add a new customer, edit their data or search for a specific person, based on provided pieces of information like a name, email address or phone number.<br>
To inform the user of possible mistakes, every menu input is secured by catching wrong inputs or wrong types of inputs like texts instead of a whole number.

---

## **FEATURES**

## Main Menu
* The main menu is used as the access point for all sub-menus. From here, the user can reach every stage of the booking or sale progress that they like.

<br>

![Screenshot of the Main Menu](docs/menu_structure/menu_01.jpg)

## Customers menu
* The customers menu is used to search for a customer using data like the name (with possible duplicates but a listing of all customers with that name to choose one), email address, phone number or ID. The user can also insert new data, update them or show a scrollable list of all customers. Deletion of data is prohibited, as all employees get access to the terminal. Such data need to be erased in the MySQL management tool.

<br>

![Screenshot of the Customers menu](docs/menu_structure/menu_02.jpg)

## Bookings / Tables Menu
* In the menu for bookings and tables, the user is able to book a table for either a new customer, an exisiting one or just a guest who does not want to be inside the database. An overview over the available tables is present and open bookings can be displayed. Tables are free again after the purchase is complete.

<br>

![Screenshot of the Bookings and Tables menu](docs/menu_structure/menu_03.jpg)

## Sales / Carts Menu
* The sales and carts menu is used to add a product to an already exisiting cart, walk-in purchases can be completed without the need for a booking, products can be removed from an exisiting cart (also from walk-in carts), purchases can be completed and a list of all sales can be viewed in ascending order.

<br>

![Screenshot of the Sales and Carts Menu](docs/menu_structure/menu_04.jpg)

## Products Menu
* The products menu can be used to add products to the database, update existing products and check the wares in a scrollable list and sorted by category.

<br>

![Screenshot of the Products Menu](docs/menu_structure/menu_05.jpg)

--- 

## **STRUCTURING**

## Database Structure
* All-Inkl was used to host a MySQL database. The structure represents the final variant of the available database for the terminal project.

<br>

![Screenshot of the Database structure](docs/database.jpg)

## Flowchart Structure
* Basic flowcharts of every menu are displayed to lay out the functions of the menu items.

<br>

![Screenshot of Flowchart 01](docs/flowcharts/01-main-menu.jpg)

<br>

![Screenshot of Flowchart 02](docs/flowcharts/02-customer-menu.jpg)

<br>

![Screenshot of Flowchart 03](docs/flowcharts/03-bookings-tables-menu.jpg)

<br>

![Screenshot of Flowchart 04](docs/flowcharts/04-sales-carts-menu.jpg)

<br>

![Screenshot of Flowchart 05](docs/flowcharts/05-products-menu.jpg)

<br>

---

## **TECHNOLOGIES**

### Python
* Python was used to create the program's logic

### MySQL
* MySQL was used to deploy a database to access all needed pieces of information.

### MySQL Connector
* The Python module mysql-connector was used to connect to the MySQL database and display errors for bugfixing.

### Pycodestyle (Former PEP8)
* The pycodestyle module was used to verify the code for pythonic structure.

### Flake8
* The Flake8 extension of Visual Studio Code was used to get a constant feedback about pythonic style.

### Black
* The black module was used to format some of the code.

### OS module
* The Python module os was used to access operating system files.

### RE module
* The RE module was used to check for incorrect inputs for email addresses or phone numbers.

### dotenv
* The Python module dotenv was used to import environmental variables to secure the database login and read the needed data.

### Colorama
* Colorama was used to highlight texts in several colors to give emphasis.

### datetime
* datetime was imported to get the current date and insert it into a database table.

### Visual Studio Code
* Visual Studio Code was used to clone the GitHub repository, edit the homepage's code and commit / push the results to GitHub.

### GitHub
* GitHub was used to store the homepage's files. Everything was deployed using GitHub Pages.

### All-Inkl
* All-Inkl was used to host the MySQL database.

---

## **TESTING**

## General testing (Used in every input)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Entering text into fields that require integer values | An error should appear and return the user to the beginning of the loop | Pass |
| Entering negative values into fields that require positive values | An error should appear and return the user to the beginning of the loop | Pass |
| Entering values outside of the selection range | An error should appear and return the user to the beginning of the loop | Pass |
| Entering numbers, texts and special signs into fields that require "y" or "n" | An error should appear and return the user to the beginning of the loop | Pass |
| Entering a wrong password when starting the program | Access should be denied | Pass |
| Cancelling actions | A previous menu should appear | Pass |

## Main Menu Testing

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Enter all available menus | Access should be granted via numbers | Pass |

## Customer Management Menu Testing

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Entering search menu | Menu should open | Pass |
| Searching for names that are unique | Only one entry should appear formatted | Pass |
| Searching for names that are duplicates | All available options should be listed | Pass |
| Accessing options given | A question if the given information is right | Pass |
| Searching for email addresses, phone numbers and customer IDs | Only unique entries should be displyed | Pass |
| | | |
| Entering add customer menu | Menu should open | Pass |
| Enter first and last names | Entry should lead to next point | Pass |
| Enter email address the right way | Next option should appear | Pass |
| Enter email address the wrong way | An error should appear and lead back to the beginning | Pass |
| Enter phone number correctly | Entry should be written into database | Pass |
| Enter phone number incorrectly | An error should appear and lead back to the beginning | Pass |
| | | |
| Entering update customer menu | Menu should appear | Pass |
| Entering customer data to search | Customers should be listed | Pass |
| Choosing a customer | Approvement message should appear | Pass |
| Changing first or last name | Entry should be written into database | Pass |
| Trying to update email address with right format | Address should be written into database | Pass |
| Trying to update email address with wrong format | An error should appear and lead back | Pass |
| Trying to update phone number with right format | Number should be written into database | Pass |
| Trying to update phone number with wrong format | An error should appear and lead back | Pass |
| | | |


## Tables / Bookings Menu Testing

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| TEXT | TEXT | TEXT |
| TEXT | TEXT | TEXT |
| TEXT | TEXT | TEXT |

## Sales / Carts Menu Testing

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| TEXT | TEXT | TEXT |
| TEXT | TEXT | TEXT |
| TEXT | TEXT | TEXT |

## Products Menu Testing

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| TEXT | TEXT | TEXT |
| TEXT | TEXT | TEXT |
| TEXT | TEXT | TEXT |

---

## **VALIDATOR TESTING**

### Flake8
* The code was checked for errors using the Flake8 extension for Visual Studio Code as a PEP8 control tool. No errors occured while testing the final product.

<br>

![Screenshot of the Flake8 testing](docs/flake8-validation.jpg)

### Pycodestyle (Former PEP8)
* After erasing all bugs pointed out from Flake8, the document was again checked using Pycodestyle. No errors occured.

<br>

![Screenshot of the Pycodestyle testing](docs/pycodestyle-validation.jpg)

---

## **BUGS**

## Unfixed bugs
* When accessing the list of scrollable data, the user first needs to enter 0 to cancel the scrolling before the value can be provided. Many versions were tried but no solution was found to that problem at the time of deployment. This issue needs to be addressed in the future.
* When left unattented for a long time, the Heroku window freezes and needs to be restarted. No fix has been found at the moment of deployment.

---

## **DEPLOYMENT**

## GitHub

### Visual Studio Code connection
* A connection between Visual Studio Code and GitHub was established using the built-in function to include the ability to clone, stage, commit and push content directly to GitHub.
Once you start Visual Studio Code with no connection, you simply need to click on the person icon in the lower left corner and select "GitHub". From there, you can connect your existing account to Visual Studio Code.

<br>

![Screenshot of the menu to connect Visual Studio Code with GitHub](docs/vscode-connection.jpg)

### Cloning, committing and pushing via Visual Studio Code
* Visual Studio code was used to stage all changed files and commit them with an included message directly to GitHub.

<br>

![Screenshot of the menu to commit changes to GitHub](docs/vscode-commit.jpg)

### Deployed page on GitHub
* The system is hosted via Heroku, but still available in the pages menu of GitHub.

![Screenshot of the deployed page in GitHub](docs/deployment-pages.jpg)

## Heroku

### Creating a new app
* In the dashboard, navigate to the button *New* and *Create new app*.

<br>

![Screenshot of Heroku deployment 01](docs/heroku/01.jpg)

### Naming the app
* Give the app a new name and select the host region (US/EU). Then click *Create app*.

<br>

![Screenshot of Heroku deployment 02](docs/heroku/02.jpg)

### Deploy the app
* Click on the *Deploy* button on the top. In the bottom, select the platform on which the code is hosted, select the username and insert the name of the repository. GitHub was chosen here.

<br>

![Screenshot of Heroku deployment 03](docs/heroku/03.jpg)

<br>

![Screenshot of Heroku deployment 04](docs/heroku/04.jpg)

### Configure possible Config Vars
* Config vars are a way to securely store need information for connections like the MySQL connection used in this project. Insert a key and value pair and add it.

<br>

![Screenshot of Heroku deployment 05](docs/heroku/05.jpg)

### Add buildpacks to the project
* Buildpacks are needed to use the Code Institute Python Template. Node.js and Python need to be added for it to work.

<br>

![Screenshot of Heroku deployment 06](docs/heroku/06.jpg)

<br>

![Screenshot of Heroku deployment 07](docs/heroku/07.jpg)

### Select a branch to deploy
* A GitHub branch that should be deployed can be found on the *Deploy* page. Here, the main branch was used to create the project.

<br>

![Screenshot of Heroku deployment 08](docs/heroku/08.jpg)

### Waiting for the project to deploy
* A window with all needed pieces of information will be displayed to inform the user of the current action. After successfully deploying the app, a *View* button will appear. It contains the link to the live site.

<br>

![Screenshot of Heroku deployment 01](docs/heroku/09.jpg)

<br>

![Screenshot of Heroku deployment 10](docs/heroku/10.jpg)

---

## **CREDITS**

## [Pycodestyle (Former PEP8)](https://pypi.org/project/pycodestyle/)
* Used to verify Python code.

## [Black](https://pypi.org/project/black/)
* Used to format the Python code.

## [drawsql](https://drawsql.app/)
* Used to create the database diagram.

## [Lucidchart](https://lucid.app/)
* Used to create flowcharts for the menu structure.

## [W3Schools](https://www.w3schools.com/)
* Used to lookup tips for the code.

## [YouTube](https://youtube.com)
* Videos for understanding some code areas.

## [ChatGPT](https://chatgpt.com/)
* Used for deepening the understanding of some Python and database concepts.

## [Visual Studio Code](https://code.visualstudio.com/)
* Used for code editing.

## [All-Inkl](https://all-inkl.com/)
* Used to host the MySQL database.