from time import sleep
from random import choice

def guess_name(name):
    # name = name.lower()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789.'
    guess = list('a' * len(name))  # a list of strings
    num = 0
    for index, char in enumerate(name):
        for char_2 in letters:
            sleep(0.015)  # looks cool when it does it a bit slower
            guess[index] = char_2
            print(num)
            num += 1
            print(''.join(guess))
            if char_2 == char:
                break

    print(''.join(guess))


def random_code_pattern(length=80):
    lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    code_pattern = []
    for i in range(length):
        code_pattern.append('%s%s ' % (choice(lst), choice(lst)))
    return ''.join(code_pattern)

# guess_name('')
# print(random_code_pattern())
# guess_name(random_code_pattern())
guess_name('THIS IS A DAY OF THE WEEK THAT IS NO ALLOWED TO WORK')

