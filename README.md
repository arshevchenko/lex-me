# Lex-me
Lex-analyzer based on Python 2.7


## Installation
Clone this repository to your local folder. Remember, you need Python 2.7 for launching this package.

    git clone https://github.com/shev2dev/lex-me.git




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


----------


### Launching
After them, write in terminal:

    python lex-me path/to/lex_file path/to/code_file

By default, it prints result in terminal, but if you add key "-s" the result of work will be saved in output.txt (with folder package):

    python lex-me -s path/to/lex_file path/to/code_file

----------

### Result
As result you will get lines of tokens like this :
`<TOKEN_NAME, TEXT, POSITION_START, POSITION_END>`

Result of example launching:

    <IF, if, 0, 1>
    <WHITE,  , 2, 2>
    <ID, num, 3, 5>
    <WHITE,  , 6, 6>
    <EQUAL, =, 7, 7>
    <WHITE,  , 8, 8>
    <NUMBER, 0, 9, 9>
    <WHITE,  , 10, 10>
    <THEN, then, 11, 14>
    <WHITE,  , 15, 15>
    <NUMBER, 1, 16, 16>
    <WHITE,  , 17, 17>
    <ELSE, else, 18, 21>
    <WHITE,  , 22, 22>
    <ID, num, 23, 25>
    <WHITE,  , 26, 26>
    <MULT, *, 27, 27>
    <WHITE,  , 28, 28>
    <ID, factorial, 29, 37>
    <LPAR, (, 38, 38>
    <ID, num, 39, 41>
    <WHITE,  , 42, 42>
    <MINUS, -, 43, 43>
    <WHITE,  , 44, 44>
    <NUMBER, 1, 45, 45>
    <RPAR, ), 46, 46>
    <WHITE,  , 47, 47>
    <FI, fi, 48, 49>
    <WHITE, \n, 50, 50>

## Dependecies
- Python 2.7
