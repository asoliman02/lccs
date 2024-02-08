import csv
import pandas
import statistics

file = open("myfile3.csv","a")
file.write('Noise')
file.write('\t')
file.write('Temperature')
print('Columns Created')
file.close

file = open("myfile3.csv","a")
file.write('\n')
file.write('25')
file.write('\t')
file.write('10')
file.write('\n')
file.write('24')
file.write('\t')
file.write('12')
file.write('\n')
file.write('12')
file.write('\t')
file.write('9')
file.write('\n')
file.write('33')
file.write('\t')
file.write('77')
print('Data Created')
file.close