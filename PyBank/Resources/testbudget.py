import os

import csv
#1. Open csv file
with open('budget_data.csv', 'rt') as f:
    csv_reader = csv.reader(f, skipinitialspace=True, quotechar="'")
    next(csv_reader)
#2 calculate intermediate values for each row n csv. 
    print (csv_reader)
    months=0 #2a. defines variables outside of the for loop
    lastmonthprofit=0
    totalprofit = 0
    totalchange = 0
    greatestincrease = -999999          #3c. Lines 29-32 define variables for the final analysis
    greatestdecrease = 999999           
    GImonth=""
    GDmonth=""
    for line in csv_reader: #2b. starts a for loop to calculate primary values from data
        print(line) #2c. this line tests whether csv file is still linked to code
        months+=1
        revenue = int(line[1])
        currentmonth = str(line [0]) #2d. Lines 16-19 draw data directly from the csv file. This will be used to perform the analysis. 
        currentprofit = revenue      
        monthlychange = revenue - lastmonthprofit
        totalprofit = totalprofit + revenue
        lastmonthprofit=revenue #2e. Lines 19-22 use the data retrieved from 2c and 2d to calculate intermediate values
        totalchange = totalchange + monthlychange #2f. Lines 21 and 23 perform second-order calculations for further analysis. 
        print(currentmonth) #2g.this line tests whether the calculation of intermediate values was succesfully performed

#3. With intermediate values on hand, calculate the final values required for report. 
average_change = totalchange/months #3a. This ine uses intermediate alues to obtain a final value
print(average_change)               #3b. This line tests whether the calculation in 3a was performed correctly. 

for line in csv_reader:     #3d. Line 33 creates a second loop to obtain the greatest increase and decrease in revenue between months in the dataset. 

    if monthlychange > greatestincrease:

                greatestincrease = monthlychange
                GImonth = currentmonth
                print(GImonth)

    elif monthlychange< greatestdecrease:

                greatestdecrease = monthlychange
                GDmonth = currentmonth
                print (GDmonth)

print("Financial Analysis")
print("xxxxxxxxxxxxxxxx")
print(f"Total Months:"+ str(months)+ "months")
print(f"Total Profits:"+ str(totalprofit))
print(f"Average Change:"+str(average_change))
print(f"Greatest Increase in Profits:"+ GImonth+ str(greatestincrease))
print(f"GreatestDecreaseinProfits:"+ GDmonth + str(greatestdecrease))


        


        