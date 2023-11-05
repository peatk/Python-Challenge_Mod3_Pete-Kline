import os
import csv

ELECTION_CSV_PATH = os.path.join("Resources", "election_data.csv")
SAVE_PATH = os.path.join("Analysis", "election_data.txt")
#path from tutor - Kourt
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# set total vote count
total_votes = 0

#set list of candidates and counts
candidate_list = []
candidate_vote_count = {}

#set winning variables
winner = ""
winner_count = 0
winner_percentage = 0 

with open(ELECTION_CSV_PATH) as election_file:
    reader = csv.reader(election_file)
    header = next(reader)
    
    #loop through rows of data
    for row in reader:
        
        #add up total votes
        total_votes = total_votes + 1

        #set candidate name to row 2
        candidate_name = row[2]

        #if a name is note in the candidate list, append the list and tally vote
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_vote_count[candidate_name] = 0

        candidate_vote_count[candidate_name] += 1 

#Print analysis to text file
with open(SAVE_PATH, 'w') as txt_file:
    print_data_1 =(f'Election Results'
    f'\n'
    f'\n--------------------------'
    f'\n'
    f'\nTotal votes: {total_votes}'
    f'\n'
    f'\n--------------------------'
    f'\n')
    txt_file.write(print_data_1)
    print(print_data_1)

    for each_candidate in candidate_vote_count:
        candidate_vote = (candidate_vote_count[each_candidate])
        candidate_percent = float(candidate_vote) / float(total_votes)*100
        if candidate_vote > winner_count:
            winner_count = candidate_vote
            winner = each_candidate
        voter_output = (f'{each_candidate} {candidate_percent:.3f}% ({candidate_vote})\n')
        print(voter_output)  
        txt_file.write(voter_output)

    print_data_2 =(f'\n'
    f'--------------------------'
    f'\n'
    f'Winner: {winner}')
    print(print_data_2)
    txt_file.write(print_data_2)
