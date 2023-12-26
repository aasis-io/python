# def person(name, address, age):
#     print("Name:", name)
#     print("Address:", address)
#     print("Age:", age)

# person(name= "John", address= "NYC",
#  age=23)

# def perform_math_operation(n1,n2,oper):
    
#     if(oper== "+"):
#         print(f"The sum of {n1} and {n2} is {n1+n2}")
#     elif(oper== "-"):
#         print(f"The sub of {n1} and {n2} is {n1-n2}")
#     elif(oper== "/"):
#         print(f"The div of {n1} and {n2} is {n1/n2}")
#     elif(oper== "*"):
#         print(f"The mul of {n1} and {n2} is {n1-n2}")
        
        
        
# n1=int(input("Enter your first number : "))
# n2=int(input("Enter your second number : "))
# oper=input("Enter your  operation : ")


# perform_math_operation(n1,n2,oper)


# def multiply(*args):
#     total_multiply = 1

#     for number in args:
#         total_multiply *= number

#     return total_multiply

# total_value = multiply(1, 2, 3)

# print(total_value)



# def greet(**kwargs):
#     print(type(kwargs))

# greet(name1="John", name2="Doe")


# def total_marks(math, english, **kwargs):
#     total = math + english

#     for subject, mark in kwargs.items():
#         total += mark
    
#     print("Total marks:", total);

# total_marks(math = 23, english = 45, opt_math = 10, account=20)


def print_info(name, **args):
    print("Name:", name)

    for detail, value in kwargs.items():
        print(f"{detail}:", value)



print_info(name = "ashish", age = 23, phone = 9840033688)