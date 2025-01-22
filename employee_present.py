"""Problem Statement:
You are the HR manager of a company. A CSV file, attendance.csv, contains data on employee attendance. The file has the following columns: EmployeeID, Date, and Status (where Status is either "Present" or "Absent"). Write a Python program to calculate the following:

Q-2:Total days each employee was present."""


import csv
data_list = []
# read and open file
with open('/content/attendance.csv','r') as f:
  file_data = csv.reader(f)
  for row in file_data:
    data_list.append(row)

employee_attendance = {} #def emty dictionary
# Calculating each empolyees total attendance storing in a dict
employee_attendance = {}
index = 0
for row in data_list:
  if index == 0: # Skipping header
    index = index + 1
    continue
  print(row)
  if row[0] in employee_attendance.keys():
    if row[2] == 'Present':
      employee_attendance[row[0]] = employee_attendance[row[0]] + 1 #updating corresponding key's value
  else:
    if row[2] == 'Present':
      employee_attendance[row[0]] = 1 #Assigning new value
print("Total attendance of each empolyee is: ")
for emp_id, total_attendance in employee_attendance:
  print(f"{emp_id}: {total_attendance}")