from collections import namedtuple

# Define AST node types
Exp = namedtuple('Exp', ['value'])
Return = namedtuple('Return', ['exp'])
FunDecl = namedtuple('FunDecl', ['name', 'statement'])
Program = namedtuple('Program', ['fun_decl'])
