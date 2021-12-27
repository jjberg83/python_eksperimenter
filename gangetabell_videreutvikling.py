#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 07:08:34 2021

@author: jjberg
"""

grense = int(input('Hvor langt opp skal gangetabellen gå? '))
print()

for header in range(grense+1):
    if header == 0:
        print(end='\t')
    else:
        print(header, end='\t')

print()
strek = '-----'
print(strek*grense)

for ytre in range(1, grense+1):
    print(ytre, '| ', end='\t')
    for indre in range(1, grense+1):
        print(ytre * indre, end='\t')
    print()