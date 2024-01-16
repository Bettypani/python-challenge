#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:31:27 2024

@author: bettypaniagua
"""

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    
    months = []
    total_rev = []
    change_from_previous = []

    for row in csvreader:
        months.append(row[0])
        total_months = len(months)
        total_rev.append(int(row[1]))
        total_profit = sum(total_rev)
    
       
    for c in range(len(total_rev) - 1):
        change_from_previous.append(total_rev[c + 1] - total_rev[c])
        print(change_from_previous)
        average = sum(change_from_previous) / len(change_from_previous)
        
    greatest_increase = max(change_from_previous)
    greateast_increase_date = months[change_from_previous. index(greatest_increase) + 1]
    greatest_decrease = min(change_from_previous)
    greatest_decrease_date = months[change_from_previous. index(greatest_decrease) + 1]
        

    

print('Total Months: ' + str(total_months))
print('Total: ' + str(total_profit))
print('Average Change: ' + str(average))
print('Greatest Increase in Profits: ' + greateast_increase_date + ' $' + str(greatest_increase))
print('Greastest Decrease in Profits: ' + greatest_decrease_date + ' $' + str(greatest_decrease))

        

        


       
