class Animal:
    def __init__(self, row):
        splitted = row.strip().split(';')
        #id;Species;name;city;born
        self.id = splitted[0]
        self.species = splitted[1]
        self.name = splitted[2]
        self.city = splitted[3]
        self.born = splitted[4]

        if self.born != "":
            splittedData = self.born.split('.')
            self.year = int(splittedData[0])
            self.month = int(splittedData[1])
            self.day = int(splittedData[2])
        else:
            self.year = 0
            self.month = 1
            self.day = 1