# a=1

# while a <= 5:
#     print(a)
#     a=a+1

# while True:

# numbers = [4,6,7,9,24]

# search_number = 5
# for number in numbers:
#     if number == search_number:
#         print("number found")
#         break

#     else:
#         print("number not found");1


# while True:
#     number = input("Enter a number:")

#     if(number.isdigit()):
#         print("You")


# numbers = [5,6,75,6,8,9]

# for number in numbers:
#     if number%2 != 0:
#         print(number)

    


# task management system

# invoke user to input task
# unvoke the user to input the task until
# user inputs exit string
# once user exit the task  input print the task items


# Task Management System

tasks = []

while True:
    # Invoke user to input task
    task = input("Enter a task (type 'exit' to end): ")

    # Check if the user wants to exit
    if task.lower() == 'exit':
        break

    # Add the task to the list
    tasks.append(task)

# Print the task items
print("\nTask List:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
