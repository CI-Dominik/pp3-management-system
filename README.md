# Restaurant Management System
This restaurant management system was designed to manage the data of customers, products, sales, bookings and tables of a client's business.

The live system can be viewed here: [Link to the Restaurant Management System](https://pp3-management-system-30090303934b.herokuapp.com/ "Link to the live website")

![Mockup image of the Restaurant Management System](docs/mockup.jpg)

---

## **TABLE OF CONTENTS**

[**BRIEFING**](#briefing)
  * PH

<br>

[**PLANNING**](#planning)
  * PH

<br>

[**USER EXPERIENCE**](#user-experience)
  * PH
    
<br>

[**FEATURES**](#features)
  * PH

<br>

[**MENU STRUCTURE**](#menu-structure)
  * PH
    
<br>

[**TECHNOLOGIES**](#technologies)
  * [Python](#python)
  * [MySQL](#mysql)
  * [MySQL Connector](#mysql-connector)
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
  * PH
    
<br>

[**VALIDATOR TESTING**](#validator-testing)
  * [PEP8 Linter](#pep8-linter)

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
    
<br>

[**CREDITS**](#credits)
  * [Techsini](#techsini)
  * [PEP8 Linter](#pep8-linter-1)
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

## Heading
* PH

<br>

![Screenshot ---------------------------------](docs/---------------------------------.jpg)

---

## **MENU STRUCTURE**

## Heading
* PH

<br>

![Screenshot ---------------------------------](docs/---------------------------------.jpg)

---

## **TECHNOLOGIES**

### Python
* Python was used to create the program's logic

### MySQL
* MySQL was used to deploy a database to access all needed pieces of information.

### MySQL Connector
* The Python module mysql-connector was used to connect to the MySQL database and display errors for bugfixing.

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

## Heading

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| TEXT | TEXT | TEXT |
| TEXT | TEXT | TEXT |
| TEXT | TEXT | TEXT |

![Screenshot ---------------------------------](docs/---------------------------------.jpg)

---

## **VALIDATOR TESTING**

### PEP8 Linter
* The code was checked for errors using PEP8 Linter. No errors occured while testing.

<br>

![Screenshot ---------------------------------](docs/---------------------------------.jpg)

---

## **BUGS**

## Unfixed bugs
* PH

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

PH ---------------------------------

---

## **CREDITS**

## [Techsini](https://techsini.com/multi-mockup/index.php)
* Used to create the mockup in the readme file.

## [PEP8 Linter](https://pypi.org/project/pep8/)
* Used to verify Python code.

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