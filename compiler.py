import subprocess
import sys
from lexer import lexer
from parser import parse
from generate import generate

# Main compiler logic
def compile_source(file_path):
    with open(file_path, 'r') as f:
        source_code = f.read()

    tokens = lexer(source_code)
    ast = parse(tokens)
    assembly = generate(ast)

    asm_file = file_path.replace('.c', '.s')
    exe_file = file_path.replace('.c', '')

    with open(asm_file, 'w') as f:
        f.write(assembly)

    subprocess.run(['gcc', asm_file, '-o', exe_file], check=True)
    print(f"Compiled {file_path} to {exe_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compiler.py <source.c>")
        sys.exit(1)

    compile_source(sys.argv[1])
