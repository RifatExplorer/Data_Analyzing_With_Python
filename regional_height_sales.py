"""Problem Statement:
You are tasked with analyzing sales data from a CSV file, sales_data.csv. The file has columns: ProductID, Region, SalesAmount, and Date. Write a Python program to:
Q: Determine the region with the highest total sales."""


import csv

# Initialize an empty list to store sales data
sale_data = []

# Read the sales data from the CSV file
with open('/content/sales_data.csv', 'r') as f:
    df = csv.reader(f)
    for row in df:
        sale_data.append(row)


# Determine the region with the highest total sales
sale_regional = {}  # Dictionary to store region-wise sales count
index = 0  # Reset index to skip the header row

for row in sale_data:
    if index == 0:  # Skip the header row
        index += 1
        continue
    if row[1] in sale_regional.keys():  # If the region already exists in the dictionary
        sale_regional[row[1]] += 1  # Increment the count
    else:  # If the region does not exist in the dictionary
        sale_regional[row[1]] = 1  # Initialize the count to 1

# Print total sales for each region
print("\nThe total sales by region:")
for region, total_sales in sale_regional.items():
    print(f"{region}: {total_sales}")

# Print the region with the highest total sales
print("\nThe region with the highest total sales:")
for region, total_sales in sale_regional.items():
    if total_sales == max(sale_regional.values()):  # Compare to find the maximum sales
        print(f"{region}: {total_sales}")


