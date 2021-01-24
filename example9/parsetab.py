
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "NUMBER PRINT VARIABLEprogram : statementsstatements : statements statement\n                  | statement statement : assignment\n                  | printassignment : VARIABLE '=' exprexpr : expr '+' term\n            | expr '-' term\n            | termterm : term '*' factor\n            | term '/' factor\n            | factorfactor : NUMBERfactor : VARIABLE\n              | '(' expr ')' print : PRINT '(' variables ')' variables : VARIABLE\n                 | variables ',' VARIABLE"
    
_lr_action_items = {')':([11,12,13,15,17,18,25,26,27,28,29,30,31,],[19,-17,-9,-13,-12,-14,31,-18,-10,-11,-7,-8,-15,]),'(':([3,10,16,21,22,23,24,],[9,16,16,16,16,16,16,]),'+':([13,14,15,17,18,25,27,28,29,30,31,],[-9,23,-13,-12,-14,23,-10,-11,-7,-8,-15,]),'*':([13,15,17,18,27,28,29,30,31,],[21,-13,-12,-14,-10,-11,21,21,-15,]),'-':([13,14,15,17,18,25,27,28,29,30,31,],[-9,24,-13,-12,-14,24,-10,-11,-7,-8,-15,]),'NUMBER':([10,16,21,22,23,24,],[15,15,15,15,15,15,]),'/':([13,15,17,18,27,28,29,30,31,],[22,-13,-12,-14,-10,-11,22,22,-15,]),',':([11,12,26,],[20,-17,-18,]),'PRINT':([0,1,2,6,7,8,13,14,15,17,18,19,27,28,29,30,31,],[3,3,-4,-3,-5,-2,-9,-6,-13,-12,-14,-16,-10,-11,-7,-8,-15,]),'VARIABLE':([0,1,2,6,7,8,9,10,13,14,15,16,17,18,19,20,21,22,23,24,27,28,29,30,31,],[4,4,-4,-3,-5,-2,12,18,-9,-6,-13,18,-12,-14,-16,26,18,18,18,18,-10,-11,-7,-8,-15,]),'=':([4,],[10,]),'$end':([1,2,5,6,7,8,13,14,15,17,18,19,27,28,29,30,31,],[-1,-4,0,-3,-5,-2,-9,-6,-13,-12,-14,-16,-10,-11,-7,-8,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([10,16,23,24,],[13,13,29,30,]),'statements':([0,],[1,]),'assignment':([0,1,],[2,2,]),'variables':([9,],[11,]),'factor':([10,16,21,22,23,24,],[17,17,27,28,17,17,]),'program':([0,],[5,]),'statement':([0,1,],[6,8,]),'expr':([10,16,],[14,25,]),'print':([0,1,],[7,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','py_yacc.py',18),
  ('statements -> statements statement','statements',2,'p_statements','py_yacc.py',25),
  ('statements -> statement','statements',1,'p_statements','py_yacc.py',26),
  ('statement -> assignment','statement',1,'p_statement','py_yacc.py',37),
  ('statement -> print','statement',1,'p_statement','py_yacc.py',38),
  ('assignment -> VARIABLE = expr','assignment',3,'p_assignment','py_yacc.py',45),
  ('expr -> expr + term','expr',3,'p_expr','py_yacc.py',54),
  ('expr -> expr - term','expr',3,'p_expr','py_yacc.py',55),
  ('expr -> term','expr',1,'p_expr','py_yacc.py',56),
  ('term -> term * factor','term',3,'p_term','py_yacc.py',68),
  ('term -> term / factor','term',3,'p_term','py_yacc.py',69),
  ('term -> factor','term',1,'p_term','py_yacc.py',70),
  ('factor -> NUMBER','factor',1,'p_factor_num','py_yacc.py',82),
  ('factor -> VARIABLE','factor',1,'p_factor','py_yacc.py',89),
  ('factor -> ( expr )','factor',3,'p_factor','py_yacc.py',90),
  ('print -> PRINT ( variables )','print',4,'p_print','py_yacc.py',100),
  ('variables -> VARIABLE','variables',1,'p_variables','py_yacc.py',108),
  ('variables -> variables , VARIABLE','variables',3,'p_variables','py_yacc.py',109),
]