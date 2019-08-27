import argparse
parser=argparse.ArgumentParser()
parser.add_argument("username",help="display username",type=str)
arg=parser.parse_args()
print("Welcome %s !"%arg.username)
