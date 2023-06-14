class RepuloGep:
    def __init__(self, sor: str):
        # típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv
        # Airbus A300;1972;220-336;3;911;142000;44,84
        
        spilettedData = sor.strip().split(';')
        self.tipus = spilettedData[0]
        self.ev = int(spilettedData[1])
        self.utas = spilettedData[2]
        self.szemelyzet = spilettedData[3]
        self.sebesseg = int(spilettedData[4])
        self.tomeg = int(spilettedData[5])
        self.fesztav = float(  spilettedData[6].replace(',', '.')  )

        self.maxUtas = int(self.utas.split('-')[-1])


    def kategoriaNev(self):
        if self.sebesseg < 500:
            return 'Alacsony sebességű'
        if self.sebesseg < 1000:
            return 'Szubszonikus'
        if self.sebesseg < 1200:
            return 'Transzszonikus'
        return 'Szuperszonikus'
