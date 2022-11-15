import csv
import os

#Declaring variables
months = []
amount = []
change = []
index_increase=0
increase=0
index_decrease=0
decrease=0

#File Path
csvpath = os.path.join("Pybank/Resources/budget_data.csv")
txtwrite = os.path.join("PyBank/analysis/financial_analysis.txt")

#Read file and open financial data
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    #Adding months into list
    for row in csvreader:
        amount.append(int(row[1]))
        months.append(row[0])
        total_months = len(months)

#Find the greatest increase and decrese in profits
for index in range(len(amount)-1):
    value = amount[index+1]-amount[index]
    if value >= increase:
        increase=value
        index_increase = index+1
    if value <= decrease:
        decrease=value
        index_decrease = index+1

    change.append(value)

#Print to terminal and export to txt file
with open(txtwrite, "w") as txt_file:
    financial_analysis = (f'''
    Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${sum(amount)}
    Average Change: ${round(sum(change)/len(change),2)}
    Greatest Increase in Profits: {months[index_increase]}, $({increase})
    Greatest Decrease in Profits: {months[index_decrease]}, $({decrease})
    ''')
    print(financial_analysis)
    txt_file.write(financial_analysis)