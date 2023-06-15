from animal import Animal

animals :list[Animal] = []
file = open('Animals.csv', 'r', encoding='utf-8')
file.readline()
for row in file:
    animals.append(Animal(row))
file.close()

print(f'1.feladat: A listában {len(animals)} db állat van.')

city = input('Kérek egy várost: ')
print('2. feladat: Állatok ebben a városban: ')
for item in animals:
    if item.city == city:
        print(f'\t{item.name} ({item.species})')

month = 0
while month < 1 or month > 12:
    month = int(input('Kérem a hónapot: '))
day = int(input('Kérem a napot: '))
print('3. feladat: Ezen a napon születtek:')
for item in animals:
    # varos: nev(faj): 20 éves
    if month == item.month and day == item.day:
        if item.year == 0:
            print(f'\t{item.city}: {item.name}({item.species}): Kora ismeretlen')
        else:
            print(f'\t{item.city}: {item.name}({item.species}): {2023-item.year} éves')

count = 0
for item in animals:
    if item.born == '':
        count +=1

print(f'4.feladat: {count} db állatnak nem tudjuk az életkorát.')

stat = {}
for item in animals:
    if item.species in stat.keys():
        stat[item.species] += 1
    else:
        stat[item.species] = 1
print('5.feladat: statisztika:')
for key, value in stat.items():
    print(f'\t{key}: {value} db')

file2 = open('ogre.txt', 'w', encoding='utf-8')
for item in animals:
    if item.species == 'Ogre':
        file2.write(f'{item.city};{item.name};{item.born}\n')
file2.close()