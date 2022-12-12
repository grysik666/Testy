# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:30:14 2022

@author: szczesniakj
"""


def dodawanie(a, b):
    return a+b


def mnozenie(a, b):
    return a*b


def odejmowanie(a, b):
    return a-b


def dzielenie(a, b):
    return a/b


def kalk(a, b, znak):
    a = wpisz_liczbe()
    znak = wpisz_znak()
    b = wpisz_liczbe()
    if (znak == "+"):
        result = dodawanie(a, b)
    if (znak == "-"):
        result = odejmowanie(a, b)
    if (znak == "*"):
        result = mnozenie(a, b)
    if (znak == "/"):
        result = dzielenie(a, b)
    wypisz(result)
    return result


def wpisz_liczbe():
    a = int(input("Podaj liczbe:"))
    return a


def wpisz_znak():
    znak = input("Podaj znak:")
    return znak


def wypisz(x):
    print(x)
