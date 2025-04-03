import csv

fields = ["name", "year", "cgpa"]
rows = [
    ["tharun", 3, 56],
    ["atithya", 3, 96],
    ["aadhi", 3, 99]
]

with open("university_records.csv", 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)