# ABM-Compiler-Python

What is ABM language?
Abstract Machine Language.

The grammar of ABM programming language: 

1. Stack Manipulation
- "push c"      Pushes c onto the stack
- "rvalue l"    Pushes contents of data location l onto the stack
- "lvalue l"    Pushes address of data location l onto the stack
- "pop"         Throws away value on top of the stack
- ":="          Stack top is placed by the lvalue below it and both are popped 
- "copy"        Pushes a copy of the top value on stack

2. Control Flow
- "label l"     Targets of jumps to l
- "goto l"      Next instruction is taken from statement with label l
- "gofalse l"   Pops the top value of the stack and jumps if it is zero
- "gotrue l"    Pops the top value of the stack and jumps if if is nonzero
- "halt"        Stops execution

3. Arithmetic Operators
- "+"           Adds top two values on stack and places result on stack
- "−"           Similar to +, but subtraction is performed
- "∗"           Similar to +, but multiplication is performed
- "/"           Similar to +, but integer division is performed
- "div"         Similar to +, but remainder of division is performed

4. Logical Operators
- "&"           Logial AND the top two values on stack and places result on stack
- "!"           Negates the top of the stack
- "|"           Similar to &, but logical OR is performed

5. Relational Operators
- "<>"          Returns 0 if top two values on stack are equal otherwise returns 1
- "<="          Similar to <>, but tests if top minus one is less or equal top
- ">="          Similar to <>, but tests if top minus one is greater or equal top
- "<"           Similar to <=, but tests if top minus one is less than top
- ">"           Similar to >=, but tests if top minus one is greater than top
- "="           Similar to <>, but tests if top minus one is equal to top of stack

6. Output
- "print"       Writes top of the stack contents to output device
- "show"        Writes a literal string to output device

7. Subprogram Control
- "begin"       Marks the beginning of parameter passing and subroutine call
- "end"         Marks the end of parameter passing and subroutine call
- "return"      Returns from subroutine
- "call"        Subroutine call

This Python Code is ABM language compiler.
Input data : ABM code.
Output data : ABM running result.
