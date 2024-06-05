
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLASS CLASS DOT EQUALS IDENTIFIER LBRACE LBRACKET LPAREN MAIN MAIN NUMBER OUT OUT PLUS PRINTLN PRINTLN PUBLIC PUBLIC RBRACE RBRACKET RPAREN SEMICOLON STATIC STATIC STRING SYSTEM SYSTEM VOID VOIDprogram : class_declclass_decl : PUBLIC CLASS IDENTIFIER LBRACE method_decl RBRACEmethod_decl : PUBLIC STATIC VOID MAIN LPAREN parameter RPAREN LBRACE statements RBRACEparameter : IDENTIFIER LBRACKET RBRACKET IDENTIFIERstatements : statement\n                  | statement statementsstatement : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING RPAREN SEMICOLON\n                 | IDENTIFIER EQUALS expression SEMICOLON\n                 | IDENTIFIER SEMICOLONexpression : term\n                  | term PLUS termterm : IDENTIFIER\n            | NUMBER\n            | STRING'
    
_lr_action_items = {'PUBLIC':([0,6,],[3,7,]),'$end':([1,2,10,],[0,-1,-2,]),'CLASS':([3,],[4,]),'IDENTIFIER':([4,13,18,19,21,28,29,37,38,44,],[5,15,23,24,23,31,-9,-8,31,-7,]),'LBRACE':([5,16,],[6,18,]),'STATIC':([7,],[9,]),'RBRACE':([8,20,21,25,26,29,37,44,],[10,25,-5,-3,-6,-9,-8,-7,]),'VOID':([9,],[11,]),'MAIN':([11,],[12,]),'LPAREN':([12,39,],[13,41,]),'RPAREN':([14,24,42,],[16,-4,43,]),'LBRACKET':([15,],[17,]),'RBRACKET':([17,],[19,]),'SYSTEM':([18,21,29,37,44,],[22,22,-9,-8,-7,]),'DOT':([22,30,],[27,36,]),'EQUALS':([23,],[28,]),'SEMICOLON':([23,31,32,33,34,35,40,43,],[29,-12,37,-10,-13,-14,-11,44,]),'OUT':([27,],[30,]),'NUMBER':([28,38,],[34,34,]),'STRING':([28,38,41,],[35,35,42,]),'PLUS':([31,33,34,35,],[-12,38,-13,-14,]),'PRINTLN':([36,],[39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'class_decl':([0,],[2,]),'method_decl':([6,],[8,]),'parameter':([13,],[14,]),'statements':([18,21,],[20,26,]),'statement':([18,21,],[21,21,]),'expression':([28,],[32,]),'term':([28,38,],[33,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> class_decl','program',1,'p_program','app.py',65),
  ('class_decl -> PUBLIC CLASS IDENTIFIER LBRACE method_decl RBRACE','class_decl',6,'p_class_decl','app.py',69),
  ('method_decl -> PUBLIC STATIC VOID MAIN LPAREN parameter RPAREN LBRACE statements RBRACE','method_decl',10,'p_method_decl','app.py',73),
  ('parameter -> IDENTIFIER LBRACKET RBRACKET IDENTIFIER','parameter',4,'p_parameter','app.py',77),
  ('statements -> statement','statements',1,'p_statements','app.py',81),
  ('statements -> statement statements','statements',2,'p_statements','app.py',82),
  ('statement -> SYSTEM DOT OUT DOT PRINTLN LPAREN STRING RPAREN SEMICOLON','statement',9,'p_statement','app.py',86),
  ('statement -> IDENTIFIER EQUALS expression SEMICOLON','statement',4,'p_statement','app.py',87),
  ('statement -> IDENTIFIER SEMICOLON','statement',2,'p_statement','app.py',88),
  ('expression -> term','expression',1,'p_expression','app.py',92),
  ('expression -> term PLUS term','expression',3,'p_expression','app.py',93),
  ('term -> IDENTIFIER','term',1,'p_term','app.py',97),
  ('term -> NUMBER','term',1,'p_term','app.py',98),
  ('term -> STRING','term',1,'p_term','app.py',99),
]