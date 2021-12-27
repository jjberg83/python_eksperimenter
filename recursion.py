"""
Recursion med Python
"""

# FACTORIAL
def factorial(n):
    if n == 1 :
        return 1
    else :
        return (n * factorial(n-1))

#print(factorial(3))

# WORD REPATED X TIMES
# Med denne metoden endrer man bare x
# word endres ikke, men legges til for hver iteration
def wordRepeat(word, x):
    x -= 1
    if x == 0 :
        return word
    else :
        return wordRepeat(word, x) + word
