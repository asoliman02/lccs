import csv
import pandas
import statistics
import flask
import plotly.express as px
# Input and output file names
dirty_report = 'report2022202312.csv'
cleaned_report = 'cleanedreport.csv'

# Function to check if a row contains spaces or asterisks

def contains_invalid_characters(row):
    for cell in row:
        if ' ' in cell or '*' in cell:
            return True
    return False

df.drop("AREA_OF_LAW")

# Open the input file and process the rows
with open(dirty_report, 'r') as infile, open(cleaned_report, 'w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    
 
    # Write the header to the output file
    header = next(csv_reader)
    csv_writer.writerow(header)
    
    # Process each row
    for row in csv_reader:
        if not contains_invalid_characters(row):
            csv_writer.writerow(row)

print(f"Cleaned data has been written to {cleaned_report}")



app = Flask(__name__)  # Create a Flask app instance

@app.route("home")  # Define a route for the root URL
def home():
    return "This is the home page."  # Response to the browser

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode



