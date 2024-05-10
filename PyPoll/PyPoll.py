import csv

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open('/Users/syedshahid/python-challenge/PyPoll/Resources/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    data = list(reader)

# Loop through the data
for row in data:
    # Increment total votes
    total_votes += 1
    
    # Extract candidate's name
    candidate_name = row[2]

    # Update candidate's vote count
    if candidate_name in candidate_votes:
        candidate_votes[candidate_name] += 1
    else:
        candidate_votes[candidate_name] = 1

# Calculate percentage of votes for each candidate and determine the winner
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100

    # Update winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Prepare the analysis string
analysis = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Calculate percentage of votes for each candidate and add to the analysis
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    analysis += f"{candidate}: {percentage:.3f}% ({votes})\n"

# Add winner information to the analysis
analysis += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------"
)

# Print the analysis to the terminal
print(analysis)

# Export the analysis to a text file
with open('election_results.txt', 'w') as output_file:
    output_file.write(analysis)

print("Analysis exported to election_results.txt")
