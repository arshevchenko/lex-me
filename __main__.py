import sys
from lexer.lexer import *

file_stream = open(sys.argv[1], "r")
lex_file = open(sys.argv[2], "r")

if "-s" in sys.argv:
    out_tokens = open("output.txt", "w")

strs = [l for l in file_stream]
lex = []
for el in strs:
    lexeme = el[:-1].split()
    lex.append({'name': lexeme[0], 'expr': lexeme[1]})

lexer = Lexer([(l['expr'], l['name']) for l in lex])
lexer.input(lex_file.read())

try:
    for tok in lexer.return_tokens():
        if "-s" in sys.argv:
            out_tokens.write(str(tok) + "\n")
        else:
            print(tok)
except LexerError as err:
    print('LexMeError at position %s' % err.pos)

if "-s" in sys.argv:
    out_tokens.close()
    print "Saved to output.txt"

file_stream.close()
lex_file.close()
