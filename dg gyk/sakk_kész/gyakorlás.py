from player import *

players: list[Player] = []

f = open("sakk.txt", "r", encoding="UTF-8")
f.readline()

for elem in f:
    players.append(Player(elem))    

f.close()

print(f"4.feladat: Versenyzők száma: {len(players)}")


sum = 0
for elem in players:
    if elem.neme == "N":
        sum = sum + 1

print(f"5.feladat: Női versenyzők aránya: {sum/len(players)*100}")


mesterek = 0
for elem in players:
    if elem.szupernagymester():
        mesterek = mesterek + 1
print(f"7.feladat: supernagymesterek száma {mesterek}")

legjobbférfi = players[0]
legjobbnői = players[0]
for elem in players:
    if elem.neme == "F" and elem.pontszám > legjobbférfi.pontszám:
        legjobbférfi = elem
    if elem.neme == "N" and elem.pontszám > legjobbnői.pontszám:
        legjobbnői = elem

print("A ranglista vezető sakkozok")
print(f"\tFérfi: {legjobbférfi.név} - {legjobbférfi.ország} - {legjobbférfi.azonosító} - {legjobbférfi.pontszám}")
print(f"\tNői: {legjobbnői.név} - {legjobbnői.ország} - {legjobbnői.azonosító} - {legjobbnői.pontszám}")

print("9.feladat:")

évszám = int(input("\tÉv: "))

sor = 0
while sor <len(players) and évszám != players[sor].év:
    sor += 1

if sor < len(players):
    print("Az adott évben volt versenyző")
else:
    print("Az adott évben nem volt versenyző")
