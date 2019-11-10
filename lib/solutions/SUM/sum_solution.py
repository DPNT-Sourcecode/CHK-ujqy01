# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x<0 or x > 100 or y<0 or y>100:
        raise InputError
    return x+y
    # raise NotImplementedError()


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = 'Input parameter(s) out of bounds'


