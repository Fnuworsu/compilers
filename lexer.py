from parser import ParserError
import re

"""Lexer implementation"""
def lexer(source):
    token_specification = [
        ('KEYWORD', r'\b(int|return)\b'),
        ('INTEGER', r'\b\d+\b'),
        ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),
        ('OPEN_BRACE', r'\{'),
        ('CLOSE_BRACE', r'\}'),
        ('OPEN_PAREN', r'\('),
        ('CLOSE_PAREN', r'\)'),
        ('SEMICOLON', r';'),
        ('SKIP', r'[ \t\n]+'),
        ('MISMATCH', r'.'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    tokens = []
    for mo in re.finditer(tok_regex, source):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise ParserError(f'Unexpected token: {value}')
        tokens.append((kind, value))
    return tokens