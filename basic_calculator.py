#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:09:04 2021

@author: jjberg
"""

"""
Test.assert_equals(calculator(2, '/', 2), 1)
Test.assert_equals(calculator(10, '-', 7), 3)
Test.assert_equals(calculator(2, '*', 16), 32)
Test.assert_equals(calculator(2, '-', 2), 0)
Test.assert_equals(calculator(15, '+', 26), 41)
Test.assert_equals(calculator(2, '+', 2), 4)
Test.assert_equals(calculator(2, "/", 0), "Can't divide by 0!")
"""

"""
# Method 1
# Converting num1 and num2 into strings
def calculator(num1, operator, num2):
    if operator == '/' and num2 == 0:
        return 'Can\'t divide by 0!'
    return eval(str(num1) + operator + str(num2))
"""

# Method 2
# Using the operator python library
# https://python.astrotech.io/stdlib/builtin/operator.html
import operator

def calculator(num1, operator, num2):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return sub(num1, num2)
    elif operator == '*':
        return mul(num1, num2)
    elif operator == '/' and num2 == 0:
        return 'Can\'t divide by 0!'
    

#print(calculator(2, '/', 2))
print(calculator(10, '-', 7))
print(calculator(2, '*', 16))
print(calculator(2, '-', 2))
print(calculator(15, '+', 26))
print(calculator(2, '+', 2))
#print(calculator(2, "/", 0))
