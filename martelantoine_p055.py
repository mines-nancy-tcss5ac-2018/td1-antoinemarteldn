# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:04:07 2018

@author: martel31u
"""

def solve(n):
    "détermine le nombre de nombres de Lychrel en dessous de n"
    res=0
    for k in range(n):
        nb=k
        i=0
        while i<50:
            nb+=(rev(nb))
            if rev(nb)==nb:
                i=50
            else: 
                i+=1
                if i==50:
                    res+=1
    return res
            
def rev(n):
    "inverse l'ordre des chiffres d'un nombre"
    n=str(n)
    rev=""
    for i in range(len(n)):
        rev+=n[-i-1]
    rev=int(rev)
    return rev

assert solve(196)==0
assert solve(197)==1
print(solve(10000))