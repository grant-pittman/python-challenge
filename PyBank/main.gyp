#import modules needed for challenge
import os
import csv

#find the path to the buget data
csvpath = os.path.join('Resources', 'budget_data.csv')

#create list to store column values to use later in calculations 
total_months = []
total_revenue = []
monthly_profit_change = []

#open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header label to iterate only through the needed row values
    csv_header = next(csvreader)

    #iterate through the rows to add values to lists total_months and total_revenues
    for row in csvreader:
        total_months.append(row[0])
        total_revenue.append(int(row[1]))

    #iterate through the rows to add calculated monthly profit chagnes to the list monthly_profit_change
    for i in range(len(total_revenue)-1):
        monthly_profit_change.append(total_revenue[i+1]-total_revenue[i])

#min/max functions determine the largest and smallest value in the list monthly_profit_change
greatest_increase = max(monthly_profit_change)
greatest_decrease = min(monthly_profit_change)

#referencing the index position in monthly profit changes to find the position of the month in question
greatest_increase_month = total_months[(monthly_profit_change.index(greatest_increase)+1)]
greatest_decrease_month = total_months[(monthly_profit_change.index(greatest_decrease)+1)]

#print out the financial statement
print("Financial Analysis")
print("_________________________")
print(f"Total Months: {len(total_months)}")
print(f"Total Profit: ${sum(total_revenue)}")
print(f"Average Revenue Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits:{greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits:{greatest_decrease_month} (${greatest_decrease})")

# Open the file using "write" mode. Specify the variable to hold the contents
output_path = os.path.join("output", "financial_analysis.txt")

with open(output_path,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_revenue)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits:{greatest_increase_month} (${greatest_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits:{greatest_decrease_month} (${greatest_decrease})")