class Student:
    sid = 1
    name = "John"
    address = "NYC"
    phone = "9856789987"

    def print_details(self):
        print("ID:", self.sid)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Phone:", self.phone)

student1 = Student()
student1.print_details()

