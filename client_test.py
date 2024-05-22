import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']),
                                                   float(quote['top_ask']['price']),
                                                   (float(quote['top_bid']['price']) + float(
                                                       quote['top_ask']['price'])) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']),
                                                   float(quote['top_ask']['price']),
                                                   (float(quote['top_bid']['price']) + float(
                                                       quote['top_ask']['price'])) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_calculateRatio(self):
        prices = [
            {'a': 120, 'b': 190},
            {'a': 2, 'b': 1}
        ]

        for price in prices:
            self.assertEqual(getRatio(price['a'], price['b']), price['a'] / price['b'])

    def test_getRatio_price0(self):
        prices = [
            {'a': 0, 'b': 10},
            {'a': 2, 'b': 0}
        ]

        for price in prices:
            self.assertEqual(getRatio(price['a'], price['b']), 0)


if __name__ == '__main__':
    unittest.main()
