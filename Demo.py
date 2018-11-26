from DominosaSolver import prettyprintboards
from boardlibrary import Demoboard, Demoboard_solution
from Play import placedomino
import time

def checkifdone(array, array1):
    if array == array1:
        return True

def demoplay():
    print('Demoboard')

    prettyprintboards(Demoboard)
    print("This is your board!")
    print("This board is " + str(len(Demoboard)-1) + ' by ' + str(len(Demoboard[0])-1)+ ' so you have to make sure your answers are in that range starting from 0 (X: 0-1  & Y:0-3)!')
    print("Lets start with our first Domino half")
    print('1|6 seems like a good Domino pair! Lets input it!')
    print("       ")
    choiceX = input('First: input 1 for x')
    wrong = True
    while wrong:
     if int(choiceX)<= 0 or int(choiceX)>1:
        print("Bad input! ")
        choiceX = input("Please enter 1!")
     elif int(choiceX) == 1:
       print("       ")
       choiceY = input('Good, now input 0 for Y!')
       print("       ")
       if int(choiceY) != 0:
           print("Bad input! ")
           choiceY = input("Please enter 0!")
       elif int(choiceY) ==0:
           print("       ")
           print("Good, that's your first half!")
           print("       ")
           choicew = input("Now enter 0 for both x and y")
           if int(choicew) != 0:
               print("Bad input! ")
               choicew = input("Please enter 0!")
               print("       ")
           elif int(choicew) == 0:
               choicev = input('Good, now input 0 for Y!')
               if int(choicev) != 0:
                   print("Bad input! ")
                   print("       ")
                   choicev = input("Please enter 0!")
               elif int(choicev) == 0:
                   placedomino(choiceX,choiceY, choicew, choicev, Demoboard)
                   print("Great! Those are your first pieces!")
               print("Let's keep going! 6|3 seems like another nice pair!")
               print("       ")
               choiceX = input("Input 0 for x!")
               if int(choiceX) != 0:
                   print("Bad input! ")
                   print("       ")
                   choiceX = input("Please enter 0!")
               elif int(choiceX) == 0:
                   print("       ")
                   choiceY = input('Good, now input 3 for Y!')
                   if int(choiceY) != 3:
                       print("Bad input! ")
                       print("       ")
                       choiceY = input("Please enter 3!")
                   elif int(choiceY) == 3:
                       print("       ")
                       print("Good, that's your first half!")
                       print("       ")
                       choicew = input("Now enter 1 for x!")
                       if int(choicew) != 1:
                           print("Bad input! ")
                           print("       ")
                           choicew = input("Please enter 1!")
                       elif int(choicew) == 1:
                           print("       ")
                           choicev = input('Good, now input 3 for Y!')
                           if int(choicev) != 3:
                               print("Bad input! ")
                               print("       ")
                               choicev = input("Please enter 3!")
                           elif int(choicev) == 3:
                               placedomino(choiceX, choiceY, choicew, choicev, Demoboard)
                               print("Lets keep the ball rolling!!")
                               print("       ")
                           print("Let's keep going! 2|4 seems like our next step!")
                           print("       ")
                           choiceX = input("Input 1 for x!")
                           if int(choiceX) != 1:
                               print("Bad input! ")
                               print("       ")
                               choiceX = input("Please enter 1!")
                           elif int(choiceX) == 1:
                               print("       ")
                               choiceY = input('Good, now input 1 for Y!')
                               if int(choiceY) != 1:
                                   print("Bad input! ")
                                   print("       ")
                                   choiceY = input("Please enter 1!")
                               elif int(choiceY) == 1:
                                   print("       ")
                                   print("Good, that's your first half!")
                                   print("       ")
                                   choicew = input("Now enter 1 for x!")
                                   if int(choicew) != 1:
                                       print("Bad input! ")
                                       print("       ")
                                       choicew = input("Please enter 1!")
                                   elif int(choicew) == 1:
                                       print("       ")
                                       choicev = input('Good, now input 2 for Y!')
                                       if int(choicev) != 2:
                                           print("Bad input! ")
                                           print("       ")
                                           choicev = input("Please enter 2!")
                                           print("       ")
                                       elif int(choicev) == 2:
                                           placedomino(choiceX, choiceY, choicew, choicev, Demoboard)
                                           print("One more pair!!!")
                                           print("       ")
                                       print("Let's keep going! 3|4 seems like our last pair!")
                                       print("       ")
                                       choiceX = input("Input 0 for x!")
                                       print("       ")
                                       if int(choiceX) != 0:
                                           print("Bad input! ")
                                           choiceX = input("Please enter 0!")
                                           print("       ")
                                       elif int(choiceX) == 0:
                                           choiceY = input('Good, now input 1 for Y!')
                                           print("       ")
                                           if int(choiceY) != 1:
                                               print("Bad input! ")
                                               choiceY = input("Please enter 1!")
                                               print("       ")
                                           elif int(choiceY) == 1:
                                               print("Good, that's your first half!")
                                               print("       ")
                                               choicew = input("Now enter 0 for x!")
                                               if int(choicew) != 0:
                                                   print("Bad input! ")
                                                   print("       ")
                                                   choicew = input("Please enter 0!")
                                               elif int(choicew) == 0:
                                                   print("       ")
                                                   choicev = input('Good, now input 2 for Y!')
                                                   if int(choicev) != 2:
                                                       print("Bad input! ")
                                                       print("       ")
                                                       choicev = input("Please enter 2!")
                                                   elif int(choicev) == 2:
                                                       placedomino(choiceX, choiceY, choicew, choicev, Demoboard)
                                                       if checkifdone(Demoboard, Demoboard_solution):
                                                           print(
                                                               'Congrats! You are now ready for the bigger and better boards!!!!')
                                                           print('Thanks for playing! Now going to the main menu.....')
                                                           time.sleep(5)
                                                           break

