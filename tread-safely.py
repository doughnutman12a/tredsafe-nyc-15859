# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:58:44 2020

@author: admin
"""

#!/usr/bin/python

import csv


#input number you want to search
number = input('Enter Your Zip Code\n')

#read csv, and split on "," the line
csv_file = csv.reader(open('tests-by-zcta.csv',), delimiter=",")


#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number == row[1]:
        print (row)
        
    
    else:
        print ("Error not found")
        