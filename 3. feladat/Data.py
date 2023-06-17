class Épület:
    def __init__(self, row):
        SplittedData = row.strip().split(";")
        self.név = SplittedData[0]
        self.város = SplittedData[1]
        self.ország = SplittedData[2]
        self.magasság = float(SplittedData[3].replace(",", "."))
        self.emelet = int(SplittedData[4])
        self.épült = int(SplittedData[5])