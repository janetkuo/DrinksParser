import json
import csv

f = open('beer_p1.json')
data = json.load(f)
print data
f.close()

f = csv.writer(open('beers_first100.csv', 'wb+'))
# use encode to convert non-ASCII characters
for item in data:
    values = [ x.encode('utf8') for x in item['fields'].values() ]
    f.writerow([item['pk'], item['model']] + values)