# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 07:35:32 2024
created for sdev 220 fall 2024

@author: s.s.salama
"""
# testing code
def add_numbers(a, b):
    return a + b
import unittest

# Writing Your First Test
class TestMathOperations(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)
        
        # excecuting
        if __name__ == "__main__":
             unittest.main()