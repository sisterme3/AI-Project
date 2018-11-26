from boardlibrary import EasyDoesIt, EasyCarl, EasyJoe, AbsolutelyGenius,MediumCarl,MediumJoe,SuperHard,ReallyHard,Alittlebitharder,ActuallyHard
from boardlibrary import EasyDoesIt_solution, EasyCarl_solution, EasyJoe_solution, Alittlebitharder_Solution,ActuallyHard_solution,SuperHard_solution,MediumCarl_solution,MediumJoe_solution,ReallyHard_solution,AbsolutelyGenius_solution
from DominosaSolver import prettyprintboards
import random



def checkifdone(array):
    return True


def play(pboard, name, count=0):
    play = True
    while play:
        print("      ")
        print("Where do you want to lay your first domino half?")
        choicex = input("Enter the x value")
        if int(choicex) < 0 or int(choicex) > len(pboard[0]):
            print('Out of range!' 'Remember that this boards starts at 0 and ends at ' + str(len(pboard[0])-1))
            choicex = input("Please reenter your x!")
        else:
           choicey = input("Enter the y value")
           if int(choicey) < 0 or int(choicey) > len(pboard):
               print('Out of range!' 'Remember that this boards starts at 0 and ends at' + str(len(pboard)-1))
               choicey = input("Please reenter your y!")
           else:
              print("Where do you want to lay your second domino half?")
              choicew = input("Enter the x value")
              if int(choicew) < 0 or int(choicew) > len(pboard[0]):
                  print('Out of range!' 'Remember that this boards starts at 0 and ends at ' + str(len(pboard[0]) - 1))
                  choicew = input("Please reenter your x!")
              else:
                  choicev = input("Enter the y value")
                  if int(choicev) < 0 or int(choicev) > len(pboard):
                      print('Out of range!' 'Remember that this boards starts at 0 and ends at' + str(len(pboard) - 1))
                      choicev = input("Please reenter your y!")
                  placedomino(choicex, choicey, choicew, choicev, pboard)
        count += 1
        print('Number of current moves: ' + str(count))
        response = input('Do you want to give up? y or n')
        if response == 'y':
            printSolution(name)
            r = input('Would you like to play again? y or n')
           # if r == 'y':
            #if r == 'n':
             #   print('Goodbye! Come back soon!')
              #  break


def placedomino(x, y,w,v,array1):
    if x == w and y<v:
        array1[int(x)][int(y)] = "▶"
        array1[int(w)][int(v)] = "◀"
        prettyprintboards(array1)
    elif x == w and y > v:
        array1[int(x)][int(y)] = "◀"
        array1[int(w)][int(v)] = "▶"
        prettyprintboards(array1)
    elif y==v and x<w:
        array1[int(x)][int(y)] = "▼"
        array1[int(w)][int(v)] = "▲"
        prettyprintboards(array1)
    elif y==v and x>w:
        array1[int(x)][int(y)] = "▲"
        array1[int(w)][int(v)] = "▼"
        prettyprintboards(array1)


def randomResponse(responsearray):
    print(random.choice(responsearray))

def printSolution(board):
        responsearray = ['Ooooh, you could do better than that!', 'You almost has it! Why!!', 'WOW. Nice try, N00B', ]
        if board == "Easy Does It":
            print("Here is what you had...")
            prettyprintboards(EasyDoesIt)
            print("Here is the solution!")
            prettyprintboards(EasyDoesIt_solution)
            randomResponse(responsearray)

        elif board == "Easy Carl ":
            print("Here is what you had...")
            prettyprintboards(EasyCarl)
            print("Here is the solution!")
            prettyprintboards(EasyCarl_solution)
            randomResponse(responsearray)

        elif board == "Easy Joe":
            print("Here is what you had...")
            prettyprintboards(EasyJoe)
            print("Here is the solution!")
            prettyprintboards(EasyJoe_solution)
            randomResponse(responsearray)

        elif board == "A Little Bit Harder":
            print("Here is what you had...")
            prettyprintboards(Alittlebitharder)
            print("Here is the solution!")
            prettyprintboards(Alittlebitharder_Solution)
            randomResponse(responsearray)

        elif board == "Medium Joe":
            print("Here is what you had...")
            prettyprintboards(MediumJoe)
            print("Here is the solution!")
            prettyprintboards(MediumJoe_solution)
            randomResponse(responsearray)

        elif board == "Medium Carl":
            print("Here is what you had...")
            prettyprintboards(MediumCarl)
            print("Here is the solution!")
            prettyprintboards(MediumCarl_solution)
            randomResponse(responsearray)

        elif board == "Actually Hard":
            print("Here is what you had...")
            prettyprintboards(ActuallyHard)
            print("Here is the solution!")
            prettyprintboards(ActuallyHard_solution)
            randomResponse(responsearray)

        elif board == "Super Hard":
            print("Here is what you had...")
            prettyprintboards(SuperHard)
            print("Here is the solution!")
            prettyprintboards(SuperHard_solution)
            randomResponse(responsearray)

        elif board == "Really Hard":
            print("Here is what you had...")
            prettyprintboards(ReallyHard)
            print("Here is the solution!")
            prettyprintboards(ReallyHard_solution)
            randomResponse(responsearray)

        elif board == "Absolutely Genius":
            print("Here is what you had...")
            prettyprintboards(AbsolutelyGenius)
            print("Here is the solution!")
            prettyprintboards(AbsolutelyGenius_solution)
            randomResponse(responsearray)