##########################################################################################
################################### Imports ##############################################

import os    # Module to create file paths across operating systems
import csv   # Module to read CSV files
import time  # Track time for program to execute

start_time = time.process_time()  # Track Time (start)

def check_duplicates(list):
    count = 0
    for i in list:
        if i == 0:
            count += 1
    return count

##########################################################################################
######################### Data Extract / Create Lists #####################################

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Header row:  Voter ID,County,Candidate
    header_row = next(csvreader)

    # Create list of candidates and list of votes and total votes
    candidates = []
    votes =[]
    total = 0

    # move candidate data into candidates list and summ votes
    for row in csvreader:
        name = row[2]   #index 2 - Candidate
        total += 1

        if name not in candidates:
            candidates.append(name)
            votes.append(0)
            votes[candidates.index(name)] = 1
        else:
            votes[candidates.index(name)] += 1

# print(candidates)
# print(votes)
# print(total)

# Create printout of candidates and their votes and percents
print(f"\n\n")

i = 0
message = ""
for name in candidates:
    message = message + f'{name}:  {round(votes[i]/total*100,1)}% ({votes[i]})\n'
    i += 1

print(message)

# Determine the maximum number of votes and first location of that number in votes list
max_votes = max(votes)
max_votes_index = votes.index(max_votes)

votes_diff = [(candidate_votes - max_votes) for candidate_votes in votes]
# votes_diff = [0,0,4,5]    # test data for if statement
number_duplicates = check_duplicates(votes_diff)

# checks if there is a tie or a single winner
if number_duplicates > 1:
    print(f'There is a tie with:')
    for i in range(len(votes_diff)):     # this is an example of where 'in range()' is better than 'in votes_diff' and .index().  .index of non-unique values pulls the first value.
        if votes_diff[i] == 0:
            print(f'{candidates[i]}')

else:
    print(f"The winner is {candidates[max_votes_index]}")

print(f"\n\n")

print(f"--- {(time.process_time() - start_time)} seconds ---")  # Final program run time
