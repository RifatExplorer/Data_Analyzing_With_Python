"""Problem Statement:
You are the HR manager of a company. A CSV file, attendance.csv, contains data on employee attendance. The file has the following columns: EmployeeID, Date, and Status (where Status is either "Present" or "Absent"). Write a Python program to calculate the following:

Q_1:Total days one employee was present."""


import csv
data_list = []
# read and open file
with open('/content/attendance.csv','r') as f:
  file_data = csv.reader(f)
  for row in file_data:
    data_list.append(row)

# Total days one employee was present?
count_present = 0
count_absent = 0
for row in data_list:
  if row[0] == 'E007' and row[2] == 'Present':
    count_present += 1
  elif row[0] == 'E007' and row[2] == 'Absent':
    count_absent += 1
print(f"Total number of present of E007 is: {count_present}")
print(f"Total number of absent of E007 is: {count_absent}")

