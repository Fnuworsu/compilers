from collections import namedtuple
from generate import generate
from pretty_print import pretty_print

# AST node types using namedtuple
Exp = namedtuple('Exp', ['value'])
Return = namedtuple('Return', ['exp'])
FunDecl = namedtuple('FunDecl', ['name', 'statement'])
Program = namedtuple('Program', ['fun_decl'])

# token types
KEYWORD, IDENTIFIER, INTEGER, OPEN_BRACE, CLOSE_BRACE, OPEN_PAREN, CLOSE_PAREN, SEMICOLON = (
    'KEYWORD', 'IDENTIFIER', 'INTEGER', '{', '}', '(', ')', ';'
)

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            val = self.tokens[self.pos][1]
            self.pos += 1
            return val
        raise ParserError(f"Expected token type {expected_type} but found {self.tokens[self.pos]}")

    def parse_exp(self):
        val = int(self.consume(INTEGER))
        return Exp(val)

    def parse_statement(self):
        # return
        self.consume(KEYWORD) 
        exp = self.parse_exp()
        self.consume(SEMICOLON)
        return Return(exp)

    def parse_fun_decl(self):
        # int
        self.consume(KEYWORD)  
        name = self.consume(IDENTIFIER)
        self.consume(OPEN_PAREN)
        self.consume(CLOSE_PAREN)
        self.consume(OPEN_BRACE)
        statement = self.parse_statement()
        self.consume(CLOSE_BRACE)
        return FunDecl(name, statement)

    def parse_program(self):
        fun_decl = self.parse_fun_decl()
        return Program(fun_decl)

def parse(tokens):
    parser = Parser(tokens)
    ast = parser.parse_program()
    if parser.pos != len(tokens):
        raise ParserError("Extra tokens found after parsing complete")
    return ast

if __name__ == "__main__":
    tokens = [
    ('KEYWORD', 'int'), ('IDENTIFIER', 'main'), ('(', '('), (')', ')'),
    ('{', '{'), ('KEYWORD', 'return'), ('INTEGER', '42'), (';', ';'), ('}', '}')
    ]

    ast = parse(tokens)
    pretty_print(ast)
    assembly = generate(ast)
    print("\nGenerated Assembly:\n")
    print(assembly)
