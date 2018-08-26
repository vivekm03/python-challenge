# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:33:35 2018

@author: vivek
"""
#Import dependencies
import os
import csv
import sys

# Create path variable
election_csv_path = r"C:\Users\vivek\Desktop\RutgersDSBootcamp\python-challenge\Vote-Counting\election_data.csv"

#Initialize two dictionaries and total votes variable
cand_dict={}
cand_pct={}
tot_votes=0

#Open file and create CSV wrappers
with open(election_csv_path) as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    header=next(csvfile)
    print(f"Header row: {header}")
        
    for row in csv_reader:
        #Variable for summing total votes
        tot_votes += 1
        #Variable to store name of candidate
        candidate=row[2]
        #Initialize for new candidate
        if candidate not in cand_dict:
            cand_dict[candidate]=0
        #Sum votes for each candidate and store in dictionary
        cand_dict[candidate]+=1
    #Get percentages for each candidate and store in dictionary
    for candidate in cand_dict:
        cand_pct[candidate]=str(round(cand_dict[candidate]*100/tot_votes, 3)) + "% (" + str(cand_dict[candidate])+ ")"
    #Find winner using key of maximum votes from dictionary and create winner text
    winner_text="Winner: " + str(max(cand_dict, key=cand_dict.get))
    
#Print Results
    print("Election Results")
    print("__________________________")
    print(f"Total Votes: {tot_votes}")
    print("__________________________")
    for candidate in cand_dict:
        print (candidate + ":" + cand_pct[candidate])
    print("__________________________")
    print (winner_text)
    print("__________________________")

#Print Results to .txt file   
    sys.stdout=open('output.txt','wt')
    print("Election Results")
    print("__________________________")
    print(f"Total Votes: {tot_votes}")
    print("__________________________")
    for candidate in cand_dict:
        print (candidate + ":" + cand_pct[candidate])
    print("__________________________")
    print (winner_text)
    print("__________________________")