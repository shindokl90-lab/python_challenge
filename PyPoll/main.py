#import dependencies
import os
import csv

#read-in and set counter for PyPoll data
csvpath = os.path.join('..', 'PyPoll','Resources', 'election_data.csv')
totalvotes = 0

#Create candidates dictionary 

candidates = {}

#Print Headers
print("Election Results")
print("-----------------------")

#process csv of poll data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        totalvotes += 1
        cand = row [2]
        if cand in candidates.keys():
            candidates[cand] +=1
        else:
            candidates[cand] = 1
    
#Print PyPoll Information
print(f'Total Votes: {totalvotes:,}')
print("----------------------")

winner = ""
maxvote = 0

for key,value in candidates.items():
    percent = value /totalvotes
    print(f'{key}: {percent:.3%} ({value:,})')
    if value > maxvote:
        maxvote = value
        winner = key 

print("----------------------")
print(f'Winner : {winner}')
print("----------------------")

save_path = os.path.join('..', 'PyPoll', 'Analysis', 'output.txt')
with open(save_path, "w") as output:
    print("Election Results", file=output)
    print("----------------------", file=output)
    print(f'Total Votes: {totalvotes:,}', file=output)
    print("----------------------", file=output)
    for key,value in candidates.items():
        percent = value /totalvotes
    
        print(f'{key}: {percent:.3%} ({value:,})', file=output)
        if value > maxvote:
            maxvote = value
            winner = key 

    print("----------------------", file=output)
    print(f'Winner : {winner}', file=output)
    print("----------------------", file=output)