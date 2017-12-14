#! /usr/bin/env python 3
# coding : utf-8

"""
    Grouping the pseudo constant and the queries necessary for the application.
"""

class Glob():
    """
        The file names and the sensitivity of
        the nutrition score are modifiable here.
    """

# Download Openfoodfacts products file name.
    offDatas = "fr.openfoodfacts.org.products.csv"

# Parsed Openfoodfacts products file name.
    offParsedData = "openfoodfacts_parsed.csv"

#URL product.
    url_barre_code = ('http://world-fr.openfoodfacts.org/produit/')


# SQL request:
    # Showing categories according to a range of nutrition score products.
    req_categ = ("SELECT DISTINCT categories FROM Products\
        WHERE nutrition_score_fr_100g BETWEEN 29 AND 30")

    # Display of products according to a ceiling of nutrition score.
    req_prod = ("SELECT product_name  FROM Products\
        WHERE nutrition_score_fr_100g > 20 AND categories=")

    #Showing 5 products in ascending order of selected category
    req_heal_prod_srt = ("SELECT product_name FROM Products WHERE categories=")
    req_heal_prod_end = ("ORDER BY nutrition_score_fr_100g LIMIT 5")

    # Selects the details of the selected product.
    req_displaySubsProd = ("SELECT product_name, brands, code, nutrition_grade_fr, url, stores\
        FROM Products WHERE product_name=")

    # Retrieving the product barcode.
    req_product_barre_code = ("SELECT code from Products WHERE product_name=")

    # Full data recovery of the product for registration.
    req_save_substi_prod = ("SELECT code, url, product_name, brands, categories, stores,\
        countries, nutrition_grade_fr, nutrition_score_fr_100g FROM Products WHERE product_name=")

    # Display of registered products by the user.
    req_userProd_display = ("SELECT product_name FROM SubstiProducts")
