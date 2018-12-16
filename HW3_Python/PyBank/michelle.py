# PyBank Homework. Analyze:

# HW The total number of months included in the dataset

#read_cvs.py class
# First we'll import the os module. The os module means that we can create file paths across operating systems. 
# This module is especially important if you want to make your programs platform-independent. os figures out which sysytem on and runs based on that
# i.e. it allows the program to be written such that it will run on Linux as well as Windows without any problems and without requiring changes
import os

# Module (aka toolbox that has a tool) for reading CSV files
import csv

#HELP. do wn directory? The path join starts from where this file that I am typing in is located 
csvpath = os.path.join('Resources', 'budget_data.csv')

# Using class Method 2: Improved Reading using CSV module
# "with this file path open this file as a csv"
# using newline to accomate reading across all os' some interpret them differently

# ML FYI, this was what was in class. mine did not run when I had new line: with open(csvpath, newline='') as csvfile:
with open(csvpath) as csvfile:


    # CSV reader specifies module, method/fxn, file the variable is taking in, delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Best practice to check to see if reader worked by printing. Will know by seeing "cvs.reader object at...blah, blah, blah. Then # out. 
    # print(csvreader)

    # Read the header row first (skip this step if there is no header. Print it the header after the hard coded text CSV header.)
    # HELP: don't really get next and what is happening here. 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    # Look for each row of data. Do something if the desired call is found; do somethign else if not
    # Read each row of data , iteratate over something 
    
     
   # The total net amount of "Profit/Losses" over the entire period

    for row in csvreader:
      Date = row[0]
      #This tells the computer to look at the second column 
      Profit_Losses = row[1]

      Total = 0
      for Profit_Losses in range(5):
        Total = Total + Profit_Losses

print("The End")
# The total net amount of "Proft/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# WIP - both analysis to terminal?
print("The End")