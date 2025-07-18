import csv
import os

# Folder where the data CSVs are stored
data_folder = 'data'
output_file = 'processed_sales.csv'

# Header for the output CSV
output_data = [['Sales', 'Date', 'Region']]

# Loop through all files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'].strip().lower() == 'pink morsel':
                    try:
                        quantity = int(row['quantity'])
                        price = float(row['price'])
                        sales = quantity * price
                        date = row['date']
                        region = row['region']
                        output_data.append([sales, date, region])
                    except ValueError:
                        print(f"Skipping row due to invalid data: {row}")

# Write the final output to CSV
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_data)

print(f"✅ Processed data written to '{output_file}'")
