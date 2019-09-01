import argparse
list2 = [0, "hi", 2, 100, 300, 2]
parser=argparse.ArgumentParser()
parser.add_argument("ListValues",help="List value",type=int)
arg=parser.parse_args()
Nofmatches=list2.count(arg.ListValues)

print("Number of %ss:"%arg.ListValues,Nofmatches)





