#! /usr/bin/env python 3
# coding : utf-8

class Glob():

    # Download Openfoodfacts products file name
    offDatas = "fr.openfoodfacts.org.products.csv"
    # Parsed Openfoodfacts products file name
    offParsedData = "openfoodfacts_parsed.csv"

    #URL product
    url_barre_code = ('http://world-fr.openfoodfacts.org/produit/')

    req_categ = ("SELECT DISTINCT categories FROM Products WHERE nutrition_score_fr_100g BETWEEN 29 AND 30")
    req_prod = ("SELECT product_name  FROM Products WHERE nutrition_score_fr_100g > 20 AND categories=")
    req_substiProd = ("SELECT product_name FROM Products WHERE nutrition_score_fr_100g < 25 AND categories=")
    req_heal_prod_srt = ("SELECT product_name FROM Products WHERE categories=")
    req_heal_prod_end =("ORDER BY nutrition_score_fr_100g LIMIT 5")
    req_displaySubsProd = ("SELECT product_name, brands, code, nutrition_grade_fr, url, stores FROM Products WHERE product_name=")
    req_product_barre_code = ("SELECT code from Products WHERE product_name=")
    req_save_substi_prod = ("SELECT code, url, product_name, brands, categories, stores, countries, nutrition_grade_fr, nutrition_score_fr_100g FROM Products WHERE product_name=")

    req_userProd_display = ("SELECT product_name FROM SubstiProducts")

