import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
ballot = []
votes = {}
win_votes = 0
winner = ""


with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    header = next(csvreader)
    
    for vote in csvreader:
        total_votes = total_votes +1
        candidate = vote[2]
        if candidate not in ballot:
            ballot.append(candidate) 
            votes[candidate] = 0
        votes[candidate] = votes[candidate] + 1


for candidates in votes:
    cvote  = votes.get(candidates)
    pvote = "{:.3%}".format(cvote/total_votes) 
    if cvote > win_votes:
        win_votes = cvote
        winner = candidates
  

print("Election Results")

print("Total Votes: " + str(total_votes))

for candidates in votes:
    print(candidates + ": " + str(cvote) + " " + str(pvote))


print("Winner:" + " "+ winner)

file_to_output = os.path.join("analysis", "election_analysis.txt")

with open(file_to_output, "w") as txt_file:

    txt_file.write("Election Results")

    txt_file.write('\n')

    txt_file.write("Total Votes: " + str(total_votes))
   
    txt_file.write('\n')

    txt_file.write(candidates + ": " + str(cvote) + " " + str(pvote))

    txt_file.write('\n')

    txt_file.write("Winner:" + " "+ winner)
