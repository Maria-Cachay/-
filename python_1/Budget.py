
earnings = float(input("Enter your earnings (Budget): "))

expenses = []

while True:
    expense = float(input("Enter an expense (or 0 if there are no more expenses): "))
    if expense == 0:
        break
    expenses.append(expense)

total_expenses = sum(expenses)
remaining = earnings - total_expenses

suggested_savings = 0.7 * remaining
leisure = 0.3 * remaining

print("\nFinancial Summary:")
print(f"Earnings (Budget): ")
print(f"Total Expenses: ")
print(f"Remaining: ")
print(f"Suggest saving 70%: ")
print(f"Available for leisure 30%: ")


print("\nThank you very much for using my program.")
