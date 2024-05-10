document.getElementById("budgetForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission from refreshing the page

    // Retrieve values from the form
    let yearlyIncome = parseInt(document.getElementById("income").value, 10);
    let yearlyExpenses = parseInt(document.getElementById("expenses").value, 10);
    let yearlySavingsGoal = parseInt(document.getElementById("savingsGoal").value, 10);

    // Calculate remaining budget
    let remainingBudget = yearlyIncome - yearlyExpenses;
    let goalAchieved = remainingBudget >= yearlySavingsGoal;

    // Initialize the financial health indicator
    let isFinanciallyHealthy = false;

    // Check conditions using logical operators
    if (remainingBudget >= 500 || goalAchieved) {
        isFinanciallyHealthy = true;
    }

    // Display results based on the remaining budget and the savings goal
    let resultMessage;
    if (isFinanciallyHealthy) {
        resultMessage = `Good news! You are in a healthy financial position. Remaining Budget: $${remainingBudget}.`;
    } else {
        let shortfall = yearlySavingsGoal - remainingBudget;
        resultMessage = `You are short of your savings goal by $${shortfall}. Consider reducing expenses or increasing income.`;
    }

    // Print the result to the console and update the result message in the DOM
    console.log(resultMessage);
    document.getElementById("result").textContent = resultMessage;
});
