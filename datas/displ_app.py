#! /usr/bin/env python 3
# coding : utf-8

"""
    Module including the various features.
"""

import os
import webbrowser
from datas.dict_app import Glob
from datas.database_app import GestionDB


class Loop():
    """
        Class including the various features in the form of loops.
    """
    def __init__(self):
        self.db = GestionDB()


    def categoriesLoop(self):
        """
            Displays the different categories and controls the input made by the user.
        """
        # Displays the different categories and proposals for action.
        req_categ = (Glob.req_categ)
        print("\n*** The available categories are:\n")
        print(self.db.queryExecutor(req_categ))
        print("\n*** Select the desired category:\n")
        print("                                               *** Your choice :", end=' ')
        choice = input()

        #Clears the terminal.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Test the input of the user.
        try:
            int(choice)
        except ValueError:
            print("\n*** Sorry your choice is incorrect, please try again ***")
            print("***             You must enter a number              ***")
            self.categoriesLoop()
        else:
            try:
                self.selected_categorie = self.db.selectResult(choice, req_categ)
            except IndexError:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.categoriesLoop()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                return choice


    def productLoop(self):
        """
            Displays the different products of the selected categorie
            and controls the input made by the user.
        """
        req_prod = ('{} "{}"'.format(Glob.req_prod, self.selected_categorie))
        print("\n*** The available products are:\n")
        print(self.db.queryExecutor(req_prod))
        print("\n*** Select the desired product:\n")
        print("                                               *** Your choice :", end=' ')
        choice = input()

        #Clears the terminal.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Test the input of the user.
        try:
            int(choice)
        except ValueError:
            print("\n*** Sorry your choice is incorrect, please try again ***")
            print("***             You must enter a number              ***")
            self.productLoop()
        else:
            try:
                self.selected_product = self.db.selectResult(choice, req_prod)
            except IndexError:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.productLoop()
            else:
                return choice


    def substiProductLoop(self):
        """
            Displays the 5 healthiest products in the selected category.
        """
        req_heal_prod = ('{} "{}" {}'.format(
            Glob.req_heal_prod_srt, self.selected_categorie, Glob.req_heal_prod_end))
        print("\n*** The healthiest products in this category are :\n")
        print(self.db.queryExecutor(req_heal_prod))

        print("\n*** Do you want some details for a product ?:\n")
        print("                                               *** Your choice :", end=' ')
        choice = input()

        #Clears the terminal.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Test the input of the user.
        try:
            int(choice)
        except ValueError:
            print("\n*** Sorry your choice is incorrect, please try again ***")
            print("***             You must enter a number              ***")
            self.substiProductLoop()
        else:
            try:
                self.selected_sub_prod = self.db.selectResult(choice, req_heal_prod)
            except IndexError:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.substiProductLoop()
            else:
                return choice


    def displaySubsProdLoop(self):
        """
            Displays the details of the selected product.
        """
        req_displaySubsProd = ('{} "{}"'.format(Glob.req_displaySubsProd, self.selected_sub_prod))
        print("\n*** Product details :\n")
        print(self.db.selectProduct(req_displaySubsProd))

        print("\n*** What do you want to do with this product ?:\n")
        print("*** 1) Save the product\n")
        print("*** 2) Show the URL page Product\n")
        print("*** 3) Back to the main menu\n")

        print("                                               *** Your choice :", end=' ')
        choice = input()

        #Clears the terminal.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Test the input of the user.
        try:
            int(choice)
        except ValueError:
            print("\n***               Make your selection                ***")
            print("***               You must enter a number            ***")
            self.displaySubsProdLoop()
        else:
            # Save the product.
            if choice == "1":
                req_save_substi_prod = ('{} "{}"'.format(
                    Glob.req_save_substi_prod, self.selected_sub_prod))
                self.db.substiProdFilling(req_save_substi_prod)

            # Show the URL page Product.
            elif choice == "2":
                req_product_barre_code = ('{} "{}"'.format(
                    Glob.req_product_barre_code, self.selected_sub_prod))
                self.req_product_barre_code = self.db.queryExecutor(req_product_barre_code)

                self.req_product_barre_code = self.db.selectResult(0, req_product_barre_code)

                self.product_url = ("{}{}".format(Glob.url_barre_code, self.req_product_barre_code))


                webbrowser.open(self.product_url, new=0, autoraise=True)
                self.displaySubsProdLoop()

            # Back to the main menu.
            elif choice == "3":
                pass
            else:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.displaySubsProdLoop()


    def userProductLoop(self):
        """
            Displays the products substituted and saved by the user.
        """
        req_userProd_display = (Glob.req_userProd_display)
        print("\n*** Your substituted products are:\n")
        print(self.db.queryExecutor(req_userProd_display))

        print("\n*** Select the product for which you want details:\n")
        print("                                               *** Your choice :", end=' ')
        choice = input()

        #Clears the terminal.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Test the input of the user.
        try:
            int(choice)
        except ValueError:
            print("\n*** Sorry your choice is incorrect, please try again ***")
            print("***             You must enter a number              ***")
            self.userProductLoop()
        else:
            try:
                self.selected_user_prod = self.db.selectResult(choice, req_userProd_display)
            except IndexError:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.userProductLoop()
            else:
                return choice


    def displayUserProdLoop(self):
        """
            Displays the details of the product substituted and saved by the user.
        """
        req_displaySubsProd = ('{} "{}"'.format(Glob.req_displaySubsProd, self.selected_user_prod))
        print("\n*** Product details :\n")
        print(self.db.selectProduct(req_displaySubsProd))
        print("\n*** What do you want to do with this product ?:\n")
        print("*** 1) Go back to the previous page")
        print("*** 2) Show the URL page Product")
        print("*** 3) Back to the main menu\n")

        print("                                               *** Your choice :", end=' ')
        choice = input()

        #Clears the terminal.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Test the input of the user.
        try:
            int(choice)
        except ValueError:
            print("\n***               Make your selection                ***")
            print("***               You must enter a number            ***")
            self.displayUserProdLoop()

        else:
            # Go back to the previous page.
            if choice == "1":
                self.userProductLoop()

            # Show the URL page Product.
            elif choice == "2":
                req_product_barre_code = ('{} "{}"'.format(
                    Glob.req_product_barre_code, self.selected_user_prod))

                # Barcode retrieval by product name.
                self.req_product_barre_code = self.db.queryExecutor(req_product_barre_code)

                # Barcode retrieval.
                self.req_product_barre_code = self.db.selectResult(0, req_product_barre_code)

                # Preparing the request for the url address of the product.
                self.product_url = ("{}{}".format(Glob.url_barre_code, self.req_product_barre_code))

                # URL request.
                webbrowser.open(self.product_url, new=0, autoraise=True)
                self.displayUserProdLoop()

            # Back to the main menu
            elif choice == "3":
                pass
            else:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.displayUserProdLoop()
