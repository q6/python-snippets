import random
def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return random.randint(0, 50) * 2

# print(genEven())

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return random.randrange(10, 20, 2)

print(deterministicNumber())