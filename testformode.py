import csv
from collections import Counter

def calculate_mode(csv_file, column_name):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = [column[column_name] for column in reader]

    # Using collections.Counter to count occurrences of each value
    counts = Counter(data)
    mode = counts.most_common(1)[0][0]

    return mode

csv_file = 'alt2data3.csv'  # Replace 'data.csv' with your CSV file path
column_name = 'column_name'  # Replace 'column_name' with the column you want to calculate mode for
mode = calculate_mode(csv_file, column_name)
print(f"The mode of {column_name} column is: {mode}")
