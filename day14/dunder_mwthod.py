class BankAccount:
    def __init__(self, name: str, address: str, balance: int = 0) -> None:
        self.name = name
        self.address = address
        self.__balance = balance

    
    def printAccount(self):
        print(f"Name: {self.name}, Address: {self.address}, Balance: {self.__balance}")


bankAccount = BankAccount("Ashish Thapa", "Satungal", 60000)

bankAccount.printAccount()
