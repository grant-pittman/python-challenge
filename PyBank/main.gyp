#import modules needed for challenge
import os
import csv

#find the path to the buget data
csvpath = os.path.join('Resources', 'budget_data.csv')

#create list to store column values to use later in calculations 
total_months = []
total_profit = []
monthly_profit_change = []

#open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header label to iterate only through the needed row values
    csv_header = next(csvreader)

    #iterate through the rows to add values to lists total_months and total_profits
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #iterate through the rows to add calculated monthly profit chagnes to the list monthly_profit_change
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])





