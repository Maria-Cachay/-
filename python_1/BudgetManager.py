# Function to introduce the program and get user's name
def intro():
    """
    Introduces the Budget Manager calculator and gets the user's name.
    Returns the user's name as a string.
    """
    print("Hello, this is a Budget Manager calculator...")
    user_name = input("What is your name?: ")
    return user_name

# Function to continue the conversation
def continue_conversation(user_name):
    """
    Asks the user if they want to continue using the Budget Manager.
    Returns 'y' or 'n' based on user input.
    """
    return input("Would you like to continue, " + user_name + "? y/n: ").lower()

# Function to get the user's budget
def get_budget():
    """
    Asks the user for their earnings (budget).
    Returns the budget as a float.
    """
    return float(input("What are your earnings (budget)? Please enter only numbers: "))

# Function to get the user's total expenses
def get_total_expenses():
    """
    Asks the user for their total expenses.
    Returns the total expenses as a float.
    """
    return float(input("What are your total expenses?: "))

# Function to confirm if the user has more expenses
def confirm_more_expenses(user_name):
    """
    Asks the user to confirm if they have more expenses.
    Returns 'y' or 'n' based on user input.
    """
    return input("Are you sure you don't have more expenses, " + user_name + "? y/n: ").lower()

# Function to get the user's updated total expenses
def get_new_expenses():
    """
    Asks the user for their new total expenses if they have additional expenses.
    Returns the new total expenses as a float.
    """
    return float(input("Then what are your total expenses?: "))

# Function to calculate and display remaining money
def calculate_remaining(budget_amount, expenses_amount):
    """
    Calculates the remaining money after expenses.
    Prints and returns the remaining money as a float.
    """
    remaining_money = budget_amount - expenses_amount
    print("Your remaining money is " + str(remaining_money))
    return remaining_money

# Function to suggest savings
def suggest_savings(remaining_money):
    """
    Suggests saving 70% of the remaining money.
    Prints and returns the suggested savings amount as a float.
    """
    suggested_savings = 0.7 * remaining_money
    print("Suggest saving 70%: " + str(suggested_savings))
    return suggested_savings

# Function to calculate and display leisure money
def calculate_leisure(remaining_money):
    """
    Calculates 30% of the remaining money for leisure.
    Prints and returns the leisure money as a float.
    """
    leisure_money = 0.3 * remaining_money
    print("Available for leisure: " + str(leisure_money))
    return leisure_money

# Function for not understanding the user's answer
def not_understanding():
    """
    Informs the user that their input was not understood.
    """
    print("Sorry, I do not understand your answer...")
    print("This process will be terminated")

# Main function to run the program
def main():
    """
    Main function to run the Budget Manager program.
    Gets user input, calculates budget, expenses, savings, and leisure money.
    Prints a financial summary at the end.
    """
    user_name = intro()
    
    while True:
        if continue_conversation(user_name) == 'y':
            budget_amount = get_budget()
            total_expenses_amount = get_total_expenses()
            more_expenses_confirmation = confirm_more_expenses(user_name)

            if more_expenses_confirmation == 'n':
                remaining_money = calculate_remaining(budget_amount, total_expenses_amount)
            elif more_expenses_confirmation == 'y':
                total_expenses_amount = get_new_expenses()
                remaining_money = calculate_remaining(budget_amount, total_expenses_amount)
            else:
                not_understanding()
                break
            
            suggested_savings = suggest_savings(remaining_money)
            leisure_money = calculate_leisure(remaining_money)
            
            financial_summary = [
                "Earnings: " + str(budget_amount),
                "Total expenses: " + str(total_expenses_amount),
                "Remaining: " + str(remaining_money),
                "Savings suggested: " + str(suggested_savings),
                "Leisure available: " + str(leisure_money)
            ]

            print("Financial Summary:")
            for item in financial_summary:
                print(item)

        else:
            print("Bye!...") 
            break

if __name__ == "__main__":
    main()
