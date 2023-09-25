# Modules
import os
import csv

# Set path for csv file
csvpath = os.path.join("PyBank/Resources/budget_data.csv")

# Open csv file 
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # Read the csv header row first
    csvheader = next(csvreader)
 
    # Loop through the data
    bank_data = []
    for row in csvreader:
        bank_data.append(row)
    
    # Calculate the total number of months:
    total_month = len(bank_data)
    
    # Calculate the net total amount of "Profit/Losses":
    profit = []
    for i in range(len(bank_data)):
        row_profit = int(bank_data[i][1])
        profit.append(row_profit)
    total_profit = sum(profit)
    
    # The changes in "Profit/Losses" over the entire period, 
    # and then the average of those changes:
    total_change = 0
    for i in range(len(bank_data)-1):
        change = profit[i+1]-profit[i]
        total_change = total_change + change
    average_change = format(total_change / (len(bank_data)-1),".2f")

    # The greatest increase in profits (date and amount) over the entire period
    max_change = 0
    for i in range(len(bank_data)-1):
        change = profit[i+1]-profit[i]
        if change > max_change:
            max_change = change
            max_month = bank_data[i+1][0]
   
    # The greatest decrease in profits (date and amount) over the entire period
    min_change = 0
    for i in range(len(bank_data)-1):
        change = profit[i+1]-profit[i]
        if change < min_change:
            min_change = change
            min_month = bank_data[i+1][0]

    # Print out the bank's analysis report:
    print(f"Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

    with open("PyBank/analysis/Output.txt","w") as textfile:
        print(f"Financial Analysis" + "\n",
              "-----------------------------" +"\n",
              f"Total Months: {total_month}"+"\n",
              f"Total: ${total_profit}"+"\n",
              f"Average Change: ${average_change}"+"\n",
              f"Greatest Increase in Profits: {max_month} (${max_change})"+"\n",
              f"Greatest Decrease in Profits: {min_month} (${min_change})",
                file = textfile)