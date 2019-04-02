"""
Chris Reppel
Prac 1
5/3/19
"""

total = 0
number = int(input("How many items: "))

while number < 0:
    print("Invalid number of items!")
    number = int(input("How many items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for ", number, " items is $", total, sep='')

print("Total price with discount for {} items is ${:.2f}".format(number, total))
