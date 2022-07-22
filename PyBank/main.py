import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

months = 1
accumulate = 0
p_lchange = []
max_date = ""
min_date = ""

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    first_row = next(csvreader)
    original = int(first_row[1])
    new = int(first_row[1])
    accumulate = int(first_row[1])
    max_pl = int(first_row[1])
    min_pl = int(first_row[1])
    for row in csvreader:
        months += 1
        accumulate = accumulate + int(row[1])
        new =  int(row[1]) - original
        p_lchange.append(new) 
        original = int(row[1])
        if new > max_pl:
            max_pl = new
            max_date = row[0]
            new = 0
        elif new < min_pl:
            min_pl = new
            min_date = row[0]
            new = 0

average = ((sum(p_lchange)) / (months -1))

print("Total Months: " + str(months))

print("Total: " + " " + ("${:.2f}".format(accumulate)))

print("Average Change: " + ("${:.2f}".format(average)))

print("Greatest Decrease in Profits: " + (min_date) + " " + ("${:.2f}".format(min(p_lchange))))

print("Greatest Increase in Profits: " + (max_date)  + " " + ("${:.2f}".format(max(p_lchange))))

file_to_output = os.path.join("analysis", "profit_analysis.txt")

with open(file_to_output, "w") as txt_file:

    txt_file.write("Total Months: " + str(months))
    
    txt_file.write('\n')

    txt_file.write("Total: " + " " + ("${:.2f}".format(accumulate)))

    txt_file.write('\n')

    txt_file.write("Average Change: " + ("${:.2f}".format(average)))

    txt_file.write('\n')

    txt_file.write("Greatest Decrease in Profits: " + (min_date) + " " + ("${:.2f}".format(min(p_lchange))))

    txt_file.write('\n')
    
    txt_file.write("Greatest Increase in Profits: " + (max_date)  + " " + ("${:.2f}".format(max(p_lchange))))