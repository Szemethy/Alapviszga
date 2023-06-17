from Data import Épület

épületek = []
f = open('legmagasabb.txt', 'r', encoding='UTF-8')
f.readline()
for row in f:
    épületek.append(Épület(row))
f.close()

print(f"Az állományban található épületek száma: {len(épületek)}")


emeletek_összege = sum(épület.emelet for épület in épületek)
print("Az állományban található épületek emeleteinek összege: {}".format(emeletek_összege))

legmagasabb_épület = épületek[0]
for sor in épületek:
    if legmagasabb_épület.magasság < sor.magasság:
        legmagasabb_épület = sor
print("A legmagasabb épület adatai:")
print(f"Név: {legmagasabb_épület.név}")
print(f"Város: {legmagasabb_épület.város}")
print(f"Ország: {legmagasabb_épület.ország}")
print(f"Magasság: {legmagasabb_épület.magasság} m")
print(f"Emeletek száma: {legmagasabb_épület.emelet}")
print(f"Építés éve: {legmagasabb_épület.épült}")

i = 0
while i < len(épületek) and épületek[i].ország != "Olaszország":
    i += 1
if i < len(épületek):
    print("Az adatok között található olasz épület.")
else:
    print("Az adatok között nincs olasz épület.")