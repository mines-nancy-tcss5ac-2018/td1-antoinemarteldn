# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:22:28 2018

@author: martel31u
"""

def solve(filename):
    """
    trie une liste de noms, calcule pour chaque nom un score lié à la valeur
    alphabétique de ses lettres multipliées par sa position dans la liste et
    somme le score de tous les noms
    """
    F=open(filename, 'r')
    d={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    namelist=str(F.read())
    namelist=namelist.split('","')
    namelist[0]=namelist[0][1:]
    namelist[-1]=namelist[-1][:-1] 
    namelist=sorted(namelist)
    res=0
    for k in range(len(namelist)): 
        score=0
        for l in namelist[k]:
            score+=d[l]
        score*=(k+1)
        res+=score
    return res


    
print(solve('p022_names.txt'))