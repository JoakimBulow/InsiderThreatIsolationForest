#!/usr/bin/python3
from datetime import datetime
import csv

def get_csv_data(filename):
  with open(filename, "r") as csv_file:
    for csv_file in csv.reader(csv_file):
      yield csv_file


##### READ FEATURES FILE #####
filename = "dataset.csv"
iter_csv = iter(get_csv_data(filename))
##############################

print("login,logout,timediff,threat")

line_nbr = -0
for line in iter_csv:
  line_nbr += 1
  id_string = line[0]
  datetime_string = line[1]
  user_string = line[2]
  pc_string = line[3]
  activity_string = line[4]
  threat_string = line[5]



  datetime_object = datetime.strptime(datetime_string, '%m/%d/%Y %H:%M:%S')
  if(activity_string == "Logon"):
    #Look for line where this user & pc combination has activity = Logoff
    inner_iter_csv = iter(get_csv_data(filename))
    sub_line_nbr = 0
    for sub_line in inner_iter_csv:
      if(sub_line_nbr == 0):
        #Skip the rows above the current sub_line row
        sub_line_nbr = line_nbr
        for i in range(line_nbr):
          next(inner_iter_csv)

      sub_line_nbr += 1
      next_user_string = sub_line[2]
      next_pc_string = sub_line[3]
      next_activity_string = sub_line[4]

      if(next_pc_string == pc_string and user_string == next_user_string and next_activity_string == "Logoff"):
        #print("Found " + pc_string + " and " + next_user_string + " on row " + str(sub_line_nbr))
        next_datetime_object = datetime.strptime(sub_line[1], '%m/%d/%Y %H:%M:%S')
        timediff = next_datetime_object - datetime_object
        #print("Logged in for: " + str(timediff))
        print(str(datetime_object)+","+str(next_datetime_object)+","+str(round((timediff.total_seconds()/60),0))+","+threat_string)
	#print("Found it on row " + str(sub_line_nbr))
        #print(str(sub_line))
        #print("Base line number: " + str(line_nbr))
        break
    
  elif(activity_string == "Logoff"):
    continue
    
  else:
    print("ERROR!")


