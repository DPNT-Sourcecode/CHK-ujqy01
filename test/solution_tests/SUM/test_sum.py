from solutions.SUM import sum_solution



class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_parameter_out_of_bounds(self):
       self.assertRaises(InputError,sum_solution.compute(101, 2))

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

