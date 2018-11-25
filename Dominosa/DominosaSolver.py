import itertools
from csp import CSP,flatten,different_values_constraint,lcv, mrv, mac, first_unassigned_variable, unordered_domain_values, no_inference,backtracking_search,forward_checking, AC3, tree_csp_solver
from boardlibrary import EasyDoesIt


#def solveboard(array):



doublesix = ['0|0', '0|1', '0|2', '0|3', '0|4','0|5','0|6','1|1','1|2','1|3','1|4','1|5','1|6','2|2','2|3','2|4','2|5','2|6','3|3','3|4','3|5','3|6','4|4', '4|5','4|6', '5|5','5|6','6|6']


d2 = {1: doublesix,
      2:  doublesix,
      3:  doublesix,
      4:  doublesix,
      5:  doublesix,
      6:  doublesix,}

v2 = d2.keys()

n2 = {1: [2,3,4,5,6],
      2: [1,3,4,5,6],
      3: [1,2,4,5,6],
      4: [1,2,3,5,6],
      5: [1,2,3,4,6],
      6: [1,2,3,4,5],
      }

Dominosa1 = CSP(v2,d2,n2,different_values_constraint)

print(backtracking_search(Dominosa1, select_unassigned_variable= mrv, order_domain_values=lcv, inference=forward_checking))
