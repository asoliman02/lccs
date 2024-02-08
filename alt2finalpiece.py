import csv
import pandas
import statistics
import matplotlib.pyplot as plt

df = pandas.read_csv('alt2data3.csv')

# Filter out the column, value_eur
study_values = df['Time Studying']

mean_value_study = round(statistics.mean(study_values), 2)
print("Mean Value Study:", mean_value_study)

phone_values = df['Phone']

mean_value_phone = round(statistics.mean(phone_values), 2)
print("Mean Value Phone:", mean_value_phone)

sunday_values = df['Sunday']

mean_value_sunday = round(statistics.mean(sunday_values), 2)
print("Mean Value Sunday:", mean_value_sunday)

monday_values = df['Monday']

mean_value_monday = round(statistics.mean(monday_values), 2)
print("Mean Value Monday:", mean_value_monday)

tuesday_values = df['Tuesday']

mean_value_tuesday = round(statistics.mean(tuesday_values), 2)
print("Mean Value Tuesday:", mean_value_tuesday)

wednesday_values = df['Wednesday']

mean_value_wednesday = round(statistics.mean(wednesday_values), 2)
print("Mean Value Wednesday:", mean_value_wednesday)

thursday_values = df['Thursday']

mean_value_thursday = round(statistics.mean(thursday_values), 2)
print("Mean Value Thursday:", mean_value_thursday)
print('\n')

# Initialise a list of ages
L = [2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 3, 2, 3, 3, 1, 3, 3, 2, 2, 3, 3, 1, 3, 3, 3, 2, 1, 3]
# Build up a list of unique values
unique_values = []
for value in L:
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

J = [Sunday
7
6
6
6
6
7
5
6
8
8
7
8
8
8
6
8
8
7
7
6
8
8
7
6
6
8
7
6
7
7
]


unique_values = []
for value in J:
    if value not in unique_values:
        unique_values.append(value)


# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = J.count(value)
    frequencies.append(frequency)


# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]

print("Mode is", mode)
print("Max_Freq", max_frequency)
print("Max_Freq_Pos", max_frequency_pos)
print('\n')



labels = 'mean_value_study', 'mean_value_phone', 'mean_value_sunday','mean_value_tuesday', 'mean_value_wednesday', 'mean_value_thursday'
sizes = [mean_value_study, mean_value_phone, mean_value_sunday, mean_value_tuesday, mean_value_wednesday, mean_value_thursday]
colors = ['pink', 'violet', 'blue', 'purple', 'yellow', 'red']
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # explode 1st slice
# Plot the Pie Chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
#plt.axis('equal')
plt.show()

