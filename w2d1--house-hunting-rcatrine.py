# Enter the cost of your dream home:
total_cost = int(input("Enter the cost of your dream home: "))

# Enter the percent of your salary to save, as a decimal:
portion_saved = float(input("Enter the percent of your salary to be saved as a decimal (portion_saved): "))

# Enter your annual salary:
annual_salary = int(input("Enter your annual salary: "))

# Calculate my down payment
portion_down_payment = .25*total_cost

# Set initial information
current_savings = 0
r = .04
month = 0

while True:
    # add 1 to current month
    month += 1
    # Calculate interest -- current savings * rate (0.04) / 12, add interest to current savings, add the amount I'm saving to my current savings
    current_savings += (current_savings*r/12+portion_saved)

    if current_savings >= portion_down_payment:break

# Report
print("It will take {0} months to make a down payment of ${1} by saving ${2}".format(month, portion_down_payment,current_savings))