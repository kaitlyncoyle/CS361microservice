import csv
from operator import itemgetter

with open('data.csv', 'r') as f:
    data = [line for line in csv.reader(f)]

data.sort()
print(data)
