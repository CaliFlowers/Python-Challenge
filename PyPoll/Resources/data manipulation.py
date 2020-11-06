import csv

with open('election_data.csv', 'rt') as f:
    csv_reader = csv.reader(f, skipinitialspace=False, quotechar="'")

    for line in csv_reader: 
     print (line)
     