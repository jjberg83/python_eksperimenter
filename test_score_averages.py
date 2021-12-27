#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 10:47:37 2021

@author: jjberg
"""

def snitt_karakter():
    antall_studenter = int(input('Hvor mange studenter er det snakk om? '))
    antall_tester = int(input('Antall prøver per student? '))
    snitt_per_student = list()
    for student in range(antall_studenter):
        karakterer = list()
        for karakter in range(antall_tester):
            denne_karakteren = float(input(f'Hvilken karakter fikk student nummer {student + 1} på prøve nummer {karakter+1}? '))
            karakterer.append(denne_karakteren)
        snitt_for_denne_studenten = sum(karakterer)/antall_tester
        print(f'Snittet for student nr {student+1} er {snitt_for_denne_studenten}')
        snitt_per_student.append(snitt_for_denne_studenten)
    print()
    print(f'Og totalt snitt for {antall_studenter} studenter med {antall_tester} prøver hver, er: {sum(snitt_per_student)/antall_studenter}')
    
snitt_karakter()
