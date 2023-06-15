class Player:
    def __init__(self, row) -> None:
        splittedData = row.strip().split(';')
        self.azonosító = splittedData[0]
        self.név = splittedData[1]
        self.ország = splittedData[2]
        self.neme = splittedData[3]
        self.pontszám = int(splittedData[4])
        self.év = splittedData[5]

    def szupernagymester(self):
        if self.neme == "F" and self.pontszám >= 2700:
            return True
        if self.neme == "N" and self.pontszám >= 2500:
            return True
        return False
    
    


