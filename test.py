# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import unittest
import kalkulator

class Testy(unittest.TestCase):
    
    def test_typ_danych(self):
        #given
        a = 5
        b = 10
        znak = "+"
        expected_type=int
        #when
        result=kalkulator.kalk(a,b,znak)
        #then
        self.assertEqual(type(result),expected_type)

    def test_dodawanie(self):
        #given
        a=6
        b=3
        expected=9
        #when
        result=kalkulator.kalk(a,b,'+')
        #then
        self.assertEqual(result,expected)
    
    def test_mnozenie(self):
        #given
        a=6
        b=3
        expected=18
        #when
        result=kalkulator.kalk(a,b,'*')
        #then
        self.assertEqual(result,expected)
    
    def test_odejmowanie(self):
        #given
        a=6
        b=3
        expected=3
        #when
        result=kalkulator.kalk(a,b,'-')
        #then
        self.assertEqual(result,expected)
    
    def test_dzielenie(self):
        #given
        a=6
        b=3
        expected=2
        #when
        result=kalkulator.kalk(a,b,'/')
        #then
        self.assertEqual(result,expected)
    
if __name__ == '__main__':
    unittest.main()
    