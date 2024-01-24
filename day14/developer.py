# from employee import Employee


import employee as emp
class Developer(emp.Employee):
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