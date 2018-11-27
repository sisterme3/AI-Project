from csp import CSP,different_values_constraint,lcv, mrv, backtracking_search,forward_checking,mac
from boardlibrary import EasyDoesIt, EasyCarl,EasyJoe,MediumJoe,Alittlebitharder,MediumCarl, SuperHard, ActuallyHard,ReallyHard,AbsolutelyGenius
from boardlibrary import prettyprintboards


def solveEasyDoesIt():
    print('EasyDoesIt')
    print(prettyprintboards(EasyDoesIt))

    EasyDoesIt1 = ['0|2','0|2','0|2','0|0','2|2','0|0','0|2','0|0','0|1','1|2','0|1','1|1','0|1','1|1','1|1','1|2','1|2']

    d2 = {     1: EasyDoesIt1,
               2: EasyDoesIt1,
               3: EasyDoesIt1,
               4: EasyDoesIt1,
               5: EasyDoesIt1,
               6: EasyDoesIt1, }

    v2 = d2.keys()

    n2 = {     1: [2, 3, 4, 5, 6],
               2: [1, 3, 4, 5, 6],
               3: [1, 2, 4, 5, 6],
               4: [1, 2, 3, 5, 6],
               5: [1, 2, 3, 4, 6],
               6: [1, 2, 3, 4, 5], }


    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,inference=mac)


def solveEasyJoe():
    print('Easy Joe')
    print(prettyprintboards(EasyJoe))

    EasyJoe1 = ['3|3','3|5','2|5','3|5','2|5','3|3','3|5','1|3','2|3','4|5','1|2','2|4','1|1','2|2','1|4','1|2','1|2']

    d2 = {1: EasyJoe1,
          2: EasyJoe1,
          3: EasyJoe1,
          4: EasyJoe1,
          5: EasyJoe1,
          6: EasyJoe1, }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6],
          2: [1, 3, 4, 5, 6],
          3: [1, 2, 4, 5, 6],
          4: [1, 2, 3, 5, 6],
          5: [1, 2, 3, 4, 6],
          6: [1, 2, 3, 4, 5], }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    print(backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,
                              inference=forward_checking))


def solveEasyCarl():
    print('Easy Carl')
    print(prettyprintboards(EasyCarl))

    EasyCarl1 = ['5|5','3|5','0|5','5|6','0|3','3|6','0|6','0|6','0|5','6|6','0|2','0|6','5|6','2|6','3|5','6|6','0|2']

    d2 = {1: EasyCarl1,
          2: EasyCarl1,
          3: EasyCarl1,
          4: EasyCarl1,
          5: EasyCarl1,
          6: EasyCarl1, }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6],
          2: [1, 3, 4, 5, 6],
          3: [1, 2, 4, 5, 6],
          4: [1, 2, 3, 5, 6],
          5: [1, 2, 3, 4, 6],
          6: [1, 2, 3, 4, 5], }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    print(backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,
                              inference=forward_checking))


def solveAlittle():
    print('A Little Bit Harder')
    print(prettyprintboards(Alittlebitharder))

    ALittle1 = ['1|2','0|2','0|2','0|2','0|1','0|2','0|3','2|3','2|2','0|3','0|1','1|1','0|1','0|3','1|3','1|3','0|0', '1|3','2|3','1|3','1|2','3|3','0|3','0|1','2|3','3|3','0|2','1|3','2|3','1|2','1|1']

    d2 = {1: ALittle1,
          2: ALittle1,
          3: ALittle1,
          4: ALittle1,
          5: ALittle1,
          6: ALittle1,
          7: ALittle1,
          8:ALittle1,
          9: ALittle1,
          10: ALittle1,
          }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6, 7, 8, 9, 10],
          2: [1, 3, 4, 5, 6, 7, 8, 9, 10],
          3: [1, 2, 4, 5, 6, 7, 8, 9, 10],
          4: [1, 2, 3, 5, 6, 7, 8, 9, 10],
          5: [1, 2, 3, 4, 6, 7, 8, 9, 10],
          6: [1, 2, 3, 4, 5, 7, 8, 9, 10],
          7: [1, 2,3, 4, 5, 6, 8, 9, 10],
          8: [1, 2, 3,4, 5, 6, 7, 9, 10],
          9: [1, 2, 3, 4, 5, 6, 7, 8, 10],
          10: [1, 2, 3, 4, 5,6, 7, 8, 9],
          }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,  inference=forward_checking)


