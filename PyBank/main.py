import os
import csv

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the CSV file
file_path = os.path.join(current_directory, "resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

     # Skip the header row
    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment total months
        total_months += 1

        # Calculate net total
        net_total += int(row[1])

        # Calculate change in profit/loss
        if total_months > 1:
            change = int(row[1]) - previous_profit_loss
            monthly_changes.append(change)

            # Check for greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        # Store current profit/loss for next iteration
        previous_profit_loss = int(row[1])

# Calculate the average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Print analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write analysis results to a text file
output_file = os.path.join(current_directory, "analysis", "results.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print("Analysis results have been written to analysis/results.txt.")