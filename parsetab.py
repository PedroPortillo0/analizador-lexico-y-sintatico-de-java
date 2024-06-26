
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLASS CLASS COMMA DOT EQUALS IDENTIFIER LBRACE LPAREN MAIN MAIN NUMBER OUT OUT PLUS PRINTLN PRINTLN PUBLIC PUBLIC RBRACE RETURN RETURN RPAREN SEMICOLON STATIC STATIC STRING SYSTEM SYSTEM VOID VOIDprogram : class_declclass_decl : PUBLIC CLASS IDENTIFIER LBRACE method_decls RBRACEmethod_decls : method_decl\n                    | method_decl method_decls\n                    | emptymethod_decl : PUBLIC STATIC type IDENTIFIER LPAREN params RPAREN LBRACE statements RBRACEtype : VOID\n            | IDENTIFIERparams : param\n              | param COMMA params\n              | emptyparam : type IDENTIFIERstatements : statement\n                  | statement statementsstatement : SYSTEM DOT OUT DOT PRINTLN LPAREN expression RPAREN SEMICOLON\n                 | type IDENTIFIER EQUALS expression SEMICOLON\n                 | IDENTIFIER EQUALS expression SEMICOLON\n                 | RETURN expression SEMICOLONexpression : term\n                  | expression PLUS termterm : IDENTIFIER\n            | NUMBER\n            | STRINGempty :'
    
_lr_action_items = {'PUBLIC':([0,6,9,36,],[3,7,7,-6,]),'$end':([1,2,12,],[0,-1,-2,]),'CLASS':([3,],[4,]),'IDENTIFIER':([4,11,14,15,16,18,19,25,26,28,29,31,33,35,44,47,48,50,53,55,58,],[5,15,17,-8,-7,15,23,15,29,34,-8,29,41,41,41,-18,41,-17,-16,41,-15,]),'LBRACE':([5,24,],[6,26,]),'RBRACE':([6,8,9,10,13,30,31,36,37,47,50,53,58,],[-24,12,-3,-5,-4,36,-13,-6,-14,-18,-17,-16,-15,]),'STATIC':([7,],[11,]),'VOID':([11,18,25,26,31,47,50,53,58,],[16,16,16,16,16,-18,-17,-16,-15,]),'LPAREN':([17,54,],[18,55,]),'RPAREN':([18,20,21,22,23,25,27,40,41,42,43,52,56,],[-24,24,-9,-11,-12,-24,-10,-19,-21,-22,-23,-20,57,]),'COMMA':([21,23,],[25,-12,]),'SYSTEM':([26,31,47,50,53,58,],[32,32,-18,-17,-16,-15,]),'RETURN':([26,31,47,50,53,58,],[33,33,-18,-17,-16,-15,]),'EQUALS':([29,34,],[35,44,]),'DOT':([32,46,],[38,51,]),'NUMBER':([33,35,44,48,55,],[42,42,42,42,42,]),'STRING':([33,35,44,48,55,],[43,43,43,43,43,]),'OUT':([38,],[46,]),'SEMICOLON':([39,40,41,42,43,45,49,52,57,],[47,-19,-21,-22,-23,50,53,-20,58,]),'PLUS':([39,40,41,42,43,45,49,52,56,],[48,-19,-21,-22,-23,48,48,-20,48,]),'PRINTLN':([51,],[54,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'class_decl':([0,],[2,]),'method_decls':([6,9,],[8,13,]),'method_decl':([6,9,],[9,9,]),'empty':([6,9,18,25,],[10,10,22,22,]),'type':([11,18,25,26,31,],[14,19,19,28,28,]),'params':([18,25,],[20,27,]),'param':([18,25,],[21,21,]),'statements':([26,31,],[30,37,]),'statement':([26,31,],[31,31,]),'expression':([33,35,44,55,],[39,45,49,56,]),'term':([33,35,44,48,55,],[40,40,40,52,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> class_decl','program',1,'p_program','app.py',67),
  ('class_decl -> PUBLIC CLASS IDENTIFIER LBRACE method_decls RBRACE','class_decl',6,'p_class_decl','app.py',71),
  ('method_decls -> method_decl','method_decls',1,'p_method_decls','app.py',75),
  ('method_decls -> method_decl method_decls','method_decls',2,'p_method_decls','app.py',76),
  ('method_decls -> empty','method_decls',1,'p_method_decls','app.py',77),
  ('method_decl -> PUBLIC STATIC type IDENTIFIER LPAREN params RPAREN LBRACE statements RBRACE','method_decl',10,'p_method_decl','app.py',81),
  ('type -> VOID','type',1,'p_type','app.py',85),
  ('type -> IDENTIFIER','type',1,'p_type','app.py',86),
  ('params -> param','params',1,'p_params','app.py',90),
  ('params -> param COMMA params','params',3,'p_params','app.py',91),
  ('params -> empty','params',1,'p_params','app.py',92),
  ('param -> type IDENTIFIER','param',2,'p_param','app.py',96),
  ('statements -> statement','statements',1,'p_statements','app.py',100),
  ('statements -> statement statements','statements',2,'p_statements','app.py',101),
  ('statement -> SYSTEM DOT OUT DOT PRINTLN LPAREN expression RPAREN SEMICOLON','statement',9,'p_statement','app.py',105),
  ('statement -> type IDENTIFIER EQUALS expression SEMICOLON','statement',5,'p_statement','app.py',106),
  ('statement -> IDENTIFIER EQUALS expression SEMICOLON','statement',4,'p_statement','app.py',107),
  ('statement -> RETURN expression SEMICOLON','statement',3,'p_statement','app.py',108),
  ('expression -> term','expression',1,'p_expression','app.py',120),
  ('expression -> expression PLUS term','expression',3,'p_expression','app.py',121),
  ('term -> IDENTIFIER','term',1,'p_term','app.py',134),
  ('term -> NUMBER','term',1,'p_term','app.py',135),
  ('term -> STRING','term',1,'p_term','app.py',136),
  ('empty -> <empty>','empty',0,'p_empty','app.py',147),
]
