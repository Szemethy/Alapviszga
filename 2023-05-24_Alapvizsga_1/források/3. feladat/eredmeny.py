class Eredmeny:
    def __init__(self, row):
        #Acsadi Lajos;1;Ferfi;30:28:42;100
        splittedData = row.strip().split(';')
        self.name = splittedData[0]
        self.number = splittedData[1]
        self.category = splittedData[2]
        self.time = splittedData[3]
        self.percent = int(splittedData[4])
        
    def hour(self):
        splittedData = self.time.split(':')
        hour = int(splittedData[0])
        minute = int(splittedData[1])
        second = int(splittedData[2])
        return hour + minute / 60 + second / 3600
