#import modules needed for challenge
import os
import csv

#find the path to the buget data
csvpath = os.path.join('Resources', 'election_data.csv')

#declare variables and lists needed to solve the challenge
vote_counter = 0
candidate_list = []
candidate_votes = [0,0,0,0]
percentages = []

#open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header label to iterate only through the needed row values
    csv_header = next(csvreader)

    #iterate through the rows to calculate vote_counter and add values to candidate_list
    for row in csvreader:
        vote_counter = vote_counter + 1
        candidate_list.append(row[2])
    
    #change candidate_list to a set to reduce to only unique values
    candidate_set = set(candidate_list)

#change the set back into a simplified list
new_candidate_list = list(candidate_set)

#open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header label to iterate only through the needed row values
    csv_header = next(csvreader)

    #iterate through the rows to tally the votes for each candidate 
    for row in csvreader:
        if row[2] == new_candidate_list[0]:
            candidate_votes[0] = candidate_votes[0] + 1

        elif row[2] == new_candidate_list[1]:
            candidate_votes[1] = candidate_votes[1] + 1
        
        elif row[2] == new_candidate_list[2]:
            candidate_votes[2] = candidate_votes[2] + 1
            
        elif row[2] == new_candidate_list[3]:
            candidate_votes[3] = candidate_votes[3] + 1

#iterate through candidate votes to calculate the percentage of total votes for each candidate 
for vote in candidate_votes: 
    percentages.append(round(((vote/vote_counter)*100),2))

#below works but missing percentages
results = {new_candidate_list[i]:candidate_votes[i] for i in range(len(new_candidate_list))}

#this is not working yet. I think it's the right way to solve the problem, but I have another less pretty solution below. 
# results = {
#     new_candidate_list[i]: {
#         candidate_votes[i] for i in range(len(new_candidate_list)),
#         percentages[i] for i in range(len(new_candidate_list))
#         } 
# }

#Prints the Output of the Election Results
print("Election Results")
print("________________________")
print(f'Total Votes: {vote_counter}')
print("________________________")
print(str(new_candidate_list[0]) + ": " + str(percentages [0]) + "%" + " (" + str(candidate_votes [0]) + ")")
print(str(new_candidate_list[1]) + ": " + str(percentages [1]) + "%" + " (" + str(candidate_votes [1]) + ")")
print(str(new_candidate_list[2]) + ": " + str(percentages [2]) + "%" + " (" + str(candidate_votes [2]) + ")")
print(str(new_candidate_list[3]) + ": " + str(percentages [3]) + "%" + " (" + str(candidate_votes [3]) + ")")
print("________________________")
print("Winner: " + str(new_candidate_list[candidate_votes.index(max(candidate_votes))]))
print("________________________")

output_path = os.path.join("output", "election_results.txt")

with open(output_path,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Election Results")
    file.write("\n")
    file.write(f'Total Votes: {vote_counter}')
    file.write("\n")
    file.write("________________________")
    file.write("\n")
    file.write(str(new_candidate_list[0]) + ": " + str(percentages [0]) + "%" + " (" + str(candidate_votes [0]) + ")")
    file.write("\n")
    file.write(str(new_candidate_list[1]) + ": " + str(percentages [1]) + "%" + " (" + str(candidate_votes [1]) + ")")
    file.write("\n")
    file.write(str(new_candidate_list[2]) + ": " + str(percentages [2]) + "%" + " (" + str(candidate_votes [2]) + ")")
    file.write("\n")
    file.write(str(new_candidate_list[3]) + ": " + str(percentages [3]) + "%" + " (" + str(candidate_votes [3]) + ")")   
    file.write("\n")
    file.write("________________________")
    file.write("\n")
    file.write("Winner: " + str(new_candidate_list[candidate_votes.index(max(candidate_votes))]))