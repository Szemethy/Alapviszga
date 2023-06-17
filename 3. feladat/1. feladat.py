print('LNKO kivonásos algoritmussal')
a = int(input('a = '))
b = int(input('b = '))
def LNKO(a, b):
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b =  b - a
    return a
print(f'LNKO {a, b} = {LNKO(a, b)}')
