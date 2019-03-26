"""
Chris Reppel
Prac 4
26/3/19
"""

# Basic list operations:
numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Your first number is", numbers[0])
print("Your last number is", numbers[-1])
print("Your smallest number is", min(numbers))
print("Your largest number is", max(numbers))
print("Your average of the numbers is", sum(numbers) / len(numbers))


# Woefully inadequate security checker:
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
