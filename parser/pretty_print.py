def pretty_print(ast):
    """Pretty print the AST."""
    fun_decl = ast.fun_decl
    print(f"FUN INT {fun_decl.name}:")
    print(f"    params: ()")
    print(f"    body:")
    print(f"        RETURN Int<{fun_decl.statement.exp.value}>")
