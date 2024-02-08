import csv
import pandas
import statistics
import matplotlib.pyplot as plt

df = pandas.read_csv('alt2data3.csv')

# Filter out the column, value_eur
study_values = df['Time Studying']

mean_value_study = round(statistics.mean(study_values), 2)
print("Mean Value Study:", mean_value_study)

# Initialise a list of ages
L = [2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 3, 2, 3, 3, 1, 3, 3, 2, 2, 3, 3, 1, 3, 3, 3, 2, 1, 3]
K = [7, 2, 1, 2, 0, 3, 3, 3, 3, 1, 4, 1, 1, 3, 3, 4, 3, 6, 4, 5, 1, 2, 3, 6, 3, 1, 2, 2, 3, 1]
# Build up a list of unique values
unique_values = []
for value in L:
    if value not in unique_values:
        unique_values.append(value)

unique_values = []
for value in K:
    if value not in unique_values:
        unique_values.append(value)


# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = L.count(value)
    frequencies.append(frequency)


# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]

print("Mode is", mode)
print("Max_Freq", max_frequency)
print("Max_Freq_Pos", max_frequency_pos)
print('\n')

K = [7, 2, 1, 2, 0, 3, 3, 3, 3, 1, 4, 1, 1, 3, 3, 4, 3, 6, 4, 5, 1, 2, 3, 6, 3, 1, 2, 2, 3, 1]


unique_values = []
for value in K:
    if value not in unique_values:
        unique_values.append(value)


# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = K.count(value)
    frequencies.append(frequency)


# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]

print("Mode is", mode)
print("Max_Freq", max_frequency)
print("Max_Freq_Pos", max_frequency_pos)
print('\n')