#import modules needed for challenge
import os
import csv

#find the path to the buget data
csvpath = os.path.join('Resources', 'election_data.csv')

vote_counter = 0
candidate_list = []

#open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header label to iterate only through the needed row values
    csv_header = next(csvreader)

    #iterate through the rows to add values to lists total_months and total_profits
    for row in csvreader:
        vote_counter = vote_counter + 1
        candidate_list.append(row[2])
    
candidate_set = set(candidate_list)


print(f'Total Votes: {vote_counter}')
print(f'The candidates are ')
print(candidate_set)




 