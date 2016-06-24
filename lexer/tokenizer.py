class Token(object):
    def __init__(self, type, val, pos_s, pos_e):
        self.type = type
        self.val = val.encode('string-escape')
        self.pos_s = pos_s
        self.pos_e = pos_e

    def __str__(self):
        return '<%s, %s, %s, %s>' % (self.type, self.val, self.pos_s, self.pos_e)
