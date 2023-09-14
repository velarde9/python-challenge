import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


# Variables
totalMonths = 0
netTotalAmount = 0
totalPeriodChanges = 0
averageChange = 0

greatestProfitIncrease = 0
greatestProfitIncreasePeriod = ""
greatestProfitDecrease = 0
greatestProfitDecreasePeriod = ""

previousPeriodProfitLoss = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    # Sample row data: ['Feb-17', '382539']
    for row in csvreader:
        rowNumber = csvreader.line_num
        # Increment total months by one
        totalMonths = totalMonths + 1
        # Add the profit/loss to the net total amount
        netTotalAmount = netTotalAmount + int(row[1])

        if rowNumber == 2:
            # For the frst row of data, temporarily set it to the greatest profits/losses variables
            greatestProfitIncrease = int(row[1])
            greatestProfitIncreasePeriod = row[0]
            greatestProfitDecrease = int(row[1])
            greatestProfitDecreasePeriod = row[0]
            previousPeriodProfitLoss = int(row[1])
        else:
            # Calculate the change between the current month period and the previous month period
            periodChange = int(row[1]) - previousPeriodProfitLoss
            # Add the calculated change to the total period changes
            totalPeriodChanges += periodChange
            previousPeriodProfitLoss = int(row[1])

            # If the current month period change is the greatest profit increase
            if periodChange > greatestProfitIncrease: 
                greatestProfitIncrease = periodChange
                greatestProfitIncreasePeriod = row[0]

            # If the current month period change is the greatest profit decrease
            if periodChange < greatestProfitDecrease: 
                greatestProfitDecrease = periodChange
                greatestProfitDecreasePeriod = row[0]

# Calculate the average change
averageChange = round(totalPeriodChanges / (totalMonths-1), 2)

output=(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${netTotalAmount}\n"
    f"Average Change: ${averageChange}\n"
    f"Greatest Increase in Profits: {greatestProfitIncreasePeriod} (${greatestProfitIncrease})\n"
    f"Greatest Decrease in Profits: {greatestProfitDecreasePeriod} (${greatestProfitDecrease})\n"
)

print(output)

output_textfile=open("analysis/output_textfile.txt", "w")
output_textfile.write(output)
output_textfile.close()
