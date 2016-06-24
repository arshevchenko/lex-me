from tokenizer import *
from err import *
import re

class Lexer(object):
    def __init__(self, rules):
        self.rules = []
        for expression, name in rules:
            self.rules.append((re.compile(expression), name))

    def input(self, input_string):
        self.position = 0
        self.input_string = input_string

    def return_tokens(self):
        while 1:
            token_result = self.token()
            if token_result is None: break
            yield token_result

    def token(self):
        if self.position >= len(self.input_string):
            return None

        for regex, type in self.rules:
            reg_result = regex.match(self.input_string, self.position)
            if reg_result:
                token_string = Token(type, reg_result.group(), self.position, reg_result.end())
                self.position = reg_result.end()
                return token_string

        raise LexerError(self.position)
