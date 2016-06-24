"""
    Created by Artem Shevchenko 24/06/2016
"""

from tokenizer import *
from err import *
import re

class Lexer(object):
    def __init__(self, rules):
        self.rules = []
        for expression, name in rules:
            # Compiling of regular exprassions
            # and adding them to the local
            # rule list
            self.rules.append((re.compile(expression), name))

    # This method set the start position
    # and string for analyzing
    def input(self, input_string):
        self.position = 0
        self.input_string = input_string

    # This method generates list of tokens
    def return_tokens(self):
        token_result = True
        while token_result:
            token_result = self.token()
            if not token_result: break
            yield token_result

    # This method return token
    def token(self):
        # Exit from analyzing, when position
        # greater the string length
        if self.position >= len(self.input_string):
            return False

        # Starting of searching lexeme
        for regex, type in self.rules:
            # Matching substring with rule
            reg_result = regex.match(self.input_string, self.position)

            # If rule find
            if reg_result:
                # Saving token
                token_string = Token(type, reg_result.group(), self.position, reg_result.end())
                # Saving last position
                self.position = reg_result.end()

                # return result of matching
                return token_string
        # If rule not found, raise error
        raise Error(self.position)
