import random

def halmaz_e(x):
    for elem in x:
        if x.count(elem) > 1:
            return 'Halmaznak nem tekinthető'
    return 'Halmaznak tekinthető'

for i in range(8):
    lista = []
    for j in range(5):
        lista.append(random.randint(0, 9))
    print(lista, '->', halmaz_e(lista))