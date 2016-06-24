import sys
from lexer.lexer import *

if sys.argv[1] == "-s":
    out_tokens = open("output.txt", "w")
    lexer_file = open(sys.argv[2], "r")
    code_file = open(sys.argv[3], "r")
else:
    lexer_file = open(sys.argv[1], "r")
    code_file = open(sys.argv[2], "r")


strings_lexeme = [l for l in lexer_file]
dict_lexeme = []
for string in strings_lexeme:
    lexeme = string[:-1].split()
    dict_lexeme.append({'name': lexeme[0], 'expr': lexeme[1]})

lexer = Lexer([(l['expr'], l['name']) for l in dict_lexeme])
lexer.input(code_file.read())

try:
    for one_token in lexer.return_tokens():
        if "-s" in sys.argv:
            out_tokens.write(str(one_token) + "\n")
        else:
            print(one_token)
except Error as err:
    print('Error at position %s' % err.pos)

if "-s" in sys.argv:
    out_tokens.close()
    print "Saved to output.txt"

lexer_file.close()
code_file.close()
