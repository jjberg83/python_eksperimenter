#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 08:56:01 2021

@author: jjberg
"""

"""

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid

relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law."
"""

def relation_to_luke(name):
    catalogue = {
        'Darth Vader': 'father',
        'Leia': 'sister',
        'Han': 'brother in law',
        'R2D2': 'droid',
        }
    #return f'Luke, I am your {catalogue[name]}.'
    return 'Luke, I am your {}'.format(catalogue[name])

print(relation_to_luke('Darth Vader'))
print(relation_to_luke('Leia'))
print(relation_to_luke('Han'))
print(relation_to_luke('R2D2'))
    