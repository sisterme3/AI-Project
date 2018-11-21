import itertools
from csp import forward_checking, mrv, AC3, backtracking_search, mac, unordered_domain_values, tree_csp_solver, _BGRID, \
    _CELL, _BOXES, _COLS
from csp import CSP,flatten,different_values_constraint
import re
from boardlibrary import bob

doublesix = ['0|0', '0|1', '0|2', '0|3', '0|4','0|5','0|6','1|1','1|2','1|3','1|4','1|5','1|6','2|2','2|3','2|4','2|5','2|6','3|3','3|4','3|5','3|6','4|4', '4|5','4|6', '5|5','5|6','6|6']


d2 = {1: doublesix,
      2:  doublesix,
      3:  doublesix,
      4:  doublesix,
      5:  doublesix,
      6:  doublesix,
      7:  doublesix,
      8:  doublesix,
      9:  doublesix,
      10: doublesix,
      11: doublesix,
      }

v2 = d2.keys()

n2 = {1: [2,3,4,5,6,7,8,9,10,11],
      2: [1,3,4,5,6,7,8,9,10,11],
      3: [1,2,4,5,6,7,8,9,10,11],
      4: [1,2,3,5,6,7,8,9,10,11],
      5: [1,2,3,4,6,7,8,9,10,11],
      6: [1,2,3,4,5,7,8,9,10,11],
      7: [1,2,3,4,5,6,8,9,10,11],
      8: [1,2,3,4,5,6,7,9,10,11],
      9: [1,2,3,4,5,6,7,8,10,11],
      10:[1,2,3,4,5,6,7,8,9,11],
      11:[1,2,3,4,5,6,7,8,9,10],
      }


class Dominosa(CSP):

    def __init__(self, grid):
        """Hello"""
        domains = doublesix


print(CSP.__init__( None, v2, doublesix, different_values_constraint))




#e.display(e.infer_assignment())


#AC3(e); e.display(e.infer_assignment())
#h = Dominosa(harder1)
#print(backtracking_search(h, select_unassigned_variable=mrv, inference=forward_checking) is not None)
