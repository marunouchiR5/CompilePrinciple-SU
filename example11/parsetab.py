
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND DEF IF LEN NUMBER PRINT RETURN VARIABLE WHILEprogram : statementsstatements : statements statement\n                  | statement statement :\n                  | assignment\n                  | operation\n                  | print\n                  | if\n                  | while\n                  | function\n                  | run_function\n                  | returnassignment : VARIABLE '=' NUMBER\n                  | VARIABLE '[' expression ']' '=' NUMBER\n                  | VARIABLE '=' VARIABLE\n                  | VARIABLE '=' VARIABLE '[' expression ']'\n                  | VARIABLE '=' num_listnum_list : '[' numbers ']' numbers : NUMBER\n               | numbers ',' NUMBERoperation : VARIABLE '=' expression\n                 | VARIABLE '+' '=' expression\n                 | VARIABLE '-' '=' expression\n                 | VARIABLE '[' expression ']' '=' expressionexpression : expression '+' term\n                  | expression '-' term\n                  | term\n                  | LEN '(' factor ')' term : term '*' factor\n            | term '/' factor\n            | factorfactor : NUMBER\n              | VARIABLE\n              | VARIABLE '[' expression ']'\n              | '(' expression ')' print : PRINT '(' VARIABLE ')' if : IF '(' condition ')' '{' statements '}' while : WHILE '(' conditions ')' '{' statements '}' conditions : condition\n                  | condition AND conditioncondition : factor '>' factor\n                 | factor '<' factor\n                 | factor '<' '=' factor\n                 | factor '>' '=' factorfunction : DEF VARIABLE '(' variables ')' '{' statements '}' run_function : VARIABLE '(' expressions ')' variables :\n                 | VARIABLE\n                 | variables ',' VARIABLEexpressions : expression\n                   | expressions ',' expressionreturn : RETURN variables"
    
