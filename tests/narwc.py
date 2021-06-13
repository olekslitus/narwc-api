from . import catalog
import csv

with open('parents_date.csv', 'w') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(['Whale ID', 'Mother ID', 'Father ID'])
    for whale in catalog.whales():
        writer.writerow([whale.id, whale.mother_id(), whale.father_id()])