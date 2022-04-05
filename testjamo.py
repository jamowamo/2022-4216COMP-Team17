import csv
import matplotlib

with open("arrest rate by competition.csv" , "r") as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)