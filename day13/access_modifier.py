class Bike:
    def __init__(self, name:str, cc:int)->None:
        self.name = name
        self.cc = cc

    def printBike(self):
        print(f"Bike name {self.name} and cc is {self.cc}")


Bike = Bike("BMW", 1000)
Bike.printBike()