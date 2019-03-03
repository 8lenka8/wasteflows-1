import csv
from pprint import pprint
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    links = []
    data = set()
    for row in reader:
        if row['from'] == 'NA' or row['to'] == 'NA':
            continue

        links.append({
            'source': row['from'],
            'target': row['to'],
            'value': row['n'],
        })
        data.add(row['from'])
        data.add(row['to'])
    data = [{'name': i} for i in data]
    pprint(links)
    pprint(data)
