
import csv
IATACodeHashmap = {}
try:
    with open('airport_codes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        IATACodeHasmap = {}
        for row in reader:
            IATACodeHasmap[row[0]] = row[1]
     
except Exception as e:
    print("Error:", e)