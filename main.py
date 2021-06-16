#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import mymodule


class TestMyModule(unittest.TestCase):

    def test_suma_5_mas_7_resultado_12(self):
        self.assertEqual(mymodule.sum(5, 7), 12)

    def test_suma_5_mas_7_resultado_no_es_13(self):
        self.assertNotEqual(mymodule.sum(5, 7), 13)

    def test_suma_0_mas_es_igual_a_0 (self):
        self.assertTrue(mymodule.sum(0,0)==0)

    def test_esGeneralaDe5(self):
        self.assertTrue(mymodule.esGenerala([5,5,5,5,5]) == True)

    def test_esGeneralaDe6(self):
        self.assertTrue(mymodule.esGenerala([6,6,6,6,6]) == True)

    def test_NoEsGenerala(self):
       self.assertFalse(mymodule.esGenerala([5, 5, 5, 5, 4]) == True)

    def test_esPoker_De_5(self):
        self.assertEqual(mymodule.esPoker([5, 5, 5, 5, 4]), True)

    def test_NoEsPokerDe6(self):
        self.assertTrue(mymodule.esPoker([6,6,6,6,6]) == False)

    def test_NoEsPokerDadoQueEsFull(self):
        self.assertTrue(mymodule.esPoker([6,5,5,5,6]) == False)

    def test_esGeneralaDe3(self):
        self.assertTrue(mymodule.esGenerala([3,3,3,3,3]) == True)



if __name__ == "__main__":
    unittest.main()
