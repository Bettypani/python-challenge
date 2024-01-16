#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:15:30 2024

@author: bettypaniagua
"""

import os
import csv


csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
   # print(csvreader)

    csv_header = next(csvreader)
   # print(f'CSV Header: {csv_header}')
    
    
    votes = []
    #candidates_list = []
    unique_candidate = {}
    vote_count = []
    vote_percent = []
    
    for row in csvreader:
        votes.append(row[0])
        total_votes = len(votes)
      
        candidates_list=(row[2])
        if candidates_list not in unique_candidate:
            unique_candidate[candidates_list] = 1
        else:
            unique_candidate[candidates_list] = unique_candidate[candidates_list] + 1
    
    print(total_votes)
    for candidate, vote in unique_candidate.items():
        print(f'{candidate}, {vote},{round(vote/total_votes*100,3)}%')

    print(f'{max(unique_candidate,key=unique_candidate.get)}')