from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_no_offers(self):
        SKUs = 'DC'
        expected_price = 15 + 20
        assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_with_offers(self):
        SKUs = 'AAA'
        expected_price = 130
        assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_one_offer_two_regular_priced(self):
        SKUs = 'AAADC'
        expected_price = 130 + 15 + 20
        assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_one_offer_same_item_not_on_offer(self):
            SKUs = 'AAAA'
            expected_price = 130 + 50
            assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_two_offers(self):
            SKUs = 'AAABB'
            expected_price = 130 + 45
            assert checkout_solution.checkout(SKUs) == expected_price

    def test_checkout_no_active_offers(self):
            SKUs = 'ABCD'
            expected_price = 50 + 30 + 20 + 15
            assert checkout_solution.checkout(SKUs) == expected_price

    def test_illegal_input(self):
        SKUs = '1'
        expected_price = -1
        assert checkout_solution.checkout(SKUs)== expected_price
