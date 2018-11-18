import itertools
from csp import Dominosa
from csp import forward_checking, mrv, AC3, backtracking_search

easy1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'  # noqa
harder1 = '4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'  # noqa


e = Dominosa(easy1)
e.display(e.infer_assignment())

AC3(e); e.display(e.infer_assignment())
h = Dominosa(harder1)
backtracking_search(h, select_unassigned_variable=mrv, inference=forward_checking) is not None
