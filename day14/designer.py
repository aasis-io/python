import employee as emp

class Designer(emp.Employee):
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