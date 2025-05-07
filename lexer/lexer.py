import re

# Token specification: token type + regex pattern
TOKEN_SPEC = [
    ('KEYWORD',    r'\bint\b|\breturn\b'),
    ('INTEGER',    r'\d+'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('SYMBOL',     r'[(){};]'), 
    ('WHITESPACE', r'[ \t\n]+')
]

token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)
get_token = re.compile(token_regex).match

def lexer(file):
    with open(file, "r") as f:
        code = f.read()
    
    tokens = []
    pos = 0
    line = 1

    while pos < len(code):
        match = get_token(code, pos)

        if not match:
            raise SyntaxError(f"Unexpected character: {code[pos]!r} at line {line}")
        
        kind = match.lastgroup
        value = match.group(kind)

        if kind == "WHITESPACE":
            line += value.count("\n")
        else:
            tokens.append((kind, value))
        
        pos = match.end()
    
    return tokens
get_token = re.compile(token_regex).match

def lexer(file):
    with open(file, "r") as f:
        code = f.read()
    
    tokens = []
    pos = 0
    line = 1

    while pos < len(code):
        match = get_token(code, pos)

        if not match:
            raise SyntaxError(f"Unexpected character: {code[pos]!r} at line {line}")
        
        kind = match.lastgroup
        value = match.group(kind)

        if kind == "WHITESPACE":
            line += value.count("\n")
        else:
            tokens.append((kind, value))
        
        pos = match.end()
    
    return tokens