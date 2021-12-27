# https://edabit.com/challenge/8rcrBw82sfHyCmJMG
# https://note.nkmk.me/en/python-tuple-list-unpack/
my_list = [0, 1, 2]

a, *b = my_list
# her har man bare to variabler, mens det er 3 items i listen
# det vil føre til en callback
# men, setter man en stjerne foran b, vil denne variabelen inneholde resten
# stjernen foran b gjør at b blir om til en list med resten

print(a)
print(b)
print(my_list) # den originale listen er fortsatt urørt
