from tkinter import *
import random
import numpy


root = Tk()

label = Label(root, text="Dominosa")
topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)
label.pack()

#function that will create the board 3x3 (really easy)

def createBoard():
    grid = [[1] * 4 for n in range(4)]
    root.geometry("800x600")
    canvas = Canvas(root, width=400, height=400)
    w = 70
    x, y = 0, 0
    for row in grid:
        for col in row:
            canvas.create_rectangle(x, y, w, w,)

            x = x + w
        y = y+w
        x = 0
        canvas.pack()
    #fillBoard()
    "Fills the board and squares with values/dominoes"
def fillBoard():
    #random.sample()

    "Resets current board"
def resetBoard():
    createBoard()
    "This will create a harder board 5x5 and the upcoming functions will increase difficulty"
def createBoardHard():

    "8x8 board"
def createBoardVeryhard():

    "25x25 board"
def createBoardImpossible():

    "Function that will darken the clicked dominoes"
def highlightDominoes():

    "This function will let the AI solve the board for the player.  a CSP algorithm will be used"

def solveBoard():


    "_Buttons for GUI"
#button one will be bound to two functions one that creates the board and the other
#that fills the board with numbers/dominoes"""

button1 = Button(topFrame, text="Start", fg="red", command=createBoard)
button2 = Button(topFrame, text="Reset", fg="green")
button3 = Button(topFrame, text="Solve", fg="blue")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

checkForHighlight = Checkbutton(bottomFrame, text = "Highlight dominoes")
checkForHighlight.grid(columnspan= 2)
checkForHighlight.pack(side=LEFT)
root.mainloop()