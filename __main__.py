"""
    Created by Artem Shevchenko 24/06/2016
"""

import sys
from lexer.lexer import *

# Cheking for "-s" key existance
if sys.argv[1] == "-s":
# If exists, open third file stream for writing
    out_tokens = open("output.txt", "w")
# Stream for file with lexems
    lexer_file = open(sys.argv[2], "r")
# Stream for file with language code
    code_file = open(sys.argv[3], "r")
else:
# Open only two standard read streams
    lexer_file = open(sys.argv[1], "r")
    code_file = open(sys.argv[2], "r")


strings_lexeme = [l for l in lexer_file]
# List where we will save lexems
# in format {name: LEX_NAME, expr: EXPRASSION}
dict_lexeme = []

# Getting lexems from lexeme stream
for string in strings_lexeme:
    lexeme = string[:-1].split()
    dict_lexeme.append({'name': lexeme[0], 'expr': lexeme[1]})

# Creation of the Lexer specimen
lexer = Lexer([(l['expr'], l['name']) for l in dict_lexeme])

# Inputing source code from file
lexer.input(code_file.read())

# Getting and printing tokens
try:
    for one_token in lexer.return_tokens():
        if "-s" in sys.argv:
            # If exists "-s", print to file
            out_tokens.write(str(one_token) + "\n")
        else:
            # Print in terminal
            print(one_token)
except Error as err:
    # Return exeption if we don't have lexeme with
    # this exprassion
    print('Error at position %s' % err.pos)

# Closing writing file stream if exists "-s" ket
if "-s" in sys.argv:
    out_tokens.close()
    print "Saved to output.txt"

lexer_file.close()
code_file.close()
