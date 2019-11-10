from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        SKUs = 'A B C'
        expected_price = 50 + 30 + 20
        assert checkout_solution.checkout(SKUs) == expected_price

    def test_illegal_input(self):
        SKUs = '1'
        expected_price = -1
        assert checkout_solution.checkout(SKUs)== expected_price
