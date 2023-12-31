class BankAccount:
    def __init__(self, name: str, address: str, balance: int = 0) -> None:
        self.name = name
        self.address = address
        self.__balance = balance

    
    def printAccount(self):
        print(f"Name: {self.name}, Address: {self.address}, Balance: {self.__balance}")

    def deposit(self, amount: int) -> None:
        self.__balance += amount
        print(f"{self.name} has deposited {amount} and new balance is {self.__balance}")

    def withdraw(self, amount: int) -> None:
        self.__balance -= amount
        print(f"{self.name} has withdrawn {amount} and new balance is {self.__balance}")  

bankAccount = BankAccount("Ashish Thapa", "Satungal", 60000)

bankAccount.printAccount()

bankAccount.deposit(20000)

bankAccount.withdraw(10000)
