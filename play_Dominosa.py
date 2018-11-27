from boardlibrary import EasyDoesIt, EasyCarl, EasyJoe, AbsolutelyGenius,MediumCarl,MediumJoe,SuperHard,ReallyHard,Alittlebitharder,ActuallyHard,Demoboard
from boardlibrary import EasyDoesIt_solution, EasyCarl_solution, EasyJoe_solution, Alittlebitharder_Solution,ActuallyHard_solution,SuperHard_solution,MediumCarl_solution,MediumJoe_solution,ReallyHard_solution,AbsolutelyGenius_solution
import random
from Demo import demoplay
import time
from Play import play
from DominosaSolver import solveboard
from DominosaSolver import prettyprintboards

""" Add failsafes for '' and wrong inputs,, Comment the code"""
"""Board - Input domain pairs, pray that it works, if not MAKE it work"""

#Go for bad inputs
def mainmenu():
    menu = True
    print("Hello! Welcome to Dominosa!!")
    print("What would you like to do!?")
    print("  ")
    print("(1) Play.")
    print("   ")
    print("(2) What is Dominosa?")
    print("       ")
    print("(3) How to play.")
    print("       ")
    print("(4) Watch the computer play.")
    print("     ")
    print("(5) Demo")
    print("    ")
    print("(6) Exit")
    print("    ")
    selection = input("Please enter the number corresponding to your selection: ")

    while menu:
        if selection == '':
            print('Bad input!')
            mainmenu()
        elif int(selection) == 0:
            mainmenu()
        elif int(selection) == 1:
            print("       ")
            choice = input("Okay, pick a difficulty:\n (1) Easy\n (2) Medium\n (3) Hard\n (4) Genius Level\n (0) To go back to the main menu")
            if choice == '':
                print("Bad input!")
                choice = input('Input choice again!!')
            elif int(choice) == 0:
                print("       ")
                mainmenu()
                break
            else:
                printallboards(choice)
                boardchoice = input("Select your board by entering the number that corresponds with the board: ")
                if boardchoice == '':
                    print("Bad input!")
                    choice = input('Input choice again!!')
                else:
                   boardselect(boardchoice)
                   mainmenu()
                break
        elif int(selection) == 2:
            description()
        elif int(selection) == 3:
            print("       ")
            howtoplay()
        elif int(selection) == 4:
            print("       ")
            print("Get ready to be amazed.")
            choice = input('What difficulty would you like it to play?\n (1) Easy\n (2) Medium\n (3) Hard\n (4) Genius Level\n (0) To go back to the main menu')
            if int(choice) >= 5 or choice == '':
                print('Bad input!! Please enter your choice!')
            elif int(choice) == 0:
                print("       ")
                mainmenu()
                break
            else:
                printallboards(choice)
                print('      ')
                choice2 = input('What board do you want the computer to play?')
                solveboard(choice2)
                prettyprintboards(choice2)
            choice = input("Type 0 to return to the main menu")
            if int(choice) == 0:
                mainmenu()
            break

        elif int(selection) == 5:
            print("       ")
            print("All Right! Welcome to the world of Dominosa!")
            print("       ")
            print("Dominosa is a logic puzzle with simple rules and challenging solutions.")
            print("        ")
            print("The rules are simple. You have to find the location of all dominoes on the grid. "
                  "A domino is a pair of numbers."
                  " You can have only one of each pair.")
            time.sleep(10)
            print("       ")
            print("Playing Dominosa consists of 5 easy steps.")
            print("1. Select a board")
            print("2. Enter the x values of where you want to place your first domino half ")
            print("3. Enter the y values of where you want to place your first domino half ")
            print("4. Repeat 2 and 3 for the second half.")
            print("5. Rinse and repeat!")
            print("       ")
            time.sleep(10)
            print("Let's start small!")
            print("       ")
            demoplay()
            mainmenu()
            choice = input("Type 0 to return to the main menu")
            if int(choice) == 0 or '':
                mainmenu()
            break

        elif int(selection) == 6:
            menu = False
            print("       ")
            print("Goodbye!! Come back soon!!")
            break

        elif int(selection) >= 7:
            print("       ")
            print("Incorrect input! Try again, silly!")
            mainmenu()
            break



