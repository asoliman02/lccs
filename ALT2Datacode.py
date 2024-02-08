import csv
import pandas
import statistics

# Open and Create the file 
csvfile = open("alt2data.csv", "w",newline = "")
print("File Created")


# Create column headers
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['How long spent studying each day?', 'How much time spend on phone each night?','How many hours slept on a Sunday Night','How many hours slept on a Monday Night', 'How many hours slept on a Tuesday Night', 'How many hours slept Wednesday Night', 'How many hours slept on a Thursday Night' ])
print("Columns Created")

# Create 2 rows of data 
csvwriter.writerow([1, 0, 5])
csvwriter.writerow([1, '20 mins', 6])
csvwriter.writerow([1, 1, 6])
csvwriter.writerow([2, 1, 6])
csvwriter.writerow([2, 1, 6])
csvwriter.writerow([2, 2, 6])
csvwriter.writerow([2, '20 mins', 6])
csvwriter.writerow([2, 2, 6])
csvwriter.writerow([2, 2, 6])
csvwriter.writerow([2, 3, 6])
csvwriter.writerow([2, 2, 6])
csvwriter.writerow([2, 3, 7])
csvwriter.writerow([2, 3, 7])
csvwriter.writerow([2, 3 ,7])
csvwriter.writerow([2, 3 ,7])
csvwriter.writerow([2, 3, 7])
csvwriter.writerow([2, 3, 7])
csvwriter.writerow([3, 3, 7])
csvwriter.writerow([3, 3, 7])
csvwriter.writerow([3, 3, 7])
csvwriter.writerow([3, 4, 8])
csvwriter.writerow([3, 4, 8])
csvwriter.writerow([3, 4, 8])
csvwriter.writerow([3, '45 mins', 8])
csvwriter.writerow([3, 5, 8])
csvwriter.writerow([3, 6,])
csvwriter.writerow([4, 6])
csvwriter.writerow([4, 7])
csvwriter.writerow([4, 7])
csvwriter.writerow([4, 7])
csvwriter.writerow([4, 7])
csvfile.close()
print("Data Created")