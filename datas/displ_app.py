#! /usr/bin/env python 3
# coding : utf-8

import os
from datas.dict_app import Glob
from datas.dataBase_app import GestionDB
import webbrowser


class Loop():
    def __init__(self):
    	self.db = GestionDB()


    def categoriesLoop(self):
        req_categ = (Glob.req_categ)
        print("\n*** The available categories are:\n")
        print(self.db.queryExecutor(req_categ))
        print("\n*** Select the desired category:\n")
        print("                                               *** Your choice :", end=' ')
        
        choice = input()
        os.system('cls' if os.name=='nt' else 'clear')
        try:
            val = int(choice)
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
                os.system('cls' if os.name=='nt' else 'clear')
                print(self.db.selectResult(choice, req_categ))

        return choice


    def productLoop(self): # "{} '{}'"
        req_prod = ('{} "{}"'.format(Glob.req_prod, self.selected_categorie))
        print("\n*** The available products are:\n")
        print(self.db.queryExecutor(req_prod))
        print("\n*** Select the desired product:\n")
        print("                                               *** Your choice :", end=' ')
        
        choice = input()
        os.system('cls' if os.name=='nt' else 'clear')
        try:
            val = int(choice)
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
                print(self.db.selectResult(choice, req_prod))

        return choice


    def substiProductLoop(self):
        req_heal_prod = ('{} "{}" {}'.format(Glob.req_heal_prod_srt, self.selected_categorie, Glob.req_heal_prod_end))
        print("\n*** The healthiest products in this category are :\n")
        print(self.db.queryExecutor(req_heal_prod))

        print("\n*** Do you want some details for a product ?:\n")
        print("                                               *** Your choice :", end=' ')
        
        choice = input()
        os.system('cls' if os.name=='nt' else 'clear')
        try:
            val = int(choice)
        except ValueError:
            print("\n*** Sorry your choice is incorrect, please try again ***")
            print("***             You must enter a number              ***")            
            self.substiProductLoop()
        else:
            try:
                self.selected_sub_Prod = self.db.selectResult(choice, req_heal_prod)
            except IndexError:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.substiProductLoop()
            else:            
                print("******", self.db.selectResult(choice, req_heal_prod))

        return choice

    def displaySubsProdLoop(self):
        req_displaySubsProd = ('{} "{}"'.format(Glob.req_displaySubsProd, self.selected_sub_Prod))
        print("\n*** Product details :\n")
        print(self.db.selectProduct(req_displaySubsProd))

        print("\n*** What do you want to do with this product ?:\n")
        print("*** 1) Save the product\n")
        print("*** 2) Show the URL page Product\n")
        print("*** 3) Back to the main menu\n")

        print("                                               *** Your choice :", end=' ')
        
        choice = input()
        os.system('cls' if os.name=='nt' else 'clear')
        try:
            val = int(choice)
        except ValueError:
            print("\n***               Make your selection                ***")
            print("***               You must enter a number            ***")
            self.displaySubsProdLoop()

        else:
            if choice =="1":
                req_save_substi_prod = ('{} "{}"'.format(Glob.req_save_substi_prod, self.selected_sub_Prod))
                self.db.substiProdFilling(req_save_substi_prod)
            
            elif choice == "2":
                req_product_barre_code = ('{} "{}"'.format(Glob.req_product_barre_code, self.selected_sub_Prod))
                self.req_product_barre_code = self.db.queryExecutor(req_product_barre_code)
                

                self.req_product_barre_code = self.db.selectResult(0, req_product_barre_code)
                

                self.product_url = ("{}{}".format(Glob.url_barre_code, self.req_product_barre_code))


                webbrowser.open(self.product_url, new=0, autoraise=True)
                self.displaySubsProdLoop()


            elif choice == "3":
                pass
            else:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.displaySubsProdLoop()                

######################################################################

    def userProductLoop(self): 
        req_userProd_display = (Glob.req_userProd_display)
        print("\n*** Your substituted products are:\n")
        print(self.db.queryExecutor(req_userProd_display))

        print("\n*** Select the product for which you want details:\n")
        print("                                               *** Your choice :", end=' ')
        
        choice = input()
        os.system('cls' if os.name=='nt' else 'clear')
        try:
            val = int(choice)
        except ValueError:
            print("\n*** Sorry your choice is incorrect, please try again ***")
            print("***             You must enter a number              ***")            
            self.userProductLoop()
        else:
            try:
                self.selected_User_Prod = self.db.selectResult(choice, req_userProd_display)
            except IndexError:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.userProductLoop()
            else:            
                print("******", self.db.selectResult(choice, req_userProd_display))

        return choice


    def displayUserProdLoop(self):
        req_displaySubsProd = ('{} "{}"'.format(Glob.req_displaySubsProd, self.selected_User_Prod))
        print("\n*** Product details :\n")
        print(self.db.selectProduct(req_displaySubsProd))
        print("\n*** What do you want to do with this product ?:\n")
        print("*** 1) Go back to the previous page")
        print("*** 2) Show the URL page Product")
        print("*** 3) Back to the main menu\n")

        print("                                               *** Your choice :", end=' ')
        
        choice = input()
        os.system('cls' if os.name=='nt' else 'clear')
        try:
            val = int(choice)
        except ValueError:
            print("\n***               Make your selection                ***")
            print("***               You must enter a number            ***")
            self.displayUserProdLoop()

        else:
            if choice =="1":
                self.userProductLoop()
            
            elif choice == "2":
                req_product_barre_code = ('{} "{}"'.format(Glob.req_product_barre_code, self.selected_User_Prod))
                self.req_product_barre_code = self.db.queryExecutor(req_product_barre_code)
                

                self.req_product_barre_code = self.db.selectResult(0, req_product_barre_code)
                

                self.product_url = ("{}{}".format(Glob.url_barre_code, self.req_product_barre_code))


                webbrowser.open(self.product_url, new=0, autoraise=True)
                self.displayUserProdLoop()


            elif choice == "3":
                pass
            else:
                print("\n*** Sorry your choice is incorrect, please try again ***")
                print("*** The product selects is outside the proposed list ***")
                self.displayUserProdLoop()
