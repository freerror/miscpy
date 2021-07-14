# for loop way
# mobile_gateways = ['ftgn1', 'ftgn2', 'ldgn2', 'ctgn1']
# print("List of all Mobile gateways:")
# for gateway in mobile_gateways:
#     print(gateway.upper())
#     
# # simple way
# print("List of all Mobile gateways:")
# print(mobile_gateways[0])
# print(mobile_gateways[1])
# print(mobile_gateways[2])
# print(mobile_gateways[3])

# # generate some code
# code = 'mobile_gateways = ['
# for i in range(0, 4):
#     code += f"\'ftgn{i}\', "
# code = code[:-2]
# code += ']'
# print(code)

# device_names = []
# num_of_devices = input("Please enter number of devices (must be whole number):")
# num_of_devices = int(num_of_devices)
# for i in range(0, num_of_devices):
#     device_names.append(input("Enter a device then press enter:"))
#     
# for device in device_names:
#     print(device.upper())

devices = {
    "akpe1": ["PE","AKL", "IP Team"],
    "ftrn1": ["RNC", "AKL", "RAN team"]
}

query = input("Enter a device hostname: ").lower()

print("\nDevice type: ", devices[query][0])
print("Region: ", devices[query][1])
print("\nOwner:", devices[query][2], "\n")