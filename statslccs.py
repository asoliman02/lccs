import pandas as pd
import numpy as np
import statistics
import plotly.express as py

file_path = "cleanedreport3.csv"

data = pd.read_csv(file_path, na_values=["No data"], encoding='utf-8')
stats_dictionary = {}

pd.drop_duplicates()
data = data.dropna()
nonnumeric_cols = ["JURISDICTION", "CATEGORY"]
numeric_cols = ["YEAR", "INCOMING", "RESOLVED"]

# Convert numeric columns to numeric type
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors="coerce")

# Collect statistics for each numeric column
for col in numeric_cols:
    stats_data = data[col]  # Now stats_data is defined per column
    
    stats_dictionary[col] = {
        "Mean": stats_data.mean(),
        "Median": stats_data.median(),
        "Mode": stats_data.mode().iloc[0] if not stats_data.mode().empty else np.nan,
        "Range": stats_data.max() - stats_data.min()
    }

print(stats_dictionary)



