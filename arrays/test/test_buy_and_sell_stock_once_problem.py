from unittest import TestCase
from arrays.buy_and_sell_stock_once_problem import buy_and_sell_stock_once_solution

class Test(TestCase):
    def test_buy_and_sell_stock_solution(self):
        self.assertTrue(buy_and_sell_stock_once_solution([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30)

