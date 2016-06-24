__all__ = ["Error"]
class Error(Exception):
    def __init__(self, position):
        # Exeption will return error position
        self.posistion = position
