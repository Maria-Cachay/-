#Function introduction
def intro():
    print("Hello, this is a Budget Manager calculator...")
    return input("What is your name??: ")

#Function to continue
def continue_conversation(intro):
    return input("Would you like to continue, " + intro + "? y/n: ").lower()

#Asking Budget
def budget():
    return input("What is your earnings(budget)? enter only numbers pls: ")

#Function Total_Expenses
def Total_Expenses():
    return input("What are your total expenses?: ")

#Function more expenses?
def sure(intro):
    return input("Are you sure you don't have more expenses? " + intro + "? y/n").lower()
#Function to 
def new_expenses():
    return input("Then what are your total expenses?: ")

#Function remaining money
def remaining_calc(remaining):
    print("Your remaining money is " + remaining)

#def for not understanding the user's answer
def not_understanding():
    print("Sorry I do not understand your answer...")
    print("This process will be terminated")

#Suggested savings
def savings(save):
    print("Suggest saving 70%: " + save)
    save = 0.7 * remaining
#leisure function
def leisuretext(leisure):
    leisure = 0.3 * remaining
    print("available for leisure: " + leisure)

#Calculation of amount of money remaining
if sure() == 'n':
    remaining = budget - Total_Expenses
    if sure()== 'y':
        remaining = budget - new_expenses
else:
    not_understanding()

save = savings()
savings(save)

leisure = leisuretext()
leisuretext(leisure)

#List of variables
Financial_summary = ["earnings: " + budget + ", Total expenses: " + new_expenses + ", remaings: " + remaining + "Savings suggested: " + save + ", leisure available: " + leisure ]

#Organized init
def main():
    while True:
        
#Greet user and get name
        intro()
        continue_conversation(intro)
        if continue_conversation == 'y':
            budget()
            Total_Expenses()

#Expenses changed
            if sure() == 'y':
                remaining = remaining_calc(remaining)
                earnings = budget(earnings)
                remaining = budget - new_expenses
#Remaining calc showed
                print(remaining_calc(remaining))
                save = savings()
                savings(save)

#leisure calc showed
                leisure = leisuretext()
                leisuretext(leisure)

#Financial summary
                print(Financial_summary)

#Expenses not changed
            if sure() == 'n':
                remaining = remaining_calc(remaining)
                earnings = budget(earnings)
                remaining = budget - Total_Expenses

#Remaining calc showed
                print(remaining_calc(remaining))
                save = savings()
                savings(save)

#leisure calc showed
                leisure = leisuretext()
                leisuretext(leisure)

#Financial summary
                print(Financial_summary)

#If user does not want to continue the conversation
        if continue_conversation == 'n':
            print("Bye!...")
            break

        else:
            not_understanding()
            break