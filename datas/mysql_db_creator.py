#! /usr/bin/env python 3
# coding : utf-8

"""
    mysql_db_creator.py is an application that can be used to parse an
    openfoofacts csv file.
    mysql_db_creator.py goes then creates a MySQL database with its tables
    and insert the data into the tables.
"""

import sys
import os
import csv
from dict_app import Glob
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb



def csv_parser():
    """
        This function admit to parse the file and extract the following fields :
        code[0] / url[1] / product_name[7] / brands[12] / categories[14] /
        stores[30] /countries[31] /nutrition_grade_fr[53] /
        nutrition_score_fr_100g[159].
    """
#Increase the field-size limit
    csv.field_size_limit(sys.maxsize)

    directory = os.path.dirname(__file__)

# File to read and parse
    off_datas = Glob.offDatas
    read_path_to_file = os.path.join(directory, "../datas", off_datas)
    fname = read_path_to_file
    file = open(fname, "rt")

# Parsed file to write
    off_parsed_data = Glob.offParsedData
    write_path_to_file = os.path.join(directory, "../datas", off_parsed_data)
    fname_out = write_path_to_file
    file_out = open(fname_out, "wt")

# Parsing : tried to select only the French data
# and ignores some empty fields
    try:
        reader = csv.reader(file, delimiter='\t', lineterminator='\n')
        for row in reader:
            if (row[31] == "France" and row[159] != "" and row[14] != ""\
                and row[7] != "" and row[53] != "" and len(row[0]) <= 13)  or\
            (row[31] == "france" and row[159] != "" and row[14] != "" \
                and row[7] != "" and row[53] != "" and len(row[0]) <= 13) or\
            (row[31] == "FR" and row[159] != "" and row[14] != "" \
                and row[7] != "" and row[53] != "" and len(row[0]) <= 13) or\
            (row[31] == "fr" and row[159] != "" and row[14] != "" \
                    and row[7] != "" and row[53] != "" and len(row[0]) <= 13):
                parse_ligne = row[0], row[1], row[7], row[12], row[14],\
                    row[30], row[31], row[53], row[159]
# Write parsed field to the file
                writer = csv.writer(file_out)
                writer.writerow(parse_ligne)
            else:
                pass
    finally:
        file.close()



def create_database():
    """"
        This function is used to create the different tables in the database.
    """
# Open database connection
    db = MySQLdb.connect("127.0.0.1", "root", "toor",\
                        "offProject", charset='utf8')

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')

# create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS \
                    offProject CHARACTER SET 'utf8'")

# create table <Products>
    cursor.execute("CREATE TABLE IF NOT EXISTS Products (\
                        code BIGINT(13) NOT NULL,\
                        url VARCHAR(250) NOT NULL,\
                        product_name VARCHAR(250) NOT NULL,\
                        brands VARCHAR(250),\
                        categories VARCHAR(250) NOT NULL,\
                        stores VARCHAR(150),\
                        countries VARCHAR(10) NOT NULL,\
                        nutrition_grade_fr VARCHAR(1) NOT NULL,\
                        nutrition_score_fr_100g TINYINT(3) NOT NULL,\
                        PRIMARY KEY (code)\
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;")

# create table <SubstiProducts>
    cursor.execute("CREATE TABLE IF NOT EXISTS SubstiProducts (\
                        code BIGINT(13) NOT NULL,\
                        url VARCHAR(250) NOT NULL,\
                        product_name VARCHAR(250) NOT NULL,\
                        brands VARCHAR(250),\
                        categories VARCHAR(250) NOT NULL,\
                        stores VARCHAR(150),\
                        countries VARCHAR(10) NOT NULL,\
                        nutrition_grade_fr VARCHAR(1) NOT NULL,\
                        nutrition_score_fr_100g TINYINT(3) NOT NULL,\
                        PRIMARY KEY (code)\
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;")

# create table <Categories>
    cursor.execute("CREATE TABLE IF NOT EXISTS Categories (\
                        categories_id INT PRIMARY KEY AUTO_INCREMENT,\
                        prodInCat BIGINT(13) NOT NULL,\
                        categories_name VARCHAR(250) NOT NULL,\
                        CONSTRAINT fk_product_code_in_cat\
                        FOREIGN KEY (prodInCat)\
                        REFERENCES Products(code)\
                        ) ENGINE=InnoDB;")


# File to read and parse
    off_parsed_data = Glob.offParsedData
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, "../datas", off_parsed_data)

    with open(path_to_file) as off_file:
        data = [tuple(line) for line in csv.reader(off_file)]

# Inserting data into the table <Products>
    for tup_line in data:
        cursor.execute("INSERT INTO Products (code, url, product_name,\
            brands, categories, stores, countries, nutrition_grade_fr, nutrition_score_fr_100g)\
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", tup_line)

# Delete categories with less than 10 products
    cursor.execute("SELECT categories, COUNT(*) FROM Products \
                    GROUP BY categories")
    response = cursor.fetchall()
    for index in range(0, len(response)):
        if response[index][1] < 10:
            str_resp = str('"'+response[index][0]+'"')
            cursor.execute("DELETE FROM Products WHERE categories =" + str_resp)
        else:
            pass

    db.commit()
    db.close()

"""
    # create table <Products>
    cursor.execute("CREATE TABLE IF NOT EXISTS Products (\
                        code BIGINT(13) NOT NULL,\
                        url VARCHAR(250) NOT NULL,\
                        product_name VARCHAR(250) NOT NULL,\
                        brands VARCHAR(250),\
                        categories VARCHAR(250) NOT NULL,\
                        stores VARCHAR(150),\
                        countries VARCHAR(10) NOT NULL,\
                        nutrition_grade_fr VARCHAR(1) NOT NULL,\
                        nutrition_score_fr_100g TINYINT(3) NOT NULL,\
                        PRIMARY KEY (code)\
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;")

    # create table <SubstiProducts>
    cursor.execute("CREATE TABLE IF NOT EXISTS SubstiProducts (\
                        code BIGINT(13) NOT NULL,\
                        url VARCHAR(250) NOT NULL,\
                        product_name VARCHAR(250) NOT NULL,\
                        brands VARCHAR(250),\
                        categories VARCHAR(250) NOT NULL,\
                        stores VARCHAR(150),\
                        countries VARCHAR(10) NOT NULL,\
                        nutrition_grade_fr VARCHAR(1) NOT NULL,\
                        nutrition_score_fr_100g TINYINT(3) NOT NULL,\
                        PRIMARY KEY (code)\
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;")

    # create table <Categories>
    cursor.execute("CREATE TABLE IF NOT EXISTS Categories (\
                        categories_id INT PRIMARY KEY AUTO_INCREMENT,\
                        categories_name VARCHAR(250) NOT NULL,\
                        CONSTRAINT fk_categories_name_id\
                        FOREIGN KEY (categories_name)\
                        REFERENCES Products(categories)\
                        ) ENGINE=InnoDB;")

CREATE TABLE IF NOT EXISTS Categories (
categories_id INT PRIMARY KEY AUTO_INCREMENT,
categories_name VARCHAR(250) NOT NULL,
CONSTRAINT fk_categories_name_id
FOREIGN KEY (categories_name)
REFERENCES Products(categories)
) ENGINE=InnoDB;

CREATE INDEX categories_ind
ON Products (categories);
"""

if __name__ == '__main__':
    csv_parser()
    create_database()
