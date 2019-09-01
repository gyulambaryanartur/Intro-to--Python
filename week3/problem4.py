import argparse
list2 = [0, "hi", 2, 100, 300, 2]
parser=argparse.ArgumentParser()
parser.add_argument("ListValues",help="List value",type=int)
arg=parser.parse_args()
print("Before :",list2)
list2.remove(arg.ListValues)
print("Before :",list2)




