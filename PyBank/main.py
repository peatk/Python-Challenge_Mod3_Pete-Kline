import os
import csv

#Set path for csv file
BUDGET_CSV_PATH = os.path.join("Resources", "budget_data.csv")
#path from tutor - Kourt
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#variables
total_month_count = 0
total_profit = 0 
monthly_change = []
month_list = []
previous_profit = 0 

#open csv file and read data
with open(BUDGET_CSV_PATH) as budget_file:
    reader = csv.reader(budget_file)
    header = next(reader)
   
    #Set for loop to read through all the data
    for row in reader:
        
        #Count total of months
        total_month_count = total_month_count + 1
        
        month_list.append(row[0])
        current_profit = int(row[1])

        #calc total profit for
        total_profit = total_profit + current_profit 

        #calc change in each month
        total_change = current_profit - previous_profit
        previous_profit = current_profit

        #append my list of change with my total month calc
        monthly_change.append(total_change)

        #find the max and min from monthly change list
        great_increase = max(monthly_change)
        great_decrease = min(monthly_change)

    #remove the first value (1088983 becasue it will throw off average calc)
    monthly_change.pop(0)


#print my values
    print(f'Financial Analysis')
    print(f'----------------------------------')
    print(f'Total Months: {total_month_count}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: ${sum(monthly_change) / len(monthly_change)}') 
    print(f'Greatest Increase in Profits:{month_list[monthly_change.index(max(monthly_change))+1]} $({great_increase})')
    print(f'Greatest Decrease in Profits:{month_list[monthly_change.index(min(monthly_change))+1]} $({great_decrease})')




#1 - Total number of months included in the dataset - DONE!

#2 - Calculate the total profit / loss in column 2 (sum the amounts) - DONE
 
#3 - What is the average change over time? - DONE!!!!

#4 - What is the largest month? DONE

#5 - What is the lowest month? DONE
  
#6 - Create new file and print all the data from above




#current change = this month - last month
#indexes get things out of lists 
#print(current_month, current_profit)
# #print(type(current_month), type(current_profit))
#print(f'{len(total_month_count)-1}') # i think this is pulling a "" value and counting 1 extra cell, using -1 to get the correct number
#print(f'{total_revenue}')
#total_revenue = row[1] - How to 
#print(type(row))
#greatest_increase = max(total_revenue)
#greatest_decrease = min(total_revenue)
#print(f'{greatest_increase} and no') #pulling 99,841 as largest, should be 1,141,840
#print(f'{greatest_decrease} and yes') #pulling 0 or blank as smallest 
