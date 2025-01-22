"""Problem Statement:
You are tasked with analyzing sales data from a CSV file, sales_data.csv. The file has columns: ProductID, Region, SalesAmount, and Date. Write a Python program to:
Q : Calculate the total sales for each product."""

import csv

# Initialize an empty list to store sales data
sale_data = []

# Read the sales data from the CSV file
with open('/content/sales_data.csv', 'r') as f:
    df = csv.reader(f)
    for row in df:
        sale_data.append(row)

# Calculate the total sales for each product
sell_product = {}  # Dictionary to store product-wise sales count
index = 0  # Index to skip the header row

for row in sale_data:
    if index == 0:  # Skip the header row
        index += 1
        continue
    if row[0] in sell_product.keys():  # If the product already exists in the dictionary
        sell_product[row[0]] = sell_product[row[0]] + 1  # Increment the count
    else:  # If the product does not exist in the dictionary
        sell_product[row[0]] = 1  # Initialize the count to 1

# Print the total sales for each product
print("Total sales for each product:")
for product, total_sales in sell_product.items():
    print(f"{product}: {total_sales}")
