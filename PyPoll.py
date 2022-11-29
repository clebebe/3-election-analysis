import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.txt")

with open(file_to_load) as election_data:
    # to do: read and analyze the data
    file_reader = csv.reader(election_data)

    #print header row
    headers = next(file_reader)
    print(headers)