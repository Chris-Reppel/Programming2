"""
Chris Reppel
Prac 1
5/3/19
"""

# Odd number from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# In tens from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# From 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Ask for number and print in stars
stars = int(input('Enter a number: '))
for i in range(stars):
    print('*', end=' ')
print()

# Print increasing number of stars on a line
for i in range(1, stars, 1):
    print('*' * i)
print()
