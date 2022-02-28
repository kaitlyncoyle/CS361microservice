import csv

# header = ['TAG', 'DATA']
with open("data.csv", "r") as f:
    data = [line for line in csv.reader(f)]

data.sort()

with open("new_data.csv", "w") as f:
    writer = csv.writer(f)
    # writer.writerow(header)
    writer.writerow(data)

# print(data)