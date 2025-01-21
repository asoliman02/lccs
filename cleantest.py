import csv
import pandas
import statistics
# Input and output file names
input_file = 'report2022202312.csv'
output_file = 'cleanedreport2.csv' #Extracted from large.csv

# Open the input file and create a writer for the output file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)

    # Write the header (assuming the first row is the header)
    header = next(csv_reader)
    csv_writer.writerow(header)
    
    # Write every 10th row
    for idx, row in enumerate(csv_reader, start=1):
        if idx % 1 == 0:
            csv_writer.writerow(row)
        df.drop("AREA_OF_LAW")
