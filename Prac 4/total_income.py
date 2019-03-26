"""
Chris Reppel
Prac 4
26/3/19
"""


def main():
    """Display income report for incomes over a given number of num_months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:5.2f} Total: ${:5.2f}".format(month + 1, income, total))


main()
