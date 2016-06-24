from tokenizer import *
from err import *
import re

class Lexer(object):
    def __init__(self, rules):
        self.rules = []
        for regex, type in rules:
            self.rules.append((re.compile(regex), type))

    def input(self, buf):
        self.buf = buf
        self.pos = 0

    def token(self):
        if self.pos >= len(self.buf):
            return None

        for regex, type in self.rules:
            m = regex.match(self.buf, self.pos)
            if m:
                tok = Token(type, m.group(), self.pos, m.end())
                self.pos = m.end()
                return tok

        raise LexerError(self.pos)

    def tokens(self):
        while 1:
            tok = self.token()
            if tok is None: break
            yield tok
