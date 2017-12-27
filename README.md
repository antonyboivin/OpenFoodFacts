

## What is it about ?

This project aims to perform manipulation and analysis of large files.
To do this, an application coded in Python will allow a user to select products, so that the program offers another healthier substitute product. The user can then, if he wishes, save his substitution.
The data used are those of the OpenFoodFacts API (https://en.openfoodfacts.org/).


## What features?

* Search for food in the Open Food Facts database.
* The user interacts with the program in the terminal,
* If the user enters a character that is not a digit, the program must repeat the question,
* The search must be done on a MySQL basis.


## what is the user path?

The user is on the terminal. The latter shows him the following choices:
1. Which food do you want to replace?
2. Find my substituted foods.
The user selects 1. The program asks the user the following questions and the user selects the answers:
* Select the category. [Several proposals associated with a number. The user enters the corresponding digit and presses enter]
* Select the food. [Several proposals associated with a number. The user enters the digit corresponding to the selected food and presses enter]
* The program offers a substitute, its description, a store or buy it (if any) and a link to the Open Food Facts page about that food.
* The user then has the possibility to save the result in the database.


## How to use this application?

1. Download the csv file from Openfoodfacts: http://en.openfoodfacts.org/data/en.openfoodfacts.org.products.csv
2. Place this file in the / datas folder
3. Execute musql_db_creator.py
4. Execute offmain.py

# Description of features ...

## ...of the mysql_db_creator.py file:
**csv_parser ():** Allows the reading and analysis of the .csv file to extract the following data: barcode, url, product name, product mark, category to which the product belongs, store where the product is sold, country, the nutritional grade and the nutritional score of the product.

**create_database ():** will create the database, as well as the necessary tables, and then automatically populate these tables if the product belongs to a category with at least 10 products.

## ...of the offmain.py file:
**main_menu ():** Entry point of the application, allows the display of the main menu that will call the different features as and when the user requests.

## ...du fichier displ_app.py :
### class Loop(): 
Contains all methods for selecting, substituting, and saving a product.
All of these methods test the user's entries to avoid crashing the program with an incorrect entry (letter instead of digit, or out of bound entry)
**categoriesLoop ():** View categories.
**productLoop ():** Display of products in the chosen category.
**substiProductLoop ():** Display of a selection of substitution products.
**displaySubsProdLoop ():** View details of the chosen substitution product.
**userProductLoop ():** Display of substituted products, saved by the user.
**displayUserProdLoop ():** View details of the substituted products saved by the user.

## ...from the database_app.py file:
### class GestionDB ():
Contains all the methods related to database management, starting with the connection to the database:
**commit ():** Saves the cursor.
**close ():** Closes the database.
**substiProdFilling ():** Insert the product data substituted by the user into the database.
**queryExecutor ():** Uses the cursor to execute the queries as an argument with possible error detection.
**selectResult ():** Returns the selection of the user.
**selectProduct ():** Displays the details of the product selected by the user.

## ...of the dict_app file:
### class Glob (): 
Contains all the pseudo variables of the application to allow easier settings.
