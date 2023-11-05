import os
import csv

#Set path for files
ELECTION_CSV_PATH = os.path.join("Resources", "election_data.csv")
SAVE_PATH = os.path.join("Analysis", "election_data.txt")

#Path from tutor - Kourt
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Set variables, list and dicts
total_votes = 0

#Candidate data
candidate_list = []
candidate_vote_count = {}

#Winner data
winner = ""
winner_count = 0
winner_percentage = 0 

#Open csv and run the code below
with open(ELECTION_CSV_PATH) as election_file:
    reader = csv.reader(election_file)
    header = next(reader)
    
    #Loop through rows of data
    for row in reader:
        
        #Add up total votes
        total_votes = total_votes + 1

        #Candidate data indexes row 2 (but its really a column...)
        candidate_name = row[2]

        #If a name is note in the candidate list, append the list and tally vote
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_vote_count[candidate_name] = 0
        
        #End vote total
        candidate_vote_count[candidate_name] += 1 

#Create text filed and print analysis to text file
with open(SAVE_PATH, 'w') as txt_file:
    
    #Election results
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

    #For loop goes through each candidate and prints data assoicated with each candidate
    for each_candidate in candidate_vote_count:
        candidate_vote = (candidate_vote_count[each_candidate])
        candidate_percent = float(candidate_vote) / float(total_votes)*100
        if candidate_vote > winner_count:
            winner_count = candidate_vote
            winner = each_candidate
        
        #This print needs to be inside of the for loop so that it prints all 3 candidates results (if outside, will only print 1 candidate)
        voter_output = (f'{each_candidate} {candidate_percent:.3f}% ({candidate_vote})\n')
        print(voter_output)  
        txt_file.write(voter_output)
    
    #Election results <continued>
    print_data_2 =(f'\n'
    f'--------------------------'
    f'\n'
    f'Winner: {winner}')
    print(print_data_2)
    txt_file.write(print_data_2)
