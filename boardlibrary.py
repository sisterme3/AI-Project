"""The library of boards that can be played within the game."""




Demoboard = [[1,3,4,6],
             [6,2,4,3],
]

Demoboard_solution =  [['▼','▶','◀','▼'],
                       ['▲','▶','◀','▲'],
]

EasyDoesIt =            [[2,0,0,1],
                         [0,0,1,1],
                         [2,2,1,2],

]

EasyDoesIt_solution = [
                         ['▼','▼','▶','◀'],
                         ['▲','▲','▶','◀'],
                         ['▶','◀','▶','◀'],
]

EasyJoe = [
    [3,3,1,1],
    [5,3,2,2],
    [2,5,4,1],
]


EasyJoe_solution = [
    ['▶', '◀', '▶', '◀'],
    ['▼', '▶', '◀', '▼'],
    ['▲', '▶', '◀', '▲'],
]


EasyCarl = [
    [5,0,5,3],
    [5,6,6,6],
    [3,0,2,0],
]


EasyCarl_solution = [
    ['▼', '▶', '◀', '▼'],
    ['▲', '▶', '◀', '▲'],
    ['▶', '◀', '▶', '◀'],
]

Alittlebitharder = [[2,1,3,2,2],
                    [0,1,3,3,1],
                    [2,0,0,2,1],
                    [0,3,1,3,0],
]


Alittlebitharder_Solution = [['▶','◀','▼','▶','◀'],
                             ['▶','◀','▲','▼','▼'],
                             ['▼','▶','◀','▲','▲'],
                             ['▲','▶','◀','▶','◀'],
]


MediumJoe =     [[3,1,3,0,0],
                [3,1,2,3,2],
                [2,0,2,3,0],
                [0,2,1,1,1],
]


MediumJoe_solution=[['▼','▶','◀','▶','◀'],
                   ['▲','▼','▼','▶','◀'],
                   ['▼','▲','▲','▶','◀'],
                   ['▲','▶','◀','▶','◀'],
]


MediumCarl =            [[0,3,2,1,1],
                         [3,0,0,0,0],
                         [3,1,1,1,2],
                         [2,3,2,3,2],
]

MediumCarl_solution =[["▶","◀","▼","▶","◀"],
                      ["▼","▼","▲","▶","◀"],
                      ["▲","▲","▼","▼","▼"],
                      ["▶","◀","▲","▲","▲"],
    ]


ActuallyHard = [[1,3,2,3,2,0],
                [4,3,1,4,2,4],
                [0,4,3,4,0,2],
                [1,3,1,0,3,1],
                [4,2,1,2,0,0],
]

ActuallyHard_solution = [['▼','▼','▶','◀','▼','▼'],
                         ['▲','▲','▼','▼','▲','▲'],
                         ['▼','▼','▲','▲','▼','▼'],
                         ['▲','▲','▼','▼','▲','▲'],
                         ['▶','◀','▲','▲','▶','◀'],
]

ReallyHard = [
                [2,1,3,1,4,4],
                [2,1,2,2,0,0],
                [1,4,0,3,1,4],
                [4,3,3,4,0,2],
                [0,1,2,3,3,0],
]

ReallyHard_solution =[
    ['▼', '▼', '▶', '◀', '▶', '◀'],
    ['▲', '▲', '▼', '▼', '▶', '◀'],
    ['▶', '◀', '▲', '▲', '▼', '▼'],
    ['▼', '▶', '◀', '▼', '▲', '▲'],
    ['▲', '▶', '◀', '▲', '▶', '◀'],


]

SuperHard = [
                [4,3,4,3,2,3],
                [1,0,3,0,0,4],
                [2,2,3,4,1,0],
                [4,0,1,4,3,2],
                [2,1,0,1,1,2],

]


SuperHard_solution = [
    ['▼', '▼', '▶', '◀', '▶', '◀'],
    ['▲', '▲', '▼', '▶', '◀', '▼'],
    ['▼', '▼', '▲', '▼', '▼', '▲'],
    ['▲', '▲', '▼', '▲', '▲', '▼'],
    ['▶', '◀', '▲', '▶', '◀', '▲'],




]
AbsolutelyGenius = [
    [0,0,6,6,4,4,2,3],
    [5,2,0,1,1,5,4,6],
    [1,5,0,4,4,3,2,0],
    [2,2,4,6,1,6,2,0],
    [6,5,4,5,3,0,1,3],
    [2,3,5,4,2,6,1,3],
    [5,1,5,1,6,3,3,0],
]

AbsolutelyGenius_solution = [
    ['▼', '▼','▶', '◀', '▼', '▼', '▶', '◀'],
    ['▲', '▲', '▶', '◀', '▲', '▲', '▶', '◀'],
    ['▼', '▼', '▶', '◀', '▶', '◀', '▼', '▼'],
    ['▲', '▲', '▼', '▼', '▼', '▼', '▲', '▲'],
    ['▼', '▼', '▲', '▲', '▲', '▲', '▼', '▼'],
    ['▲', '▲', '▼', '▶', '◀', '▼', '▲', '▲'],
    ['▶', '◀', '▲', '▶', '◀', '▲', '▶', '◀'],


]


"""Allows for the boards to be pretty-printed"""

def prettyprintboards(array):
    for r in array:
        for c in r:
            print(c, end=" ")
        print()