def printallboards(choice):

    if int(choice) == 1:
        print('Here are the easy boards!')
        print("        ")
        print('(0) Demo Board')
        print("        ")
        prettyprintboards(Demoboard)
        print("        ")
        print('(1) EasyDoesIt')
        print("        ")
        prettyprintboards(EasyDoesIt)
        print("        ")
        print('(2) EasyCarl')
        prettyprintboards(EasyCarl)
        print("        ")
        print('(3) EasyJoe')
        prettyprintboards(EasyJoe)
    elif int(choice) == 2:
        print('Here are the medium boards!')
        print("        ")
        print('(4) A little bit harder\n')
        prettyprintboards(Alittlebitharder)
        print("        ")
        print('(5) Medium Joe \n')
        prettyprintboards(MediumJoe)
        print("        ")
        print('(6) Medium Carl \n')
        prettyprintboards(MediumCarl)
    elif int(choice) == 3:
        print('Here are the Hard boards!')
        print("        ")
        print('(7) Actually Hard \n')
        prettyprintboards(ActuallyHard)
        print("        ")
        print('(8) Super Hard \n')
        prettyprintboards(SuperHard)
        print("        ")
        print('(9) Really Hard\n')
        prettyprintboards(ReallyHard)
    elif int(choice) == 4:
        print('Okay big shot, this is the genius board!')
        print('       ')
        print('(10) AbsolutelyGenius')
        prettyprintboards(AbsolutelyGenius)
    elif int(choice) >= 5:
        wrong = True
        while(wrong):
         print('Please input the correct category (1) Easy, (2) Medium, (3)Hard, (4) Genius')
         choice = input('Please input selection')
         if int(choice) <=4:
          wrong = False
          printallboards(choice)


def description():
    print("       ")
    print("Dominosa is a logic puzzle with simple rules and challenging solutions.")
    print("        ")
    print("The rules are simple. You have to find the location of all dominoes on the grid. "
          "A domino is a pair of numbers."
          " You can have only one of each pair.")
    choice = input("Type 0 to return to the main menu")
    if int(choice) == 0 or choice=='':
        mainmenu()

def howtoplay():
    print("Playing Dominosa consists of 5 easy steps.")
    print("1. Select a board")
    print("2. Enter the x values of where you want to place your first domino half ")
    print("3. Enter the y values of where you want to place your first domino half ")
    print("4. Repeat 2 and 3 for the second half.")
    print("5. Rinse and repeat!")
    choice = input("Type 0 to return to the main menu")
    if int(choice) == 0 or choice == '':
        mainmenu()

def boardselect(board):
    if int(board) == 1 :
        print('       ')
        name = 'Easy Does It'
        print(name)
        prettyprintboards(EasyDoesIt)
        print("This board is " + str(len(EasyDoesIt) - 1) + ' by ' + str(
        len(EasyDoesIt[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(EasyDoesIt, name)
    elif int(board) == 2:
        print('       ')
        name = 'Easy Carl'
        print(name)
        prettyprintboards(EasyCarl)
        print("This board is " + str(len(EasyCarl) - 1) + ' by ' + str(
        len(EasyCarl[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(EasyCarl, name)
    elif int(board) == 3:
        print('       ')
        name = 'Easy Joe'
        print(name)
        prettyprintboards(EasyJoe)
        print("This board is " + str(len(EasyJoe) - 1) + ' by ' + str(
        len(EasyJoe[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(EasyJoe, name)
    elif int(board) == 4:
        print('       ')
        name = 'A Little Bit Harder'
        print(name)
        prettyprintboards(Alittlebitharder)
        print("This board is " + str(len(Alittlebitharder) - 1) + ' by ' + str(
        len(Alittlebitharder[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(Alittlebitharder, name)
    elif int(board) == 5:
        print('       ')
        name = 'Medium Joe'
        print(name)
        prettyprintboards(MediumJoe)
        print("This board is " + str(len(MediumJoe) - 1) + ' by ' + str(
        len(MediumJoe[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(MediumJoe, name)
    elif int(board) == 6:
        print('       ')
        name = 'Medium Carl'
        print(name)
        prettyprintboards(MediumCarl)
        print("This board is " + str(len(MediumCarl) - 1) + ' by ' + str(
        len(MediumCarl[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(MediumCarl, name)
    elif int(board)== 7:
        print('       ')
        name = 'Actually Hard'
        print(name)
        prettyprintboards(ActuallyHard)
        print("This board is " + str(len(ActuallyHard) - 1) + ' by ' + str(
        len(ActuallyHard[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(ActuallyHard, name)
    elif int(board) == 8:
        print('       ')
        name = 'Super Hard'
        print(name)
        prettyprintboards(SuperHard)
        print("This board is " + str(len(SuperHard) - 1) + ' by ' + str(
        len(SuperHard[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(SuperHard, name)
    elif int(board) == 9:
        print('       ')
        name = 'Really Hard'
        print(name)
        prettyprintboards(ReallyHard)
        print("This board is " + str(len(ReallyHard) - 1) + ' by ' + str(
        len(ReallyHard[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(ReallyHard, name)
    elif int(board) == 10:
        print('       ')
        name = 'Absolutely Genius'
        print(name)
        prettyprintboards(AbsolutelyGenius)
        print("This board is " + str(len(AbsolutelyGenius) - 1) + ' by ' + str(
        len(AbsolutelyGenius[0]) - 1) + ' so you have to make sure your answers are in that range(0 to the max range)!')
        play(AbsolutelyGenius, name)
    elif board == '':
        print('Bad input!!')
        wrong =True
        while wrong:
            choice = input('Please enter a board')
            if choice <=10 and choice>0:
                wrong = False
                boardselect(choice)


mainmenu()