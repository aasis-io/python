from abc import ABC, abstractmethod

class Vechile(ABC):
    
    @abstractmethod
    def start(self):
        pass




class Car(Vechile):
    def __init__ (self, name):
        self.name = name

    def start(self):
        print(f"{self.name} is starting...")

    def stop(self):
        print(f"{self.name} is stopping...")


car = Car(name = "BYD")
car.start()
car.stop()
