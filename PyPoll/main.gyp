#import modules needed for challenge
import os
import csv

#find the path to the election data
csvpath = os.path.join('Resources', 'election_data.csv')

#declare variables and lists needed to solve the challenge
vote_counter = 0
candidate_list = []
candidate_vote = []
percentages = []

#open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header label to iterate only through the needed row values
    csv_header = next(csvreader)

    #iterate through the rows to calculate vote_counter and add values to candidate_list
    for row in csvreader:
        #count up the total votes for each row in the CSV file
        vote_counter = vote_counter + 1
        
        #sets the current candidate equal to the current row
        current_candidate = row[2]

        #checks to see if the current candidate is in the candidate list yet
        if current_candidate in candidate_list:
            vote_index = candidate_list.index(current_candidate)
            candidate_vote[vote_index] = candidate_vote[vote_index] + 1
        
        #if the current candidate is not yet in the list, then append them and also start counting their total votes at 1
        else:
            candidate_list.append(current_candidate)
            candidate_vote.append(1)

    #set a placeholder value for the current highest amount of votes
    place_holder = candidate_vote[0]
    for vote in candidate_vote: 
        #calculates the percentage of total votes for each candidate
        percentages.append(round(((vote/vote_counter)*100),2))
        #if the next candidate has more votes then the current candidate, then declare them the winner
        if vote > place_holder:
            place_holder = candidate_vote[vote]
        else:
            winner_index = candidate_vote.index(place_holder)
            winner = candidate_list[winner_index]



  

