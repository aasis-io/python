class Employee:
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary

    def print_details(self):
        print("Name:" + self.name)
        print("Address:" + self.address)
        print("Salary:" + str(self.salary))

class Designer(Employee):
    def __init__(self, name, address, salary, tool):
        super().__init__(name, address, salary)
        self.tool = tool


    def print_details(self):
        super().print_details()
        print("Tool:" + self.tool)


    # def print_details(self):
    #     print("Name:" + self.name)
    #     print("Address:" + self.address)
    #     print("Salary:" + str(self.salary))
    #     print("Tool:" + self.tool)


class Developer(Employee):
    def __init__(self, name, address, salary, programming_lang):
        super().__init__(name, address, salary)
        self.programming_lang = programming_lang

    def print_details(self):
        super().print_details()
        print("Programming Language:" + self.programming_lang)

    # def print_details(self):
    #     print("Name:" + self.name)
    #     print("Address:" + self.address)
    #     print("Salary:" + str(self.salary))
    #     print("Programming Language:" + self.programming_lang)


designer1 = Designer(
    name = "Ashish",
    address = "Kathmandu",
    salary = 100000,
    tool = "Figma"
)

developer1 = Developer(
    name = "John",
    address = "NYC",
    salary = "$1000",
    programming_lang = "C"
)

designer1.print_details()

developer1.print_details()

print("Programming Language:")