import csv
import pandas
import statistics

df = pandas.read_csv('alt2datafile.csv')
print(df.to_string())
# Filter out the column, value_eur
study_values = df['Time Studying']
mean_value_study = round(statistics.mean(study_values), 2)
print("Mean Value Study:", mean_value_study)

