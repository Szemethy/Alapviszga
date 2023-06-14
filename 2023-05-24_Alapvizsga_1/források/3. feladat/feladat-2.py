def tokeletes_e(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

print('2. feladat: tökéletes számok')
print('Kérek két természetes számot')
tol = int(input('tól = '))
ig = int(input('ig = '))

# volt = False
# for i in range(tol, ig + 1):
#     if tokeletes_e(i):
#         print(i, end='; ')
#         volt = True
# if not volt:
#     print('nincs')
tokeletesSzamok = []
for i in range(tol, ig + 1):
    if tokeletes_e(i):
        tokeletesSzamok.append(str(i))

if len(tokeletesSzamok) == 0:
    print('A megadott tartományban nincsen tökéletes szám!')
else:
    print('; '.join(tokeletesSzamok))

