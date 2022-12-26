import csv

with open('ip_addresses.csv', 'r') as file:
    data = csv.reader(file)
    ip_address = {}
    for line in data:
        ip_address[line[0]] = line[1]

    