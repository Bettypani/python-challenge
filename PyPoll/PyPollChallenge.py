#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:15:30 2024

@author: bettypaniagua
"""

import os
import csv

#iniciate csv path way
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
   # print(csvreader)

    csv_header = next(csvreader)
   # print(f'CSV Header: {csv_header}')
    
   #define variables 
    votes = []
    unique_candidate = {}
    vote_count = []
    vote_percent = []
    
    #iniciate loop for total votes
    for row in csvreader:
        votes.append(row[0])
        total_votes = len(votes)
      
      #if/else statement for finding the number of votes per candidate
        candidates_list=(row[2])
        if candidates_list not in unique_candidate:
            unique_candidate[candidates_list] = 1
        else:
            unique_candidate[candidates_list] = unique_candidate[candidates_list] + 1
    
   
    for candidate, vote in unique_candidate.items():
        print(f'{candidate}, {vote},{round(vote/total_votes*100,3)}%')

    print(f'{max(unique_candidate,key=unique_candidate.get)}')

    print('Election Results')
    print('------------------------------')
    print('Total Votes: ' + str(total_votes))
    print('------------------------------')
    print(f'{candidate}, {vote},{round(vote/total_votes*100,3)}%')
    print('------------------------------')
    print('Winner: ' +f'{max(unique_candidate,key=unique_candidate.get)}')
