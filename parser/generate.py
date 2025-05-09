def generate(ast):
    """Generate assembly from AST."""
    lines = []
    fun_decl = ast.fun_decl
    lines.append(f".globl _{fun_decl.name}")
    lines.append(f"_{fun_decl.name}:")
    ret_stmt = fun_decl.statement
    lines.append(f"    movl    ${ret_stmt.exp.value}, %eax")
    lines.append("    ret")
    return '\n'.join(lines)
