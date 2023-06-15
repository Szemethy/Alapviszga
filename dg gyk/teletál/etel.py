class Etel:
    def __init__(self, sor) -> None:
        #Fajta;Megnevezés;Ár;Rendelt mennyiség

        adat = sor.strip().split(';')
        self.fajta = adat[0]
        self.megnevezes = adat[1]
        self.ar = int(adat[2])
        self.mennyiseg = int(adat[3])

    def bevetelEuroban(self, arfolyam):
        return round(self.mennyiseg * self.ar / arfolyam, 2)