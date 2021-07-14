import csv

lines = []
lines.append(['hostname', 'ip_address'])
lines.append(["ftgn1", "178.128.19.20"])
lines.append(["ftgn2", "178.128.19.40"])
lines.append(["ldgn2", "178.128.19.50"])
lines.append(["ctgn1", "178.128.19.60"])
lines.append(["ctgn2", "178.128.19.65"])
lines.append(["ftrn1", "178.128.19.26"])
lines.append(["ldrn1", "178.128.19.80"])

final_string = ""
for line in lines:
    final_string += f"{line[0]},{line[1]}\n"

with open('ip_addresses.csv', 'w') as file:
    file.write(final_string)
# with open('ip_address.csv', 'w') as file: