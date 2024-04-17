import csv
import os

# Define the file path
csv_path = os.path.join("resources", "election_data.csv")
output_file = os.path.join("analysis", "results.txt")

# Initialize vote count
total_votes = 0
candidates = {}

# Open the CSV file
with open(csv_path, newline='') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1
        
        # Extract the candidate name from the current row
        candidate_name = row[2]
        
        # Add the candidate to the dictionary and increment their vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the winner
winner_name = max(candidates, key=candidates.get)

# Prepare the output string
output_str = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output_str += f"{candidate}: {percentage:.3f}% ({votes})\n"

output_str += (
    "-------------------------\n"
    f"Winner: {winner_name}\n"
    "-------------------------\n"
)

# Print Election Results to terminal
print(output_str)

# Write results to text file
with open(output_file, "w") as txtfile:
    txtfile.write(output_str)

print(f"Results saved to {output_file}")