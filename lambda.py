# anonym lambda inni annen funksjon
# doble tallet man setter inn i original funksjon
def originalFunc(tall):
    return lambda a : a * tall

myDoubler = originalFunc(2)

print(myDoubler(10))
