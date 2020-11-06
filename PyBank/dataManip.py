import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader( csvfile, delimiter=',', skipinitialspace='true')
    

    print (csvreader)

for row in csvreader: 
        print (row)
