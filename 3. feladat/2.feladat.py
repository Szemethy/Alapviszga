def számol(nap):
    magánhangzó = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
    db = 0
    for i in nap:
        if i.lower() in magánhangzó:
            db += 1
    return db

napok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
max_magánhangzó = 0
max_magánhangzó_nap = ''

for nap in napok:
    magánhangzó_db = számol(nap)
    if magánhangzó_db > max_magánhangzó:
        max_magánhangzó = magánhangzó_db
        max_magánhangzó_nap = nap

print(f"A legtöbb magánhangzó a(z) {max_magánhangzó_nap} hétköznap nevében van.")