def solveMediumJoe():
    print('Medium Joe')
    print(prettyprintboards(MediumJoe))

    MediumJoe1 = ['1|3','3|3','2|3','0|2','1|3','0|2','0|2','1|1','0|1','0|2','0|1','1|3','1|2','0|2','1|2','2|3','2|2','1|2','0|3','2|3','2|3','1|1','0|3','3|3','1|3','0|0','2|3','0|3','0|2','0|2','1|1']

    d2 = {1: MediumJoe1,
          2: MediumJoe1,
          3: MediumJoe1,
          4: MediumJoe1,
          5: MediumJoe1,
          6: MediumJoe1,
          7: MediumJoe1,
          8: MediumJoe1,
          9: MediumJoe1,
          10: MediumJoe1,

    }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6, 7, 8, 9, 10],
          2: [1, 3, 4, 5, 6, 7, 8, 9, 10],
          3: [1, 2, 4, 5, 6, 7, 8, 9, 10],
          4: [1, 2, 3, 5, 6, 7, 8, 9, 10],
          5: [1, 2, 3, 4, 6, 7, 8, 9, 10],
          6: [1, 2, 3, 4, 5, 7, 8, 9, 10],
          7: [1, 2,3, 4, 5, 6, 8, 9, 10],
          8: [1, 2, 3,4, 5, 6, 7, 9, 10],
          9: [1, 2, 3, 4, 5, 6, 7, 8, 10],
          10: [1, 2, 3, 4, 5,6, 7, 8, 9],  }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    print(backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,
                              inference=forward_checking))


def solveMediumCarl():
    print('Medium Carl')
    print(prettyprintboards(MediumCarl))

    MediumCarl1 = ['0|3','0|3','3|3','2|3','0|3','1|3','2|3','0|3','0|1','1|3','2|3','0|0','1|1','2|3','0|2','0|1','1|2','1|2','0|0','1|1','2|3','0|1','0|1','1|3','1|1','0|0','1|2','2|3','0|1','0|2','2|2']

    d2 = {1: MediumCarl1,
          2: MediumCarl1,
          3: MediumCarl1,
          4: MediumCarl1,
          5: MediumCarl1,
          6: MediumCarl1,
          7: MediumCarl1,
          8: MediumCarl1,
          9: MediumCarl1,
          10: MediumCarl1,
          }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6, 7, 8, 9, 10],
          2: [1, 3, 4, 5, 6, 7, 8, 9, 10],
          3: [1, 2, 4, 5, 6, 7, 8, 9, 10],
          4: [1, 2, 3, 5, 6, 7, 8, 9, 10],
          5: [1, 2, 3, 4, 6, 7, 8, 9, 10],
          6: [1, 2, 3, 4, 5, 7, 8, 9, 10],
          7: [1, 2,3, 4, 5, 6, 8, 9, 10],
          8: [1, 2, 3,4, 5, 6, 7, 9, 10],
          9: [1, 2, 3, 4, 5, 6, 7, 8, 10],
          10: [1, 2, 3, 4, 5,6, 7, 8, 9],  }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    print(backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,
                              inference=forward_checking))


def solveActually():
    print('Actually Hard')
    print(prettyprintboards(ActuallyHard))

    Actually = ['1|3','0|4','1|4','1|3','2|4','3|4','2|3','1|3','1|3','1|2','1|3','2|3','3|4','1|2','4|4','0|2','2|4','0|3','2|2','0|3','0|2','0|2','0|0','2|4','0|1',
                '1|4','0|1','3|4','0|4','3|3','3|4','2|3','3|4','1|2','1|3','1|1','1|4','0|1','3|4','0|4','2|3','0|4','0|2','0|2','0|3','2|4','1|3','0|4','1|2']

    d2 = {1: Actually,
          2: Actually,
          3: Actually,
          4: Actually,
          5: Actually,
          6: Actually,
          7: Actually,
          8: Actually,
          9: Actually,
         10: Actually,
         11: Actually,
         12: Actually,
         13: Actually,
         14: Actually,
         15: Actually,

    }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6, 7, 8, 9, 10],
          2: [1, 3, 4, 5, 6, 7, 8, 9, 10],
          3: [1, 2, 4, 5, 6, 7, 8, 9, 10],
          4: [1, 2, 3, 5, 6, 7, 8, 9, 10],
          5: [1, 2, 3, 4, 6, 7, 8, 9, 10],
          6: [1, 2, 3, 4, 5, 7, 8, 9, 10],
          7: [1, 2,3, 4, 5, 6, 8, 9, 10],
          8: [1, 2, 3,4, 5, 6, 7, 9, 10],
          9: [1, 2, 3, 4, 5, 6, 7, 8, 10],
          10: [1, 2, 3, 4, 5, 6, 7, 8, 9],
          11: Actually,
          12: Actually,
          13: Actually,
          14: Actually,
          15: Actually,
          }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    print(backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,
                              inference=forward_checking))


