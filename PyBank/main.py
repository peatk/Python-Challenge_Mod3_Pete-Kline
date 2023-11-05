import os
import csv

#Set path for csv file
BUDGET_CSV_PATH = os.path.join("Resources", "budget_data.csv")
SAVE_PATH = os.path.join("Analysis", "budget_data.txt")

#path from tutor - Kourt
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Set my variables to 0 
total_month_count = 0
total_profit = 0 
previous_profit = 0 

#Create lists to host data
monthly_change = []
month_list = []

#Open csv file and read csv data
with open(BUDGET_CSV_PATH) as budget_file:
    reader = csv.reader(budget_file)
    header = next(reader)
   
    #Set for loop to read through all the data
    for row in reader:
        
        #Count total of months
        total_month_count = total_month_count + 1
        
        month_list.append(row[0])
        current_profit = int(row[1])

        #Calc total profit for
        total_profit = total_profit + current_profit 

        #calc change in each month
        total_change = current_profit - previous_profit
        previous_profit = current_profit

        #Add calculated values to list
        monthly_change.append(total_change)

        #Find the max and min from monthly change list
        great_increase = max(monthly_change)
        great_decrease = min(monthly_change)

    #Remove the first value (1088983 becasue it will throw off average calc)
    monthly_change.pop(0)


#Create variable to print all data

data_to_print =(f'Financial Analysis'
f'\n----------------------------------'
f'\nTotal Months: {total_month_count}'
f'\nTotal: ${total_profit}'
f'\nAverage Change: ${sum(monthly_change) / len(monthly_change)}'
f'\nGreatest Increase in Profits:{month_list[monthly_change.index(max(monthly_change))+1]} $({great_increase})'
f'\nGreatest Decrease in Profits:{month_list[monthly_change.index(min(monthly_change))+1]} $({great_decrease})')

print(data_to_print)

#Print analysis to text file
with open(SAVE_PATH, 'w') as txt_file:
    txt_file.write(data_to_print)
