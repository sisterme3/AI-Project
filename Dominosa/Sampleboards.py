import numpy as np
from array import *

#Possible domino pieces
#def printvalidchoices():


# Failsafes!!!
#if statements that don't break anything
#Get Mainmenu to completely work!

#Find a symbols for dominos

#Find a better way to put down dominos

#Find a way to validate domino placement

#def validplaces():


#Figure out and complete intellegent parts



#Let Omar do the Thingy


#Board and board solution library


def mainmenu():
    game_active = True
    print("Hello! Welcome to Dominosa!!")
    print("What would you like to do!?")
    print("  ")
    print("1. Play.")
    print("   ")
    print("2. What is Dominosa?")
    print("       ")
    print("3. How to play.")
    print("       ")
    print("4. Watch the computer play.")
    print("     ")
    print("5. Play against the computer.")
    print("    ")
    print("6. Play a Random board")
    print("    ")
    print("Type quit if you want to exit")
    print("    ")
    selection = input("Please enter your selection!       ")

    while selection != quit:
        if int(selection) == 1:
            print("       ")
            print("Okay, pick a board")
            print("Type 0 to go back.")
            print("Bob(Easy)")
            prettyprintboards(bob)
            print("          ")
            print("Carl(Easy)")
            prettyprintboards(carl)
            print("          ")
            print("Joe(Easy)")
            prettyprintboards(joe)
            boardchoice = input("Select your board")
            boardselect(boardchoice)
            break
        elif int(selection) == 2:
            description()
            boardchoice = input("Type 0 to return to the main menu")
            print("Type 0 to go back.")
            break

        elif int(selection) == 3:
            print("       ")
            howtoplay()
            print("Type 0 to go back.")
            boardchoice = input("Type 0 to return to the main menu")

        elif int(selection) == 4:
            print("       ")
            print("Get ready to be amazed. What board do you want the computer to play>")
            print("Type 0 to go back.")
            break

        elif int(selection) == 5:
            print("       ")
            print("Versus! Okay, pick a board to play!")
            print("Type 0 to go back.")
            break

        elif int(selection) == 6:
            print("       ")
            print("Get Ready......")
            print("Type 0 to go back.")
            break

    #if selection.type() is str:
    #   print("Incorrect input! Try again, silly")

        elif int(selection) >= 7:
            print("       ")
            print("Incorrect input! Try again, silly!")
            break

        elif int(selection) == 0:
            print("Hello! Welcome to Dominosa!!")
            print("What would you like to do!?")
            print("  ")
            print("1. Play.")
            print("   ")
            print("2. Instructions.")
            print("     ")
            print("3. Watch the computer play.")
            print("     ")
            print("4. Play against the computer.")
            print("    ")
            print("5. Play a Random board")
            print("       ")

#if selection.type() is float:
 #   print("Incorrect input! Try again, silly!")


def prettyprintboards(array):
    for r in array:
        for c in r:
            print(c, end=" ")
        print()

def placedomino(x, y,array1):
    array1[int(x)][int(y)] = "▼"
    prettyprintboards(array1)

def description():
    print("       ")
    print("Dominosa is a logic puzzle with simple rules and challenging solutions.")
    print("        ")
    print("The rules are simple. You have to find the location of all dominoes on the grid. "
          "A domino is a pair of numbers."
          " You can have only one of each pair.")


def howtoplay():
    print("Playing Dominosa consists of 5 easy steps.")
    print("1. Select a board")
    print("2. Enter the x values of where you want to place your first domino half ")
    print("3. Enter the y values of where you want to place your first domino half ")
    print("4. Repeat 2 and 3 for the second half.")
    print("5. Rinse and repeat!")

def boardselect(board):
    if board == "bob":
        name=board
        prettyprintboards(bob)
        play(bob, name)

    if board == "carl":
        name = board
        prettyprintboards(carl)
        play(carl, name)

    if board == "joe":
        name = board
        prettyprintboards(joe)
        play(joe, name)


def printSolution(board):
    if board == "joe":
        prettyprintboards(joes)
        print("Oooooh so close!")

def play(pboard, name):
    play = True
    while(play):
        print("      ")
        print("Where do you want to lay your first domino half?")
        choicex = input("Enter the x value")
        choicey = input("Enter the y value")
        placedomino(choicex, choicey, pboard)
        print("Where do you want to lay your second domino half?")
        choicex = input("Enter the x value")
        choicey = input("Enter the y value")
        placedomino(choicex, choicey, pboard)
        response =input("Do you want to give up?")
        if(response == "y"):
            printSolution(name);
            play = False

    playresponse= input("Do you want to play again?")
    if(playresponse == 'y'):
        mainmenu()





bob =            [[0,0,0,3,2],
                  [2,3,2,3,3],
                  [0,3,1,1,1],
                   [1,0,2,2,1],
    ]

carl = [[0,2,0,1,1],
                   [0,2,0,3,2],
                   [3,3,3,2,1],
                   [3,0,1,2,1],
    ]

joe = [[2,3,2,2,1],
           [1,1,0,2,3],
           [0,3,3,1,0],
           [0,3,1,0,2], ]


joes = [[2,3,2,2,1],
                   [1,1,0,2,3],
                   [0,3,3,1,0],
                   [0,3,1,0,2], ]

#List of tuples
#Figure out how to make a list of tuples

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
zip(list_a,list_b)
