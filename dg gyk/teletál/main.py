from etel import Etel

etelek: list[Etel] = []
f = open('teletal.csv', 'r', encoding='UTF-8')
f.readline()
for sor in f:
    etelek.append(Etel(sor))
f.close()

print(f'2. feladat: {len(etelek)} étel van a kínálatban.')

db = 0
for e in etelek:
    if e.fajta == 'Főétel':
        db += 1

print(f'3. feladat: {db} db főétel van a listában.')

legolcsobb = etelek[0]
for e in etelek:
    if e.ar < legolcsobb.ar:
        legolcsobb = e

print(f'4/a feladat: A legolcsóbb étel: {legolcsobb.megnevezes}')

legolcsobb = None
for e in etelek:
    if e.fajta == 'Menü':
        if legolcsobb == None or e.ar < legolcsobb.ar:
            legolcsobb = e

print(f'4/b feladat: A legolcsóbb menü: {legolcsobb.megnevezes}')

osszesen = 0
for e in etelek:
    if e.fajta == 'Főétel':
        osszesen += e.bevetelEuroban(402.5)

print(f'5. feladat: Az összes árbevétel euróban a főételekből: {osszesen} euró')

statisztika = {}
for e in etelek:
    if e.fajta in statisztika.keys():
        statisztika[e.fajta] += e.mennyiseg
    else:
        statisztika[e.fajta] = e.mennyiseg

print('6. feladat: statisztika')

for key, value in statisztika.items():
    if value > 1000:
        print(f'\t{key} - {value}')

ar = int(input('7. feladat: Mennyi pénzed van? '))
f = open('olcso.txt', 'w', encoding='UTF-8')
f.write('Megnevezés;Ár\n')
for e in etelek:
    if e.ar <= ar:
        f.write(f'{e.megnevezes};{e.ar}\n')
f.close()
