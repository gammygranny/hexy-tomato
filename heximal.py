import math


def clear_screen():
    for i in range(d(114)):
        print('')


def from_base_ten(x, n):  # converts from decimal
    if x == 0: return 0
    newb = ''
    if x < 0:
        newb += '-'
        x = -x
    mag = int(math.log(x, n))  # Works out largest digit
    for i in range(16):  # Iterates through to change base
        power = mag - i
        N = n ** power
        newb += str(int(x / N))
        x = x % N
        if power == 0: newb += '.'
        if x == 0:
            if (mag - i) > 0: newb += '0' * (mag - i)
            break
    return float(newb)


def to_base_ten(x, n):
    if x == 0: return 0
    if x < 0:
        x = -x
        negative = 1
    else:
        negative = 0
    mag = int(math.log(x, 10))
    x = str(x)
    bten = point = 0
    for i in range(len(x)):
        if x[i] == '.':
            point = 1
        else:
            bten += int(x[i]) * n ** (mag - i + point)
    if negative == 1:
        bten = -bten
    return bten


def h(x):
    return from_base_ten(x, 6)


def d(x):
    return to_base_ten(x, 6)


print(h(1/7))


