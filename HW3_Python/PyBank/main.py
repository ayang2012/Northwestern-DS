# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    all_data = [row for row in csvreader]
    
    #---------------------------------------------------------------------------------        
    months = 1
    total = 0
    prev_month = 0
    total_diff = 0
    # Read each row of data after the header
    prev_month = all_data[0]
    prev_month = prev_month[1]

    total = float(prev_month)
   
    max_change = 0
    min_change = 0
    for row in all_data[1:]:
        months= months+1
        total = total + int(row[1])
        diff = int(row[1])-int(prev_month)
        total_diff = total_diff + diff
        prev_month = row[1]

        if diff > max_change:
            max_change = diff
            max_row = row

        if diff < min_change:
            min_change = diff
            min_row = row
   

    avg_change = round(float(total_diff)/(months-1), 0)
    print("Financial Analysis")
    print("--------------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest increase in profits: {max_row} {max_change}")
    print(f"Greatest decrease in profits: {min_row} {min_change}")

    # print("#-------------------------------------------------------------------------------")
    # print(all_data[0])
    # print(all_data[0][0])
    # print(all_data[0][1])

print("Financial Analysis", file=open("answers.txt", "a"))
print("--------------------------------------", file=open("answers.txt", "a"))
print(f"Total Months: {months}", file=open("answers.txt", "a"))
print(f"Total: ${total}", file=open("answers.txt", "a"))
print(f"Average Change: ${avg_change}", file=open("answers.txt", "a"))
print(f"Greatest increase in profits: {max_row} {max_change}", file=open("answers.txt", "a"))
print(f"Greatest decrease in profits: {min_row} {min_change}", file=open("answers.txt", "a"))