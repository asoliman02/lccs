with open(alt2data.csv, "r", newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader, None)
    print("Header with:", header)
    for row in csvreader:
        print(row[0])
        print(row[1])
        tot_Temp = tot_Temp + int(row[0])
        rec_ct = rec-ct +1
        #add code to accum average here
        #add code to count the records here