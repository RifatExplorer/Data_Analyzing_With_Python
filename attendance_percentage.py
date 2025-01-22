"""Problem Statement:
You are the HR manager of a company. A CSV file, attendance.csv, contains data on employee attendance. The file has the following columns: EmployeeID, Date, and Status (where Status is either "Present" or "Absent"). Write a Python program to calculate the following:
Q-4: The percentage of days attended for each employee."""

import csv
data_list = []
# read and open file
with open('/content/attendance.csv','r') as f:
  file_data = csv.reader(f)
  for row in file_data:
    data_list.append(row)

employee_attendance = {} #def emty dictionary
# Calculating each empolyees total attendance storing in a dict

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


# The percentage of days attended for each employee.
date_list = []
for row in data_list:
  if row[1] not in date_list:
    date_list.append(row[1])


total_work_day = len(date_list) - 1
attendance_percentage = {}
for key, value in employee_attendance.items():
  attendance_percentage[key] = (value / total_work_day) * 100

print("\nAttendance Percentage for Each Employee:")
for emp_id, percentage in attendance_percentage.items():
  print(f"{emp_id} : {percentage:.2f}%")


