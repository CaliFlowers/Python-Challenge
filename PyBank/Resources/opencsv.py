import os


import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:

    csv_reader = csv.reader( csvfile, delimiter=',', skipinitialspace='true')
    

    print (csvreader)

for line in csv_reader: 
        print (line)