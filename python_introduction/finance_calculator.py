# Step 1: User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Step 2: Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Step 3: Project Annual Savings with Interest
annual_savings = monthly_savings * 12
projected_savings_with_interest = annual_savings + (annual_savings * 0.05)

# Step 4: Output Results
print(f"Your monthly savings are: ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings_with_interest:.2f}.")
