def my_adder():
    the_numbers = input('Write the numbers you want to add, separated by commas: ')
    to_integers = list(the_numbers.split(','))
    print(to_integers)
    sum = 0;
    for l in to_integers:
        int(l)
        print(f'{l} is of type {type(l)}')
        sum += 1
    print('The sum is: {sum}')

my_adder()

"""
def adder(*the_numbers):
    sum = 0
    for j in the_numbers:
        sum += 1
    print(f'The sum is: {sum}.')

adder()
"""
