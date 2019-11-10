from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_no_offers(self):
        SKUs = 'D C'
        expected_price = 15 + 20
        assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_with_offers(self):
        SKUs = 'A A A'
        expected_price = 130
        assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_one_offer_two_regular_priced(self):
        SKUs = 'A A A D C'
        expected_price = 130 + 15 + 20
        assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_one_offer_same_item_not_on_offer(self):
            SKUs = 'A A A A'
            expected_price = 130 + 50
            assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_two_offers(self):
            SKUs = 'A A A B B'
            expected_price = 130 + 45
            assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_no_active_offers(self):
            SKUs = 'A B C D'
            expected_price = 50 + 30 + 20 + 15
            assert checkout_solution.checkout(SKUs) == expected_price

    def test_illegal_input(self):
        SKUs = '1'
        expected_price = -1
        assert checkout_solution.checkout(SKUs)== expected_price