#! /usr/bin/env python 3
# coding : utf-8

"""
    Database Management Module.
"""

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb



class GestionDB():
    """
        Establishment and interfacing of a database
    """
    def __init__(self):
        """
            Establishing the connection - Creating the cursor
        """

        try:
            self.database = MySQLdb.connect(
                "127.0.0.1", "root", "toor", "offProject", charset='utf8')

        except Exception as err:
            print('Connection to the database failed : \n'\
                'error detected :\n%s' % err)
            self.echec = 1
        else:
            print('\n*** Successful connection to the database ***')
            self.cursor = self.database.cursor()
            self.echec = 0


    def commit(self):
        """
            Save the cursor
        """
        if self.database:
            self.database.commit()


    def close(self):
        """
            Close the database
        """
        if self.database:
            self.database.close()


    def substiProdFilling(self, query):
        """
            Insertion of substituted products into the database.
        """
        self.cursor.execute(query)
        response = self.cursor.fetchall()
        for tup_line in response:
            print(tup_line)
            self.cursor.execute("INSERT INTO SubstiProducts (code, url, product_name,\
                brands, categories, stores, countries, nutrition_grade_fr, nutrition_score_fr_100g)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", tup_line)

        self.database.commit()


    def queryExecutor(self, query):
        """
            Execution of the request <query>, with possible error detection
        """
        try:
            self.cursor.execute(query)
        except Exception as err:
            # displays the query and the system error message.
            print("SQL query incorrect: \n{}\nError detected :".format(query))
            print(err)
            return 0
        else:
            response = self.cursor.fetchall()
            for index in range(0, len(response)):
                print("{} -> {}".format(index, (response[index][0])))
            self.database.commit()


    def selectResult(self, index, req):
        """
            Return the user selection.
        """
        index = int(index)
        self.cursor.execute(req)
        response = self.cursor.fetchall()
        response = str(response[index][0])
        self.database.commit()
        return response


    def selectProduct(self, query):
        """
            View details about user selection.
        """
        self.cursor.execute(query)
        response = self.cursor.fetchall()
        print("Product name     -> {}".format(response[0][0]))
        print("Brands           -> {}".format(response[0][1]))
        print("Barre code       -> {}".format(response[0][2]))
        print("Nutrition grade  -> {}".format(response[0][3]))
        print("url              -> {}".format(response[0][4]))
        print("Stores           -> {}".format(response[0][5]))
        self.database.commit()
