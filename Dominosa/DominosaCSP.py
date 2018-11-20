import itertools
from csp import forward_checking, mrv, AC3, backtracking_search, mac, unordered_domain_values, tree_csp_solver, _BGRID, \
    _CELL, _BOXES, _COLS
from csp import CSP,flatten,different_values_constraint
import re
from boardlibrary import bob

def flatten(seqs): return sum(seqs, [])

easy1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'  # noqa
harder1 = '4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'  # noqa

_R3 = list(range(2))
_CELL = itertools.count().__next__
_BGRID = [[[[_CELL() for x in _R3] for y in _R3] for bx in _R3] for by in _R3]
_BOXES = flatten([list(map(flatten, brow)) for brow in _BGRID])
_ROWS = flatten([list(map(flatten, zip(*brow))) for brow in _BGRID])
_COLS = list(zip(*_ROWS))

_NEIGHBORS = {v: set() for v in flatten(_ROWS)}
for unit in map(set, _BOXES + _ROWS + _COLS):
    for v in unit:
        _NEIGHBORS[v].update(unit - set([v]))


class Dominosa(CSP):
    R3 = _R3
    Cell = _CELL
    bgrid = _BGRID
    boxes = _BOXES
    rows = _ROWS
    cols = _COLS
    neighbors = _NEIGHBORS

    def __init__(self, grid):
        """Hello"""
        """Build a Sudoku problem from a string representing the grid:
        the digits 1-9 denote a filled cell, '.' or '0' an empty one;
        other characters are ignored."""
        squares = iter(re.findall(r'\d|\.', grid))
        domains = {var: [ch] if ch in '123456780' else '123456789'
                   for var, ch in zip(flatten(self.rows), squares)}
        # Too many squares
        CSP.__init__(self, None, domains, self.neighbors, different_values_constraint)



e = Dominosa(easy1)
#e.display(e.infer_assignment())
_R4 = list(range(2))
_CELL = itertools.count().__next__
print(_CELL)
_uGRID = [[[[_CELL() for x in _R4] for y in _R4] for bx in _R4]]
print(_uGRID)
_ROWSs = [list(map(flatten, zip(*brow))) for brow in _uGRID]
print(([list(map(flatten, zip(*brow))) for brow in _uGRID]))
print(list((zip(*_ROWSs))))

my_list = [[]]

#AC3(e); e.display(e.infer_assignment())
#h = Dominosa(harder1)
#print(backtracking_search(h, select_unassigned_variable=mrv, inference=forward_checking) is not None)
