# class Student:

#     def __init__(self, student_id, name, add, phone):
#         self.student_id = student_id
#         self.name = name
#         self.add = add
#         self.phone = phone

#     def print_details(self):
#         print("ID:", self.student_id)
#         print("Name:", self.name)
#         print("Address:", self.add)
#         print("Phone:", self.phone)

# student1 = Student(1, "John", "ktm", "9878990098")
# student1.print_details()

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def printCalculation(self):
        print("Addition = ", self.a+self.b)
        print("Subtraction = ", self.a-self.b)
        print("Division = ", self.a/self.b)
        print("Multiplication = ", self.a*self.b)

calc = Calculator(6, 3)

calc.printCalculation()

