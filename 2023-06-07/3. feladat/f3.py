from fogadasi_fordulo import Fogadasi_fordulo

fordulok: list[Fogadasi_fordulo] = []

print('3. feladat')
print('3.1 feladat: Adatok beolvasása és tárolása')

f = open('toto.txt', 'r')
f.readline()
for sor in f:
    fordulok.append(Fogadasi_fordulo(sor))
f.close()

print(f'3.2 feladat: Fogadási fordulók száma: {len(fordulok)}')

db = 0
for elem in fordulok:
    db += elem.t13p1
print(f'3.3 feladat: Telitalálatos szelvények száma: {db} darab')

i = 0
while i < len(fordulok) and 'X' in fordulok[i].eredmenyek:
    i += 1
if i < len(fordulok):
    print('3.4 feladat: Volt döntetlen mentes forduló')
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló')