import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#variables

# set total vote count
total_votes = 0

#set list of candidates and counts
candidate_list = []
candidate_vote_count = {}


#set winning variables
#winner = ""
#winner_count = 0
#winner_percentage = 0 


with open(election_csv, newline = "") as election_file:
    reader = csv.reader(election_file)
    header = next(reader)
    #NEED to store header row

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

for x in candidate_vote_count:
    
    candidate_percent = (candidate_vote_count[x]/ total_votes)*100
   


print(f'{total_votes}') 
print(f'{candidate_list}')
print(f'{candidate_vote_count}')
print(f'{x} {candidate_percent}')


#1 - The total number of votes cast - DONE

#2 - A complete list of candidates who received votes - DONE

#3 - The percentage of votes each candidate won - DONE
 
#4 - The total number of votes each candidate won- DONE, prints with candidate list

#5 - The winner of the election based on popular vote - if statement to compare - and use find max vote


#print(f'{candidate_percent}')