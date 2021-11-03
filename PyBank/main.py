#pybank script

#import dependencies
import os
import csv

#read csv
csvpath = os.path.join('..', "PyBank", "Resources", "budget_data.csv")

print("Financial Analysis")
print("-------------------------")

total = 0 
rowcount = 0 
change_from_previous = []
months = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    header = next(csvreader)
    previous_revenue = 0

    for row in csvreader: 
        rowcount += 1
        total += int(row[1])
        change_from_previous.append(int(row[1])-previous_revenue)
        months.append(row[0])
        previous_revenue = int(row[1])

    print(f'Total Months: {rowcount}')
    print(f'Total: ${total:,}')

    print(f'Average Change: ${sum(change_from_previous[1:])/(len(change_from_previous)-1):,.2f}')
    
    max = max(change_from_previous)
    min = min(change_from_previous)

    print (f'Greatest Increase in Profits: {months[change_from_previous.index(max)]} (${max:,})')
    print (f'Greatest Decrease in Profits: {months[change_from_previous.index(min)]} (${min:,})')

#save and print to text file
save_path = os.path.join('..', 'PyBank', 'Analysis', 'output.txt')
with open(save_path, "w") as output: 
    print("Financial Analysis", file=output)
    print("-------------------------", file=output)
    print(f'Total Months: {rowcount}', file=output)
    print(f'Total: ${total:,}', file=output)
    print(f'Average Change: ${sum(change_from_previous[1:])/(len(change_from_previous)-1):,.2f}', file=output)
    print (f'Greatest Increase in Profits: {months[change_from_previous.index(max)]} (${max:,})', file=output)
    print (f'Greatest Decrease in Profits: {months[change_from_previous.index(min)]} (${min:})', file=output)


