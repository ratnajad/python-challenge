import os
import csv
file = "Resources/budget_data.csv"
with open(file) as csvfile:
        data = csv.DictReader(csvfile)
        countmonths = 0
        sumprofits_losses = 0
        changes = []
        change_dates =[]
        previous_profloss = 0
        firsttime = 0
        #Find total number of months in dataset
        #Find total amount of "Profit/Losses" in entire period
        for row in data:
                sumprofits_losses = sumprofits_losses + int(row['Profit/Losses'])
                countmonths = countmonths + 1
                if firsttime == 0:
                        previous_profloss = int(row['Profit/Losses'])
                        firsttime = 1
                else:
                        changes.append(int(row['Profit/Losses']) - previous_profloss)
                        change_dates.append(row['Date'])
                        previous_profloss = int(row['Profit/Losses'])

        #Calculate changes in "Profits/Losses" over the entire period and find avg
        sum = 0
        count = 0
        largestincrease = changes[0]
        largestdecrease = changes[0]
        largestincreaseindex = 0
        largestdecreaseindex = 0
        for difference in changes:
                sum = sum + difference
                if difference > largestincrease:
                        largestincrease = difference
                        largestincreaseindex = count
                if difference < largestdecrease:
                        largestdecrease = difference
                        largestdecreaseindex = count
                count = count + 1
        #find average change
        average = sum / len(changes)

output_string = (
        f'Financial Analysis\n'
        f'----------------------------------\n'
        f'Total Months: {countmonths}\n'
        f'Total: ${sumprofits_losses}\n'
        f'Average Change: ${average}\n'
        f'Greatest Increase in Profits: {(change_dates[largestincreaseindex])} (${largestincrease})\n'
        f'Greatest Decrease in Profits: {(change_dates[largestdecreaseindex])} (${largestdecrease})\n'
)
with open('analysis/output1.txt', "w") as txt_file:
        txt_file.write(output_string)
print(output_string)     