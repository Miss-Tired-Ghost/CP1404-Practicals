"""
Provide example usage of list operators
Code by: Miss Ghost/April First
"""

# Basic list operations
numbers = []
for _ in range(5):
    numbers.append(float(input("Number: ")))  # assuming the intention is to support floats, not just integers
# f"{number:g}" removes trailing 0s
# can use multiple prints to replace the """"""" but both options feel bad
# a singular long print breaks pep8 standards and is hard to read
# recommendations are appreciated
print(f"""The first number is {numbers[0]:g}
The last number is {numbers[-1]:g}
The smallest number is {min(numbers):g}
The largest number is {max(numbers):g}
The average of the number is {sum(numbers)/len(numbers):g}""")


# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
