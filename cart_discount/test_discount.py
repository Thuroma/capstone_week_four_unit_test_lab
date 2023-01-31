import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario
    def test_list_of_two_prices(self):
        prices = [3, 20]
        self.assertIsNone(discount(prices))


    

    # TODO test for NameError if something BUT a list is passed to discount
   


    # test if the returned price is negative
    def test_lowest_price_is_greater_than_zero(self):
        prices = [2, 4, 6]
        self.assertGreater(discount(prices), 0)



if __name__ == '__main__':
    unittest.main()