_lr_action_items = {'RETURN':([0,1,4,5,6,8,10,11,12,13,14,17,18,21,22,31,33,39,40,42,43,45,46,59,60,70,71,72,76,82,85,86,89,91,92,95,98,99,100,101,102,104,105,106,107,108,109,110,],[4,4,-47,-6,-11,-8,-3,-7,-10,-12,-5,-9,-2,-48,-52,-32,-33,-27,-13,-15,-31,-17,-21,-36,-49,-22,-23,-46,-35,4,-29,-30,-18,-25,-26,4,-34,4,4,-28,-16,-14,-24,4,-38,4,-37,-45,]),'NUMBER':([19,24,27,28,29,30,44,47,48,54,55,56,58,62,63,64,65,68,69,73,78,80,90,94,],[31,40,31,31,31,31,67,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,103,104,]),'WHILE':([0,1,4,5,6,8,10,11,12,13,14,17,18,21,22,31,33,39,40,42,43,45,46,59,60,70,71,72,76,82,85,86,89,91,92,95,98,99,100,101,102,104,105,106,107,108,109,110,],[2,2,-47,-6,-11,-8,-3,-7,-10,-12,-5,-9,-2,-48,-52,-32,-33,-27,-13,-15,-31,-17,-21,-36,-49,-22,-23,-46,-35,2,-29,-30,-18,-25,-26,2,-34,2,2,-28,-16,-14,-24,2,-38,2,-37,-45,]),'PRINT':([0,1,4,5,6,8,10,11,12,13,14,17,18,21,22,31,33,39,40,42,43,45,46,59,60,70,71,72,76,82,85,86,89,91,92,95,98,99,100,101,102,104,105,106,107,108,109,110,],[3,3,-47,-6,-11,-8,-3,-7,-10,-12,-5,-9,-2,-48,-52,-32,-33,-27,-13,-15,-31,-17,-21,-36,-49,-22,-23,-46,-35,3,-29,-30,-18,-25,-26,3,-34,3,3,-28,-16,-14,-24,3,-38,3,-37,-45,]),'DEF':([0,1,4,5,6,8,10,11,12,13,14,17,18,21,22,31,33,39,40,42,43,45,46,59,60,70,71,72,76,82,85,86,89,91,92,95,98,99,100,101,102,104,105,106,107,108,109,110,],[7,7,-47,-6,-11,-8,-3,-7,-10,-12,-5,-9,-2,-48,-52,-32,-33,-27,-13,-15,-31,-17,-21,-36,-49,-22,-23,-46,-35,7,-29,-30,-18,-25,-26,7,-34,7,7,-28,-16,-14,-24,7,-38,7,-37,-45,]),')':([21,31,33,34,35,36,38,39,43,49,50,52,53,60,61,76,77,79,83,85,86,87,91,92,93,96,97,98,101,],[-48,-32,-33,57,-39,59,-47,-27,-31,72,-50,75,76,-49,84,-35,-41,-42,-40,-29,-30,101,-25,-26,-51,-44,-43,-34,-28,]),'(':([2,3,15,16,19,23,24,27,28,29,30,41,47,48,54,55,56,58,62,63,64,65,68,69,73,78,80,94,],[19,20,27,29,30,38,30,30,30,30,30,64,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'+':([15,31,33,39,40,42,43,46,50,51,53,70,71,76,81,85,86,88,91,92,93,98,101,102,104,105,],[25,-32,-33,-27,-32,-33,-31,68,68,68,68,68,68,-35,68,-29,-30,68,-25,-26,68,-34,-28,-34,-32,68,]),'*':([31,33,39,40,42,43,76,85,86,91,92,98,102,104,],[-32,-33,62,-32,-33,-31,-35,-29,-30,62,62,-34,-34,-32,]),'-':([15,31,33,39,40,42,43,46,50,51,53,70,71,76,81,85,86,88,91,92,93,98,101,102,104,105,],[26,-32,-33,-27,-32,-33,-31,69,69,69,69,69,69,-35,69,-29,-30,69,-25,-26,69,-34,-28,-34,-32,69,]),',':([4,21,22,31,33,38,39,43,49,50,60,61,66,67,76,85,86,91,92,93,98,101,103,],[-47,-48,37,-32,-33,-47,-27,-31,73,-50,-49,37,90,-19,-35,-29,-30,-25,-26,-51,-34,-28,-20,]),'/':([31,33,39,40,42,43,76,85,86,91,92,98,102,104,],[-32,-33,63,-32,-33,-31,-35,-29,-30,63,63,-34,-34,-32,]),'=':([15,25,26,54,55,74,],[24,47,48,78,80,94,]),'<':([31,32,33,76,98,],[-32,55,-33,-35,-34,]),'$end':([0,1,4,5,6,8,9,10,11,12,13,14,17,18,21,22,31,33,39,40,42,43,45,46,59,60,70,71,72,76,85,86,89,91,92,98,101,102,104,105,107,109,110,],[-4,-1,-47,-6,-11,-8,0,-3,-7,-10,-12,-5,-9,-2,-48,-52,-32,-33,-27,-13,-15,-31,-17,-21,-36,-49,-22,-23,-46,-35,-29,-30,-18,-25,-26,-34,-28,-16,-14,-24,-38,-37,-45,]),'VARIABLE':([0,1,4,5,6,7,8,10,11,12,13,14,17,18,19,20,21,22,24,27,28,29,30,31,33,37,38,39,40,42,43,45,46,47,48,54,55,56,58,59,60,62,63,64,65,68,69,70,71,72,73,76,78,80,82,85,86,89,91,92,94,95,98,99,100,101,102,104,105,106,107,108,109,110,],[15,15,21,-6,-11,23,-8,-3,-7,-10,-12,-5,-9,-2,33,36,-48,-52,42,33,33,33,33,-32,-33,60,21,-27,-13,-15,-31,-17,-21,33,33,33,33,33,33,-36,-49,33,33,33,33,33,33,-22,-23,-46,33,-35,33,33,15,-29,-30,-18,-25,-26,33,15,-34,15,15,-28,-16,-14,-24,15,-38,15,-37,-45,]),'[':([15,24,33,42,],[28,44,56,65,]),']':([31,33,39,43,51,66,67,76,81,85,86,88,91,92,98,101,103,],[-32,-33,-27,-31,74,89,-19,-35,98,-29,-30,102,-25,-26,-34,-28,-20,]),'IF':([0,1,4,5,6,8,10,11,12,13,14,17,18,21,22,31,33,39,40,42,43,45,46,59,60,70,71,72,76,82,85,86,89,91,92,95,98,99,100,101,102,104,105,106,107,108,109,110,],[16,16,-47,-6,-11,-8,-3,-7,-10,-12,-5,-9,-2,-48,-52,-32,-33,-27,-13,-15,-31,-17,-21,-36,-49,-22,-23,-46,-35,16,-29,-30,-18,-25,-26,16,-34,16,16,-28,-16,-14,-24,16,-38,16,-37,-45,]),'AND':([31,33,35,76,77,79,96,97,98,],[-32,-33,58,-35,-41,-42,-44,-43,-34,]),'LEN':([24,27,28,30,47,48,56,65,73,94,],[41,41,41,41,41,41,41,41,41,41,]),'{':([57,75,84,],[82,95,100,]),'>':([31,32,33,76,98,],[-32,54,-33,-35,-34,]),'}':([4,5,6,8,10,11,12,13,14,17,18,21,22,31,33,39,40,42,43,45,46,59,60,70,71,72,76,82,85,86,89,91,92,95,98,99,100,101,102,104,105,106,107,108,109,110,],[-47,-6,-11,-8,-3,-7,-10,-12,-5,-9,-2,-48,-52,-32,-33,-27,-13,-15,-31,-17,-21,-36,-49,-22,-23,-46,-35,-4,-29,-30,-18,-25,-26,-4,-34,107,-4,-28,-16,-14,-24,109,-38,110,-37,-45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([0,1,82,95,99,100,106,108,],[12,12,12,12,12,12,12,12,]),'term':([24,27,28,30,47,48,56,65,68,69,73,94,],[39,39,39,39,39,39,39,39,91,92,39,39,]),'statements':([0,82,95,100,],[1,99,106,108,]),'numbers':([44,],[66,]),'assignment':([0,1,82,95,99,100,106,108,],[14,14,14,14,14,14,14,14,]),'variables':([4,38,],[22,61,]),'expressions':([27,],[49,]),'while':([0,1,82,95,99,100,106,108,],[17,17,17,17,17,17,17,17,]),'program':([0,],[9,]),'expression':([24,27,28,30,47,48,56,65,73,94,],[46,50,51,53,70,71,81,88,93,105,]),'statement':([0,1,82,95,99,100,106,108,],[10,18,10,10,18,10,18,18,]),'factor':([19,24,27,28,29,30,47,48,54,55,56,58,62,63,64,65,68,69,73,78,80,94,],[32,43,43,43,32,43,43,43,77,79,43,32,85,86,87,43,43,43,43,96,97,43,]),'print':([0,1,82,95,99,100,106,108,],[11,11,11,11,11,11,11,11,]),'return':([0,1,82,95,99,100,106,108,],[13,13,13,13,13,13,13,13,]),'operation':([0,1,82,95,99,100,106,108,],[5,5,5,5,5,5,5,5,]),'num_list':([24,],[45,]),'conditions':([19,],[34,]),'run_function':([0,1,82,95,99,100,106,108,],[6,6,6,6,6,6,6,6,]),'condition':([19,29,58,],[35,52,83,]),'if':([0,1,82,95,99,100,106,108,],[8,8,8,8,8,8,8,8,]),}

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
  ('statement -> <empty>','statement',0,'p_statement','py_yacc.py',37),
  ('statement -> assignment','statement',1,'p_statement','py_yacc.py',38),
  ('statement -> operation','statement',1,'p_statement','py_yacc.py',39),
  ('statement -> print','statement',1,'p_statement','py_yacc.py',40),
  ('statement -> if','statement',1,'p_statement','py_yacc.py',41),
  ('statement -> while','statement',1,'p_statement','py_yacc.py',42),
  ('statement -> function','statement',1,'p_statement','py_yacc.py',43),
  ('statement -> run_function','statement',1,'p_statement','py_yacc.py',44),
  ('statement -> return','statement',1,'p_statement','py_yacc.py',45),
  ('assignment -> VARIABLE = NUMBER','assignment',3,'p_assignment','py_yacc.py',55),
  ('assignment -> VARIABLE [ expression ] = NUMBER','assignment',6,'p_assignment','py_yacc.py',56),
  ('assignment -> VARIABLE = VARIABLE','assignment',3,'p_assignment','py_yacc.py',57),
  ('assignment -> VARIABLE = VARIABLE [ expression ]','assignment',6,'p_assignment','py_yacc.py',58),
  ('assignment -> VARIABLE = num_list','assignment',3,'p_assignment','py_yacc.py',59),
  ('num_list -> [ numbers ]','num_list',3,'p_num_list','py_yacc.py',93),
  ('numbers -> NUMBER','numbers',1,'p_numbers','py_yacc.py',100),
  ('numbers -> numbers , NUMBER','numbers',3,'p_numbers','py_yacc.py',101),
  ('operation -> VARIABLE = expression','operation',3,'p_operation','py_yacc.py',112),
  ('operation -> VARIABLE + = expression','operation',4,'p_operation','py_yacc.py',113),
  ('operation -> VARIABLE - = expression','operation',4,'p_operation','py_yacc.py',114),
  ('operation -> VARIABLE [ expression ] = expression','operation',6,'p_operation','py_yacc.py',115),
  ('expression -> expression + term','expression',3,'p_expression','py_yacc.py',135),
  ('expression -> expression - term','expression',3,'p_expression','py_yacc.py',136),
  ('expression -> term','expression',1,'p_expression','py_yacc.py',137),
  ('expression -> LEN ( factor )','expression',4,'p_expression','py_yacc.py',138),
  ('term -> term * factor','term',3,'p_term','py_yacc.py',154),
  ('term -> term / factor','term',3,'p_term','py_yacc.py',155),
  ('term -> factor','term',1,'p_term','py_yacc.py',156),
  ('factor -> NUMBER','factor',1,'p_factor','py_yacc.py',168),
  ('factor -> VARIABLE','factor',1,'p_factor','py_yacc.py',169),
  ('factor -> VARIABLE [ expression ]','factor',4,'p_factor','py_yacc.py',170),
  ('factor -> ( expression )','factor',3,'p_factor','py_yacc.py',171),
  ('print -> PRINT ( VARIABLE )','print',4,'p_print','py_yacc.py',189),
  ('if -> IF ( condition ) { statements }','if',7,'p_if','py_yacc.py',196),
  ('while -> WHILE ( conditions ) { statements }','while',7,'p_while','py_yacc.py',204),
  ('conditions -> condition','conditions',1,'p_conditions','py_yacc.py',212),
  ('conditions -> condition AND condition','conditions',3,'p_conditions','py_yacc.py',213),
  ('condition -> factor > factor','condition',3,'p_condition','py_yacc.py',224),
  ('condition -> factor < factor','condition',3,'p_condition','py_yacc.py',225),
  ('condition -> factor < = factor','condition',4,'p_condition','py_yacc.py',226),
  ('condition -> factor > = factor','condition',4,'p_condition','py_yacc.py',227),
  ('function -> DEF VARIABLE ( variables ) { statements }','function',8,'p_function','py_yacc.py',241),
  ('run_function -> VARIABLE ( expressions )','run_function',4,'p_run_function','py_yacc.py',250),
  ('variables -> <empty>','variables',0,'p_variables','py_yacc.py',258),
  ('variables -> VARIABLE','variables',1,'p_variables','py_yacc.py',259),
  ('variables -> variables , VARIABLE','variables',3,'p_variables','py_yacc.py',260),
  ('expressions -> expression','expressions',1,'p_expressions','py_yacc.py',274),
  ('expressions -> expressions , expression','expressions',3,'p_expressions','py_yacc.py',275),
  ('return -> RETURN variables','return',2,'p_return','py_yacc.py',286),
]