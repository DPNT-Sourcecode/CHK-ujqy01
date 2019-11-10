from solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        name = 'John'
        assert hello_solution.hello(name)=='Hello, {}!'.format(name)