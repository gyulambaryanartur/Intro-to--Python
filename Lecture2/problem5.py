import argparse
parser=argparse.ArgumentParser()
parser.add_argument("str",help="display text",type=str)
arg=parser.parse_args()
print("The given string: %s !"%arg.str)
print("All lowercase: %s !"%arg.str.lower())
print("All uppercase: %s"%arg.str.upper())
