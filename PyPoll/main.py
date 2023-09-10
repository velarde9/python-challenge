import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Variables
totalVotes = 0

# Candidates Dictionary structure
# {
#  "Charles Casper Stockham": {
#    "numVotes": 85213
#  },
#  "Diana DeGette": {
#    "numVotes": 272892
#  },
#  "Raymon Anthony Doane": {
#    "numVotes": 11606
#  }
#}
candidates = {}
greatestVotes = 0
winnerCandidate = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Iterate through data rows
    for row in csvreader:
        # Increment total votes
        totalVotes = totalVotes + 1 
        candidate = row[2]

        # If the candidate doesn't exist in the dictionary, add candidate
        if candidates.get(candidate) == None: 
            candidates[candidate] = { "numVotes": 1}
        else:
        # Otherwise, update the vote count for the existing candidate
            candidates[candidate]["numVotes"] = candidates[candidate]["numVotes"] + 1

print("Election Results")
print("-------------------------")

print(f"Total Votes: {totalVotes}")
print("-------------------------")

# Iterate through candidates dictionary
for key in candidates:
    percentageOfVotes = round((candidates[key]['numVotes'] / totalVotes) * 100, 3)
    print(f"{key}: {percentageOfVotes}% ({candidates[key]['numVotes']})")

    # To determine the winner candidate
    if candidates[key]['numVotes'] > greatestVotes:
        greatestVotes = candidates[key]['numVotes']
        winnerCandidate = key

print("-------------------------")
print(f"Winner: {winnerCandidate}")
print("-------------------------")