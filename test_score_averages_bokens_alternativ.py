#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 10:47:37 2021

@author: jjberg
"""

def snitt_karakter():
    antall_studenter = int(input('Hvor mange studenter er det snakk om? '))
    antall_tester = int(input('Antall prøver per student? '))
    for student in range(antall_studenter):
        karakter_sum = 0.0
        print(f'Student nummer {student + 1}')
        print('--------------------')
        for karakter in range(antall_tester):
            print(f'Test nummer {karakter+1}', end='')
            denne_karakteren = float(input(': '))
            karakter_sum += denne_karakteren
        print(f'Snittet for student nummer {student+1} er: {karakter_sum/antall_tester}')
            
            
            
    
    
snitt_karakter()
