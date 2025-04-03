import csv

path = r"C:\Stack overflow\Python_foundational_training\Python Basics\Day-17 topics\university_records.csv"

rows, fields = [], []

with open(path, 'r') as f:
    csvreader = csv.reader(f)
    fields = next(csvreader)

    for i in csvreader:
        if i:
            rows.append(i)

print(fields)
print(rows)