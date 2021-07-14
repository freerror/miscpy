import requests
import json
import argparse


json_request = requests.get('http://nrmurp02l.kaainga.nz/api/ipam/ip-addresses/')
# json_request = requests.get('http://nrmurp02l.kaainga.nz/api/ipam/ip-addresses/?dns_name=a3jrm01&format=json')
json_dump = json.loads(json_request.content)

parser = argparse.ArgumentParser(description='Please Enter device hostname.')
parser.add_argument('-d', '--dnsname', required=False, type=str, help='Enter dns name')
args = parser.parse_args()
device = args.dnsname

if device == None:
    query = input("Enter DNS Name: ")
else:
    query = device 

data_found = False

print("#############################################\n")
for data in json_dump['results']:
    details = (data['dns_name'], data['address'])
    if details[0].find(query) != -1:
        print("The IP of {0} is {1}\n".format(details[0], details[1]))
        data_found = True
if not data_found:
    print("Nothing matched your device query!\nPlease try again.\n")
    avail_names = ""
    print("Available DNS names:")
    for data in json_dump['results']:
        avail_names += f"{data['dns_name']}, "
    print(avail_names, "\n")
print("#############################################")