def solveReally():
    print('Really Hard')
    print(prettyprintboards(ReallyHard))

    Really = ['1|2','2|3','1|2','1|4','0|4','1|2','1|4','3|4','0|1','1|1','1|4','3|4','1|3','1|3','1|2','0|4','3|3','1|2','2|3','0|2','0|3','2|3','1|3','0|3','2|3',
              '1|2','2|2','3|4','3|4','1|4','0|2','1|3','0|4','3|3','0|4','0|1','0|1','0|3','4|4','0|0','1|4','0|2','0|3','0|4','0|4','2|4','0|2','2|2','3|4']

    d2 = {1: Really,
          2: Really,
          3: Really,
          4: Really,
          5: Really,
          6: Really,
          7: Really,
          8: Really,
          9: Really,
          10: Really,
          11: Really,
          12: Really,
          13: Really,
          14: Really,
          15: Really,
          }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6],
          2: [1, 3, 4, 5, 6],
          3: [1, 2, 4, 5, 6],
          4: [1, 2, 3, 5, 6],
          5: [1, 2, 3, 4, 6],
          6: [1, 2, 3, 4, 5], }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    print(backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,
                              inference=forward_checking))


def solveSuper():
    print('Super Hard')
    print(prettyprintboards(SuperHard))

    Super = ['3|4','1|4','1|2','2|4','2|4','0|1','2|2','1|3','1|2','0|3','0|2','0|2','0|1','2|3','1|2','0|2','0|1','1|3','3|4','0|4','0|2','2|2','0|3','4|4','1|2',
             '2|3','0|0','1|4','3|4','1|1','0|2','0|1','0|4','1|3','2|3','0|4','0|1','2|3','3|4','0|3','2|3','0|1','3|4','0|3','3|4','1|4','0|1','0|4','1|4']

    d2 = {1: Super,
          2: Super,
          3: Super,
          4: Super,
          5: Super,
          6: Super,
          7: Super,
          8: Super,
          9: Super,
          10: Super,
          11: Super,
          12: Super,
          13: Super,
          14: Super,
          15: Super,
          }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6],
          2: [1, 3, 4, 5, 6],
          3: [1, 2, 4, 5, 6],
          4: [1, 2, 3, 5, 6],
          5: [1, 2, 3, 4, 6],
          6: [1, 2, 3, 4, 5], }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    print(backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,
                              inference=forward_checking))



def solveGenius():
    print('Absolutely Genius')
    print(prettyprintboards(AbsolutelyGenius))

    Genius = []

    d2 = {1: Genius,
          2: Genius,
          3: Genius,
          4: Genius,
          5: Genius,
          6: Genius,
          7: Genius,
          8: Genius,
          9: Genius,
          10: Genius,
          11: Genius,
          12: Genius,
          13: Genius,
          14: Genius,
          15: Genius,
          16: Genius,
          17: Genius,
          18: Genius,
          19: Genius,
          20: Genius,
          21: Genius,
          22: Genius,
          23: Genius,
          24: Genius,
          25: Genius,
          26: Genius,
          27: Genius,
          28: Genius,
          }

    v2 = d2.keys()

    n2 = {1: [2, 3, 4, 5, 6],
          2: [1, 3, 4, 5, 6],
          3: [1, 2, 4, 5, 6],
          4: [1, 2, 3, 5, 6],
          5: [1, 2, 3, 4, 6],
          6: [1, 2, 3, 4, 5], }

    Dominosa1 = CSP(v2, d2, n2, different_values_constraint)

    print(backtracking_search(Dominosa1, select_unassigned_variable=mrv, order_domain_values=lcv,
                              inference=forward_checking))


def solveboard(array):
    if int(array) == 1:
        solveEasyDoesIt()
    elif int(array) == 2:
        solveEasyJoe()
    elif int(array) == 3:
        solveEasyCarl()
    elif int(array) == 4:
        solveAlittle()
    elif int(array) == 5:
        solveMediumJoe()
    elif int(array) == 6:
        solveMediumCarl()
    elif int(array) == 7:
        solveSuper()
    elif int(array) == 8:
        solveActually()
    elif int(array) == 9:
        solveReally()
    elif int(array) == 10:
        solveGenius()


