import csv
import statistics
import numpy as np
import plotly.express as px

# Input and output file names
dirty_report = 'report2022202312.csv'
cleaned_report = 'cleanedreport3.csv'

# Function to check if a cell contains invalid characters (spaces or asterisks)
def contains_invalid_characters(cell):
    return '! ' in cell or '*' in cell

# Open the input file for reading and the output file for writing
with open(dirty_report, 'r') as infile, open(cleaned_report, 'w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)

    # Read the header and find the index of the 'Area_of_Law' column
    header = next(csv_reader)
    if 'AREA_OF_LAW' in header:
        area_of_law_index = header.index('AREA_OF_LAW')
        # Remove the 'Area_of_Law' column from the header
        header.pop(area_of_law_index)
    else:
        print("Column 'AREA_OF_LAW' not found in the dataset.")
        area_of_law_index = None

    # Write the updated header to the output file
    csv_writer.writerow(header)

    # Process each row
    for row in csv_reader:
        # If the 'Area_of_Law' column exists, remove it
        if area_of_law_index is not None:
            row.pop(area_of_law_index)

        # Check if the row contains any invalid characters
        if not any(contains_invalid_characters(cell) for cell in row):
            csv_writer.writerow(row)

print(f"Cleaned data has been written to {cleaned_report}")
print(cleaned_report)

df = pl.DataFrame (
    
    {"nrs": [1168,70,1078,48276,3211,90,18,0,3368,851,85,9,33829,22,2,4626,2157,2196,170839,3212,47990,1112,977,15,707,266,307,3151,847]
     "names": ["Rape (Including Attempted Rape)",'Firearms/Weapon/Possession Of Explosives/Ammunition','Drugs','Other','Sexual','Other','Murder','Threaten To Kill','Drugs','Firearms','Road Traffic','Theft','Larceny/Fraud/Robbery','Other','Possession Of Firearms/ Ammunition/Explosive Substances','Larceny/Fraud/Robbery','Public Order/Assault','Other','Road Traffic','Sexual','Other','Rape (Including Attempted Rape) Rape (Including Attempted Rape)','Drugs','Public Order','Sexual Offences','Theft/Fraud/Robbery Theft/Fraud/Robbery','Other','Drugs','Firearms/Weapon/Possession Of Explosives/Ammunition',]  
        }
    )
'''
app = Flask(__name__)  # Create a Flask app instance

@app.route("/")  # Define a route for the root URL
def home():
    return render_template("Hello World")  # Response to the browser

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=,debug=True)
# Initialize database
#def init_db():
 #   with app.app_context():
  #      db = get_db()
   #     db.execute('''
#CREATE TABLE IF NOT EXISTS user_preferences (
    #                  id INTEGER PRIMARY KEY AUTOINCREMENT,
     #                 max_fuel REAL,
      #                max_emissions REAL)''')
       # db.commit()
     



