from ast_node import Exp, Return, FunDecl, Program
from tokens import KEYWORD, IDENTIFIER, INTEGER, OPEN_BRACE, CLOSE_BRACE, OPEN_PAREN, CLOSE_PAREN, SEMICOLON

class ParserError(Exception):
    pass

# Parser implementation
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            val = self.tokens[self.pos][1]
            self.pos += 1
            return val
        raise ParserError(f"Expected {expected_type}, found {self.tokens[self.pos]}")

    def parse_exp(self):
        val = int(self.consume(INTEGER))
        return Exp(val)

    def parse_statement(self):
        self.consume(KEYWORD)  # 'return'
        exp = self.parse_exp()
        self.consume(SEMICOLON)
        return Return(exp)

    def parse_fun_decl(self):
        self.consume(KEYWORD)  # 'int'
        name = self.consume(IDENTIFIER)
        self.consume(OPEN_PAREN)
        self.consume(CLOSE_PAREN)
        self.consume(OPEN_BRACE)
        stmt = self.parse_statement()
        self.consume(CLOSE_BRACE)
        return FunDecl(name, stmt)

    def parse_program(self):
        fun_decl = self.parse_fun_decl()
        return Program(fun_decl)

def parse(tokens):
    parser = Parser(tokens)
    ast = parser.parse_program()
    if parser.pos != len(tokens):
        raise ParserError("Extra tokens after parsing")
    return ast
