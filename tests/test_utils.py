from typing import NoReturn
import unittest

import sys
sys.path.append("..")

from internal import utils

class TestGetDefaultDate(unittest.TestCase):
    
    def test_get_default_date(self):
        self.assertEqual(utils.get_default_date(), ('2021', '08')) 


class TestConvertDate(unittest.TestCase):

    def setUp(self):
        self.payload = [
            ('2021', '08'),
            ('2020', '01'),
            ('2021', '12')
        ]
        self.expected = [
            ('2021', '07'),
            ('2019', '12'),
            ('2021', '11')
        ]
    
    def test_convert_date(self):
        for i in range(len(self.payload)):
            self.assertEqual(utils.convert_date(self.payload[i][0], self.payload[i][1]), 
                                                (self.expected[i][0], self.expected[i][1])) 


class TestGetMonth(unittest.TestCase):

    def setUp(self):
        self.payload = [1, 13, 0, 8, 'abc']
        self.expected = ['january', None, None, 'august', None]

    def test_get_month(self):
        for i in range(len(self.payload)):
            self.assertEqual(utils.get_month(self.payload[i]), self.expected[i])
