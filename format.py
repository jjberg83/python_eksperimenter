"""
Pyhons String template versjon
Returner 'Hello, my Love!' hvis navn er Jørund,
og 'Hello, navn!' for alle andre navn.
"""

def hilsen(navn):
    return 'Hello, {}!'.format('my Love' if navn == 'Jørund' else navn)

#print(hilsen('Jørund'))
#print(hilsen('Jøran'))

def hilsen_med_input():
    navn = input('Hvem er du? \n')
    print('Hallo, {}!'.format('babe' if navn == 'Jørund' else navn))

hilsen_med_input()
