# Minimal C Compiler (Stage 1)

A compiler for a minimal subset of C. It reads a simple C program, lexes it into tokens, parses it into an AST, generates x86-64 assembly, and compiles it into an executable using GCC.

## Features (Stage 1)
- Supports `int main() { return <int>; }` only
- Lexing (tokenizing)
- Parsing into an abstact syntax tree (AST)
- Code generation (x86-64)
- Assembly to executable via `gcc`

---
## Clone Repository
```bash
git clone -b lex-parse-generate --single-branch https://github.com/Fnuworsu/compilers.git
```

## Usage

### How C file (main.c) looks

```c
// main.c
int main() {
    return 42;
}
```

### Run the compiler
```bash
python3 compiler.py main.c
```
### Run the executable
```bash
./main
echo $? # should printt out 42
```
