import csv
import pandas
import statistics

tottemp=0
recct=0
totnoise=0
# Open the file read it and print the first 2 rows
csvfile = open("myfile4.csv","r", newline='')
csv_reader = csv.reader(csvfile)
header = next(csv_reader, None)

line = csvfile.readline()
print(line, "readline1")
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)
print("\n")

line = csvfile.readline()
print(line, "readline1")
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)
print("\n")

line = csvfile.readline()
print(line, "readline1")
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)
print("\n")

line = csvfile.readline()
print(line, "readline1")

line = csvfile.readline()
print(line, "readline1")
columns=line.strip().split(',')
column2=columns[1]
totnoise=totnoise+int(column2)
recct=recct+1
print("Totnoise",totnoise," ",recct)
print("\n")