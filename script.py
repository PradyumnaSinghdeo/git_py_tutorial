import json
import csv

with open('data.csv', 'r', encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    
with open('data_converted.json', "w") as jsonfile:
    json.dump(rows, jsonfile, indent=4)