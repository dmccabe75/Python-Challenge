import os
import csv
Total_Margin = 0
Total_Months = 0
Previous_Value = 0
Changes = []
date = []


budget_data = os.path.join('budget_data.csv')
with open(budget_data, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
   for row in csvreader:
    Total_Months += 1
    Total_Margin += int(row[1])
    Current_Value = row[1]
    change = (int(Current_Value) - int(Previous_Value))
    Changes.append(change)
    date.append(row[0])
    Previous_Value = row[1]
Changes=Changes[1:]
max_changes = (max(Changes), str(date[Changes.index(max(Changes))+1]))
min_changes = (min(Changes), str(date[Changes.index(min(Changes))+1]))

print("Financial Analysis")
print("-----------------------------------------------")
print("Total Months:", Total_Months) 
print('Total Margin: ${:,}'.format(Total_Margin))
print('Avg Change: ${:,}'.format(round(sum(Changes)/len(Changes),2)))
print('Greatest Revenue Increase: ${:,}'.format(max(Changes)) + " - " + str(date[Changes.index(max(Changes))+1]))
print('Greatest Revenue Decrease: ${:,}'.format(min(Changes)) + " - " + str(date[Changes.index(min(Changes))+1]))
print("-----------------------------------------------")

Final_Analysis = (Total_Months, Total_Margin, round(sum(Changes)/len(Changes),2), str(max(Changes)) + str(date[Changes.index(max(Changes))+1]), str(min(Changes)) + str(date[Changes.index(min(Changes))+1]))

output_file = os.path.join("pybank_output.txt")
with open(output_file, 'w') as text_file:
    writer = csv.writer(text_file)
    writer.writerow(Final_Analysis)
    
