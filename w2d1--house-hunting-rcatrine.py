# Enter the cost of your dream home:
total_cost = int(input("Enter the cost of your dream home: "))

# Enter the percent of your salary to save, as a decimal:
percent_saved = float(input("Enter the percent of your salary to be saved as a decimal (portion_saved): "))

# Enter your annual salary:
annual_salary = int(input("Enter your annual salary: "))

# Calculate my down payment
percentage_down_payment = .25*total_cost

# Set initial information
current_savings = 0
interest_rate = .04
current_month = 0

# Each month until our savings >= down payment
while True:
    # add 1 to current month
    current_month += 1
    # Calculate interest -- current savings * rate (0.04) / 12, add interest to current savings, add the amount I'm saving to my current savings
    current_savings += (current_savings*interest_rate/12+percent_saved)
    # break when down payment percentage is greater than or equal to current savings
    if current_savings >= percentage_down_payment:break
    
# Report how many months that took
print("It will take {0} months to make a down payment of ${1} by saving ${2}".format(current_month, percentage_down_payment, current_savings))

