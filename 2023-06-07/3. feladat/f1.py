print('1. feladat: Téglalap kerülete és területe:')
print('Adja meg a téglalap oldalait')

a = None
while a == None:
    try:
        a = float(input('a = '))
    except:
        a = None

b = None
while b == None:
    try:
        b = float(input('b = '))
    except:
        b = None

print('T =', a * b)
print('K =', a + a + b + b)