# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:22:47 2018

@author: vivek
"""
#Import dependencies
import os
import csv
import sys

# Create path variable
budget_csv_path=r"C:\Users\vivek\Desktop\RutgersDSBootcamp\python-challenge\Revenue\budget_data.csv"

#Initialize variables
i=0
sum_pl=0
chg_pl=0

#Initialize lists for 1)storing change in profit and 2) storing the month of change
chg=[]
month=[]

#Open file and create CSV wrappers
with open(budget_csv_path,newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    header=next(csvfile)

    for row in csv_reader:
        #Variable for counting total months
        i=i+1
        #Variable for sum of profit and loss(PL)
        sum_pl=sum_pl + int(row[1])
        # Calculate change from second row and create list of changes
        if i>1:
            chg_pl=int(row[1])-chg_pl
            chg.append(chg_pl)
            #Create list of the months
            month.append(row[0])
            chg_pl=int(row[1])
        #for first row we store value of PL to start calculation of change
        elif i == 1:
            chg_pl=int(row[1])

#Create summary variable for printing
    chg_sum=sum(chg)
    avg_chg=round(chg_sum/(i-1),2)
    max_chg=max(chg)
    max_month=month[chg.index(max_chg)]
    min_chg=min(chg)
    min_month=month[chg.index(min_chg)]

#Output to console
    print( f"Financial Analysis\n--------------------\nTotal Months: {i}" )
    print( f"Total: ${sum_pl}\nAverage Change: ${avg_chg}" )
    print( f"Greatest Increase in Profits: {max_month} ( ${max_chg} )" )
    print( f"Greatest Decrease in Profits: {min_month} ( ${min_chg} )" )
    
#Output to .txt file
    sys.stdout=open('output.txt','wt')
    print( f"Financial Analysis\n--------------------\nTotal Months: {i}" )
    print( f"Total: ${sum_pl}\nAverage Change: ${avg_chg}" )
    print( f"Greatest Increase in Profits: {max_month} ( ${max_chg} )" )
    print( f"Greatest Decrease in Profits: {min_month} ( ${min_chg} )" )
    
 
    