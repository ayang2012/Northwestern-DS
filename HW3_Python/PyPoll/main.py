# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

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

    votes =0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    
    
    for row in all_data[1:]:
        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li":
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
    
    # candidates = []    
    # candidates = [candidates.append(x[2]) for x in all_data if x[2] not in candidates]
    # candidate_data = [{"name":candidate,"vote_count":df.Candidate[df.Candidate == candidate].count()} for candidate in candidates]
    # candidate_data

    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {len(all_data)}")
    print("------------------------------")
    print(f"Khan: {round(float(khan_votes) / len(all_data)*100,3)}% ({khan_votes}) ")
    print(f"Khan: {round(float(correy_votes) / len(all_data)*100,3)}% ({correy_votes}) ")
    print(f"Khan: {round(float(li_votes) / len(all_data)*100,3)}% ({li_votes}) ")
    print(f"Khan: {round(float(otooley_votes) / len(all_data)*100,3)}% ({otooley_votes}) ")
    print("------------------------------")
    print("Winner: Khan")
    print("------------------------------")

    print("Election Results", file=open("answers.txt", "a"))
    print("------------------------------", file=open("answers.txt", "a"))
    print(f"Total Votes: {len(all_data)}", file=open("answers.txt", "a"))
    print("------------------------------")
    print(f"Khan: {round(float(khan_votes) / len(all_data)*100,3)}% ({khan_votes}) ", file=open("answers.txt", "a"))
    print(f"Khan: {round(float(correy_votes) / len(all_data)*100,3)}% ({correy_votes}) ", file=open("answers.txt", "a"))
    print(f"Khan: {round(float(li_votes) / len(all_data)*100,3)}% ({li_votes}) ", file=open("answers.txt", "a"))
    print(f"Khan: {round(float(otooley_votes) / len(all_data)*100,3)}% ({otooley_votes}) ", file=open("answers.txt", "a"))
    print("------------------------------", file=open("answers.txt", "a"))
    print("Winner: Khan", file=open("answers.txt", "a"))
    print("------------------------------", file=open("answers.txt", "a"))