# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def solve(n):
    "retourne la somme des chiffres de 2^n"
    n=pow(2,n)
    n=str(n)
    res=0
    for k in n:
        res+=int(k)
    return res

assert solve(15) == 26
print(solve(1000))