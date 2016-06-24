# Lex-me
Lex-analyzer based on Python 2.7


----------
## Installation
Clone this repository to your local folder. Remember, you need Python 2.7 for launching this package.

    git clone https://github.com/shev2dev/lex-me.git


----------


## Usage

### Preparation
For creation of your own lexical analyzer just create a file with your lexeme definings. Save this as file:

    IF        [iI][fF]\b
    FI        [fF][iI]\b
    THEN      [tT][hH][eE][nN]\b
    ELSE      [eE][lL][sS][eE]\b
    STRING    \"(?:[^"\\]|\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4}))*\"
    NUMBER    -?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?
    ID        [\w_]+
    EQUAL     \=
    MULT      \*
    MINUS     \-
    LPAR      \(
    RPAR      \)
    WHITE     \s


Take this peace of code as code example file:

    if num = 0 then 1 else num * factorial(num - 1) fi

### Launching
After them, write in terminal:

    python lex-me path/to/lex_file path/to/code_file

By default, it prints result in terminal, but if you add key "-s" the result of work will be saved in output.txt:

    python lex-me path/to/lex_file path/to/code_file -s
### Result
As result you will get lines of tokens like this :
`<TOKEN_NAME, TEXT, POSITION_START, POSITION_END>`

Result of launching example:

    <IF, if, 0, 2>
    <WHITE,  , 2, 3>
    <ID, num, 3, 6>
    <WHITE,  , 6, 7>
    <EQUAL, =, 7, 8>
    <WHITE,  , 8, 9>
    <NUMBER, 0, 9, 10>
    <WHITE,  , 10, 11>
    <THEN, then, 11, 15>
    <WHITE,  , 15, 16>
    <NUMBER, 1, 16, 17>
    <WHITE,  , 17, 18>
    <ELSE, else, 18, 22>
    <WHITE,  , 22, 23>
    <ID, num, 23, 26>
    <WHITE,  , 26, 27>
    <MULT, *, 27, 28>
    <WHITE,  , 28, 29>
    <ID, factorial, 29, 38>
    <LPAR, (, 38, 39>
    <ID, num, 39, 42>
    <WHITE,  , 42, 43>
    <MINUS, -, 43, 44>
    <WHITE,  , 44, 45>
    <NUMBER, 1, 45, 46>
    <RPAR, ), 46, 47>
    <WHITE,  , 47, 48>
    <FI, fi, 48, 50>
    <WHITE, \n, 50, 51>


----------


## Dependecies
- Python 2.7
