"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    get_months()


def get_months():
    incomes = []
    number_of_months = int(input("How many months? "))
    for month in range(1, number_of_months + 1):
        get_income(incomes, month)
    print_report(incomes, number_of_months)


def get_income(incomes, month):
    income = float(input(f"Enter income for month {month}: "))
    incomes.append(income)



def print_report(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income, total = calculate_total(incomes, month, total)
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def calculate_total(incomes, month, total):
    income = incomes[month - 1]
    total += income
    return income, total


main()

