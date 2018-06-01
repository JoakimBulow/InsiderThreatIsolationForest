#!/usr/bin/python3

#To create a new file with inserted 'threat' column run this
#script like: './insert_answear_column.py > dataset.csv'

from datetime import datetime
import csv

def get_csv_data(filename):
  with open(filename, "r") as csv_file:
    for csv_file in csv.reader(csv_file):
      yield csv_file

##### READ ANSWERS FILE #####
filename = "4.2-logon-answers.csv"
answers_csv = iter(get_csv_data(filename))
next(answers_csv)
answers = []
for line in answers_csv:
  id=line[1]
  answers.append(id)
  #print(id)


#### READ DATA FILE ####
filename = "r4.2-logon.csv"
data_csv = iter(get_csv_data(filename))
next(data_csv)
#answers = []
for line in data_csv:
  id=line[0]
  if(id in answers):
    line.append("1")
  else:
    line.append("0") 
  string_row = ",".join(line)
  print(string_row)
