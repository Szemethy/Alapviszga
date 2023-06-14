from repulogep import RepuloGep
import math

gepek: list[RepuloGep] = []

f = open('utasszallitok.txt', 'r', encoding='UTF-8')
f.readline()
for sor in f:
    gepek.append(RepuloGep(sor))
f.close()

print('4. feladat: adatsorok száma:', len(gepek))

db=0
for g in gepek:
    if g.tipus.startswith('Boeing'):
        db += 1
print(f'5. feladat: Boeing típusok száma: {db}')

maxKapacitasuGep = gepek[0]
for g in gepek:
    if maxKapacitasuGep.maxUtas < g.maxUtas:
        maxKapacitasuGep = g

print('6. feladat: A legtöbb utast szállító repülőgéptípus')
print(f'\tTípus: {maxKapacitasuGep.tipus}')
print(f'\tElső felszállás: {maxKapacitasuGep.ev}')
print(f'\tUtasok száma: {maxKapacitasuGep.utas}')
print(f'\tSzemélyzet: {maxKapacitasuGep.szemelyzet}')
print(f'\tUtazó sebesség: {maxKapacitasuGep.sebesseg}')

'''
# 1980 után gyártott gépek közül melyik a legnagyobb befogadóképességű
maxKapacitasuGep = None
for g in gepek:
    if g.ev > 1980:
        if maxKapacitasuGep == None or maxKapacitasuGep.maxUtas < g.maxUtas:
            maxKapacitasuGep = g
'''

stat = {}
for g in gepek:
    if g.kategoriaNev() in stat.keys():
        stat[g.kategoriaNev()] += 1
    else:
        stat[g.kategoriaNev()] = 1

#debug üzenet
print(stat)

hianyzoKategoriak = []
if 'Alacsony sebességű' not in stat.keys():
    hianyzoKategoriak.append('Alacsony sebességű')
if 'Szubszonikus' not in stat.keys():
    hianyzoKategoriak.append('Szubszonikus')
if 'Transzszonikus' not in stat.keys():
    hianyzoKategoriak.append('Transzszonikus')
if 'Szuperszonikus' not in stat.keys():
    hianyzoKategoriak.append('Szuperszonikus')

#debug üzenet
print(hianyzoKategoriak)

print('7. feladat:')
if len(hianyzoKategoriak) == 0:
    print('\tMinden sebességkategóriából van repülőgéptípus.')
else:
    print(f'\t{" ".join(hianyzoKategoriak)}')

f = open('utasszallitok_new.txt', 'w', encoding='UTF-8')
f.write('típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv\n')
for g in gepek:
    f.write('{0};{1};{2};{3};{4};{5};{6}\n'.format(   
             g.tipus,                        
             g.ev,                           
             g.maxUtas,
             g.szemelyzet.split('-')[-1],
             g.sebesseg,
             round(g.tomeg / 1000),    # nem felel meg a magyar kerekítési szabályoknak
             math.floor(0.5 + g.fesztav * 3.2808)
           ))

f.close()

try:
    q = float(input('Torlónyomás: '))
    p = float(input('Statikus nyomás:'))

    M = math.sqrt(  5 * ( math.pow(q/p + 1, 2/7) - 1 )   )
    print(f'Sebesség: {M} Mach')
except:
    print('Hibás érték')

print('program vége...')

