# Assembly code generator
def generate(ast):
    lines = [
        f".globl _{ast.fun_decl.name}",
        f"_{ast.fun_decl.name}:",
        f"    movl    ${ast.fun_decl.statement.exp.value}, %eax",
        "    ret"
    ]
    return '\n'.join(lines)