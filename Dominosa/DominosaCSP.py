import itertools
from csp import forward_checking, mrv, AC3, backtracking_search, mac, unordered_domain_values, tree_csp_solver, _BGRID, \
    _CELL, _BOXES, _COLS
from csp import CSP,flatten,different_values_constraint
import re
from boardlibrary import bob

rgbp = ['R', 'G', 'B', 'P']

# The 23 wards of Tokyo

d2 = {'ADACHI' : rgbp, 'KATSU' : rgbp, 'EDOG' : rgbp, 'KOTO' : rgbp, 'CHUO': rgbp, 'SUMI': rgbp, 'TAITO':  rgbp, 'ARAK':   rgbp, 'KITA':   rgbp, 'BUNK':   rgbp, 'CHIY':   rgbp, 'MINA':   rgbp, 'SHIN':   rgbp,
    'SHINA':  rgbp,
    'OTA':    rgbp,
    'MEGU':   rgbp,
    'SETA':   rgbp,
    'SUGI':   rgbp,
    'NAKA':   rgbp,
    'NERI':   rgbp,
    'ITA':    rgbp,
    'TOSHI':  rgbp,
    'SHIB' :  rgbp,
      }

v2 = d2.keys()

n2 = {'ADACHI' : ['KATSU','SUMI','ARAK','KITA'],
      'KATSU' : ['ADACHI', 'EDOG','SUMI'],
      'EDOG' : ['KATSU', 'KOTO','SUMI'],
      'KOTO' : ['EDOG','CHUO','SUMI'],
      'CHUO':['KOTO','SUMI','MINA','CHIY','TAITO'],
      'TAITO':['CHUO','SUMI','CHIY','BUNK','KITA','ARAK'],
      'SUMI':['KATSU','EDOG','KOTO','CHUO','TAITO','ADACHI','ARAK'],
      'ARAK': ['TAITO', 'BUNK', 'SUMI', 'ADACHI', 'KITA'],
      'KITA': ['ADACHI', 'ARAK', 'BUNK', 'TOSHI', 'ITA','TAITO'],
      'BUNK': ['ARAK', 'TAITO', 'CHIY', 'SHIN', 'TOSHI', 'KITA'],
      'CHIY': ['CHUO', 'MINA', 'SHIN', 'BUNK', 'TAITO'],
      'MINA': ['CHUO', 'CHIY', 'SHIN', 'SHIB', 'SHINA'],
      'SHIN': ['MINA', 'CHIY', 'BUNK', 'TOSHI', 'NERI', 'NAKA', 'SHIB'],
      'SHINA': ['MINA', 'SHIB', 'MEGU', 'OTA'],
      'OTA': ['SHINA', 'MEGU', 'SETA'],
      'MEGU': ['SHIB', 'MINA', 'SHINA', 'OTA', 'SETA', ],
      'SETA': ['OTA', 'MEGU', 'SHIB', 'SUGI'],
      'SUGI': ['SETA', 'NERI', 'NAKA', 'SHIB'],
      'NAKA': ['SUGI', 'SHIB', 'SHIN', 'TOSHI', 'NERI'],
      'NERI': ['TOSHI', 'NAKA', 'SUGI', 'SHIN', 'ITA'],
      'ITA': ['KITA', 'NERI', 'TOSHI'],
      'TOSHI': ['KITA', 'BUNK', 'ITA', 'NERI', 'NAKA', 'SHIN'],
      'SHIB': ['NAKA', 'SHIN', 'SUGI', 'SETA', 'MEGU', 'SHINA', 'MINA'],}



class Dominosa(CSP):

    def __init__(self, grid):
        """Hello"""

        squares = iter(re.findall(r'\d|\.', grid))
        domains = {var: [ch] if ch in '123456780' else '123456789'
                   for var, ch in zip(flatten(self.rows), squares)}



def constraint(A, a, B, b):
    if A == B:      # e.g. NSW == NSW
        return True

    if a == b:      # e.g. WA = G and SA = G
        return False

    return True




print(backtracking_search(c2, select_uassigned_variable=mrv,order_domain_values=mac, inference=forward_checking))


#e.display(e.infer_assignment())


#AC3(e); e.display(e.infer_assignment())
#h = Dominosa(harder1)
#print(backtracking_search(h, select_unassigned_variable=mrv, inference=forward_checking) is not None)
