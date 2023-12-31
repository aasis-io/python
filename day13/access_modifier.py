class Bike:
    def __init__(self, name:str, cc:int)->None:
        self.__name = name
        self.cc = cc

    def printBike(self):
        print(f"Bike name {self.__name} and cc is {self.cc}")


Bike = Bike(name="BMW", cc=1000)
Bike.printBike()

# Bike._name = "Kawasaki"

print(Bike.__name)