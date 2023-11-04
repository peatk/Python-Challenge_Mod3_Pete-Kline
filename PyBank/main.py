import os
import csv

#Set path for csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

#variables
total_months = []
total_revenue = [] 
average_change = 0

#open csv file and read data
with open(budget_csv, newline = "") as csv_file:
    reader = csv.reader(csv_file)
    remove_header = next(csv_file)
    #NEED to store header row too
    
    for row in reader:
        total_revenue.append(row[1])
        total_months.append(row[0])

    greatest_increase = max(total_revenue)
    greatest_decrease = min(total_revenue)


print(f'{len(total_months)-1}') # i think this is pulling a "" value and counting 1 extra cell, using -1 to get the correct number
print(f'{total_revenue}')
print(f'{greatest_increase} and no') #pulling 99,841 as largest, should be 1,141,840
print(f'{greatest_decrease} and yes') #pulling 0 or blank as smallest 

#1 - Total number of months included in the dataset - sort of done

#2 - Calculate the total profit / loss in column 2 (sum the amounts) - sort of done
 
#3 - What is the average change over time? - NEED HELP WITH ENTIRELY

#4 - What is the largest month? - is this pulling correctly?

#5 - What is the lowest month?
  
#6 - Create new file and print all the data from above
