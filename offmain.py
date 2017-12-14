#! /usr/bin/env python 3
# coding : utf-8

"""
    Entry point of the program, including the main loop.
"""

import sys
import os
from datas.displ_app import Loop



#Instantiation of an object containing the different loops of the application
lp = Loop()

if lp.db.echec:
    sys.exit()


def main_menu():
    """ Shows the different options available """
    prog_run = True
    while prog_run:

        # Clear then show main application options
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n*** Make your choice (or <Enter> to finish):\n")
        print("*** 1) What food do you want to replace ?\n")
        print("*** 2) Find my substituted foods\n")
        print("                                               *** Your choice :", end=' ')

        choice = input()
        os.system('cls' if os.name == 'nt' else 'clear')

        # Open categorie menu
        if choice == "1":
            choice = lp.categoriesLoop()


            # Open product menu
            if choice:
                lp.productLoop()

                # Open
                if choice:
                    lp.substiProductLoop()



                    #open fiche produit
                    if choice:
                        lp.displaySubsProdLoop()


            elif choice == "":
                prog_run = False
                break

            else:
                print("\n*** Sorry your choice is incorrect, please try again ***")


        # Open substitute product menu
        elif choice == "2":
            choice = lp.userProductLoop()

            # Open details sub products
            if choice:
                lp.displayUserProdLoop()


        # Leave the program
        elif choice == "":
            prog_run = False
            break

        else:
            print("\n*** Sorry your choice is incorrect, please try again ***")


    choice = input("*** Do you really want to leave ? (y/n) ")
    if choice[0] == "y" or choice[0] == "Y":
        lp.db.close()
        print("\n*** Thank you for having used this application ***\
        \n                       *** Goodbye! ***\n")
    else:
        main_menu()

if __name__ == '__main__':
    main_menu()
