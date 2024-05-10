import csv

# Initialize variables
total_months = 0
net_total = 0
changes = []
greatest_increase = 0
greatest_decrease = 0

# Read the CSV file
with open('/Users/syedshahid/python-challenge/PyBank/Resources/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    data = list(reader)

# Loop through the data
for i in range(len(data)):
    # Update total months
    total_months += 1
    
    # Calculate net total
    net_total += int(data[i][1])

    # Calculate change in profit/losses
    if i > 0:
        change = int(data[i][1]) - int(data[i-1][1])
        changes.append(change)

        # Update greatest increase and decrease
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = data[i][0]
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = data[i][0]

# Calculate average change
average_change = sum(changes) / len(changes)

# Print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
