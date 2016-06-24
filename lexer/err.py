__all__ = ["Error"]
class Error(Exception):
    def __init__(self, position):
        self.posistion = position
