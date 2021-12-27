# https://www.w3schools.com/python/ref_math_floor.asp

def rund_ned():

    # først må jeg importere math library
    import math

    # så kan jeg gå i gang med resten av funksjonen
    nummer = float(input('Skriv inn tallet du vil runde ned: \n'))
    print(math.floor(nummer))


rund_ned()
