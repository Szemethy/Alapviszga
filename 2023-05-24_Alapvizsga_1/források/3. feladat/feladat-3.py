from eredmeny import *

competitors: list[Eredmeny] = []
f = open('ub2017egyeni.txt', 'r', encoding='utf-8')
f.readline()
for row in f:
    competitors.append(Eredmeny(row))
f.close()

print(f'3.2 feladat: Futók száma: {len(competitors)}')

count = 0
for c in competitors:
    if c.category == 'Noi' and c.percent == 100:
        count += 1
print(f'3.3 feladat: Célba érkező női sportolók: {count} fő')

competitorWithLongestName = competitors[0]
for c in competitors:
    if len(c.name) > len(competitorWithLongestName.name):
        competitorWithLongestName = c
print('3.4 feladat: A leghosszabb nevű futó')
print(f'\tNév: {competitorWithLongestName.name}')
print(f'\tRajtszám: {competitorWithLongestName.number}')
print(f'\tEredmény: {competitorWithLongestName.time}')

count = 0
sum = 0
for c in competitors:
    if c.category == 'Ferfi' and c.percent == 100:
        count += 1
        sum += c.hour()
print(f'3.5 Férfi sportolók átlagos ideje: {sum / count:.2f} óra')        
