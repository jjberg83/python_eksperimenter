#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 10:59:32 2021

@author: jjberg
"""

print('This program displays a list of numbers')
print('(starting at 1) and their squares.')
end = int(input('How high should I go? '))
print()
print('Number\tSquare')
print('---------------')

for tall in range(1, end +1):
    square = tall ** 2
    print(f'{tall}\t\t{square}')