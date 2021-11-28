import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", help="echo the string you use here", type=str, action="append")
parser.add_argument("pos", help="echo the string you use here", type=str, nargs="+")
args = parser.parse_args()
print(args.pos)
print(args.v)