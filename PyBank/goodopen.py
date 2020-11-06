import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader( csvfile, delimiter=',', skipinitialspace='true')
     numbers = ()

    print (csvreader)


    for row in csvreader: 
        print (row[1])
        Numbers = For every item in Row[1]

    Avg = Avg(numbers)
    print(Avg)  

