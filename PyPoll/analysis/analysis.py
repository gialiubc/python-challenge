# Modules
import os
import csv

# Set path for csv file
csvpath = os.path.join("PyPoll/Resources/election_data.csv")

# Open csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the csvheader
    csvheader = next(csvreader)

    # Loop through the data
    election_data = []
    for row in csvreader:
        election_data.append(row)

    # The total number of votes cast
    total_votes = len(election_data)

    # A complete list of candidates who received votes
    # Retrieve the Candidate column to a list
    candidate_list = []
    for i in range(total_votes-1):
        candidate = election_data[i][2]
        candidate_list.append(candidate)
    # Create a list for unique value of candidate's name
    unique_list = []
    for x in candidate_list:
        if x not in unique_list:
            unique_list.append(x)
    
    # The total number of votes each candidate won
    candidate1_vote = 0
    candidate2_vote = 0
    candidate3_vote = 0

    for i in range(total_votes):
        #The total number of votes for candidate 1
        if election_data[i][2] == unique_list[0]:
            candidate1_vote = candidate1_vote + 1

        #The total number of votes for candidate 2
        elif election_data[i][2] == unique_list[1]:
            candidate2_vote = candidate2_vote + 1

        #The total number of votes for candidate 3
        elif election_data[i][2] == unique_list[2]:
            candidate3_vote = candidate3_vote + 1
    votes = [candidate1_vote, candidate2_vote, candidate3_vote]
    
    # The percentage of votes each candidate won
    percent_candidate1 = format(candidate1_vote / total_votes * 100, ".3f")
    percent_candidate2 = format(candidate2_vote / total_votes * 100, ".3f")
    percent_candidate3 = format(candidate3_vote / total_votes * 100, ".3f")
    percents = [percent_candidate1, percent_candidate2, percent_candidate3]

    # Create a dictionary for candidate voting result
    vote_result = {0:unique_list,1:votes,2:percents}

    # The winner of the election based on popular vote  
    max_vote = max(votes)
   
    for i in range(2):     
        winner = []
        if vote_result[1][i] == max_vote:  
            winner = vote_result[0][i]

    # Print out the election results
    print(f"Election Results")
    print("------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"------------------------------")
    print(f"{unique_list[0]}: {percent_candidate1}% ({candidate1_vote})")
    print(f"{unique_list[1]}: {percent_candidate2}% ({candidate2_vote})")
    print(f"{unique_list[2]}: {percent_candidate3}% ({candidate3_vote})")
    print(f"------------------------------")
    print(f"Winner: {winner}")
    print(f"------------------------------")
    
    # Store results in text file
    with open("PyPoll/analysis/Output.txt", "w") as textfile:
        print(f"Election Results" +"\n",
              "------------------------------" +"\n",
              f"Total Votes: {total_votes}" +"\n",
              f"------------------------------" +"\n",
              f"{unique_list[0]}: {percent_candidate1}% ({candidate1_vote})" +"\n",
              f"{unique_list[1]}: {percent_candidate2}% ({candidate2_vote})" +"\n",
              f"{unique_list[2]}: {percent_candidate3}% ({candidate3_vote})" +"\n",
              "------------------------------" +"\n",
              f"Winner: {winner}" + "\n",
              "------------------------------" +"\n",
                 file = textfile)