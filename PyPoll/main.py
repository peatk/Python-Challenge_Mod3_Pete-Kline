import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#variables
total_votes = []
candidate_vote_list = [] #should this be a dictionary instead?
candidate_vote_count = []

with open(election_csv, newline = "") as csv_file:
    reader = csv.reader(csv_file)
    remove_header = next(csv_file)
    #NEED to store header row

    for row in reader:
        total_votes.append = (row[1])
        candidate_vote_list.append = (row[2])
print(f'{len(total_votes)}')
print(f'{candidate_vote_list}')


#calculations
#print(f'{candidate_vote_list} and ({candidate_vote_count}/{total_votes})')


#1 - The total number of votes cast

#2 - A complete list of candidates who received votes

#3 - The percentage of votes each candidate won

#4 - The total number of votes each candidate won

#5 - The winner of the election based on popular vote