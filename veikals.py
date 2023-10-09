class Prece:
    def __init__(self, name, count, type):
        self.nosaukums = name
        self.skaits = count
        self.veids = type
        self.info()

    def info(self):
        print("Veikala plauktos atrodas",self.count ,"preces.")
        

class datori(Prece):
    def __init__(self, name, count, manufacturer):
        super().__init__(name, count, "dators")
        self.__razotajs = manufacturer
        self.info()

pirmais = Prece("RTX 3080", 7, "NvidiaS")
print(pirmais)