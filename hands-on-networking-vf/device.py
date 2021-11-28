import argparse

parser = argparse.ArgumentParser(description='Please Enter device hostname.')
parser.add_argument('-d', '--device', required=True, type=str, help='Ener device hostname')
args = parser.parse_args()

device = args.device
print(device)