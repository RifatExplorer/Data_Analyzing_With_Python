"""Problem Statement:
You are tasked with analyzing sales data from a CSV file, sales_data.csv. The file has columns: ProductID, Region, SalesAmount, and Date. Write a Python program to:
Q: Find the product with the highest sales in a specific region provided by the user."""

import csv

# Initialize an empty list to store sales data
sale_data = []

# Read the sales data from the CSV file
with open('/content/sales_data.csv', 'r') as f:
    df = csv.reader(f)
    for row in df:
        sale_data.append(row)

# Finding the product with the highest sales in a specific region provided by the user
regional_product = {}  # Dictionary to store product sales in the specified region
specific_region = input("Enter the region: ")  # Prompt the user for a region
for row in sale_data:
    # Check if the current row belongs to the specified region
    if specific_region == row[1]:
        # Update the count for the product
        if row[0] in regional_product.keys():
            regional_product[row[0]] += 1
        else:
            regional_product[row[0]] = 1

# Display the product with the highest sales in the specified region
print(f"The highest sales in {specific_region} region is below:")
for product, total_sales in regional_product.items():
    if total_sales == max(regional_product.values()):  # Check for the highest sales
        print(f"{product}: {total_sales}")
