from designer import Designer
from developer import Developer

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

