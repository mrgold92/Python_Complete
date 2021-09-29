import csv

with open('06-Archivos-CSV/sample.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)

with open('06-Archivos-CSV/sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[' Product '], row['Country'])
        print(row)

results = []
with open('06-Archivos-CSV/sample.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
print(results)

with open('06-Archivos-CSV/names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
