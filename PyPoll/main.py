import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open('election_data.csv', 'rt') as f:
    csv_reader = csv.reader(f, skipinitialspace=True, quotechar="'")
    next(csv_reader)

    
    for line in csv_reader:
        print(line)
    
        vote_percentage={}
        votes = 0
        count = {}
        vote_count = {}
        name = line[2]
        most_votes = 0
        
        for line in csv_reader:
            
            votes +=1 
        if name not in vote_count: #3b. Line 22 counts votes in the data associated with a candidate's name 
            
            vote_count[name] = 1 
        else: 
            vote_count[name] +=1
        print(vote_count) #3c.Line 27 is atest of whether the code is functional up to this point. 

        for name in vote_count: 

            vote_percentage[name] = round(((vote_count[name]*100)/votes),2) #4a. Line 33 is a formula using the variables listed/obtained in 1-3.
            print(vote_percentage) #4b. Line 34 checks whether 4a. works as intended.

            if vote_count[name]>most_votes:
                most_votes = vote_count[name]
                winner = name
        
    print("Election Results")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(f"Total Votes: (votes)")
    for name in vote_count:
        print("f{name}:(vote_percentage[name])% ((vote_count[name]))")
    print("xxxxxxxxxxxxxxxxxxxxxxx")
    print("WINNER:  {winner}")

    output_path= os.path.join('..','Analysis','Analysis_of_Basic_Electoral_Data_with_Python.txt')
    with open(output_path, 'w') as text:
        text.write("Election Results")
        text.write(("xxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        text.write(f"Total Votes: (votes)\n") 
    for name in vote_count:
        text.write(f"{vote_count[name]} (vote_percentage[name])% (vote_count[name])\n")
        text.write("xxxxxxxxxxxxxxxxxxxxxxx\n")
        text.write(("WINNER: {winner}")