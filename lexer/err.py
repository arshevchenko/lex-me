"""
    Created by Artem Shevchenko 24/06/2016
"""

__all__ = ["Error"]
class Error(Exception):
    def __init__(self, position):
        # Exeption will return error position
        self.posistion = position
