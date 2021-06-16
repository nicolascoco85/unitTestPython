#!/usr/bin/env python
# -*- coding: utf-8 -*-
def sum(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a + b

def esGenerala(lista):
    valor = lista[0]
    indice = 0
    while valor == lista[indice] and indice < len(lista)-1:
        indice = indice +1

    if valor == lista[indice]:
        return True
    else:
        return False


def esPoker(lista):

    for i in range (1,7):
        if (lista.count(i)==4):
            return True
    return False

