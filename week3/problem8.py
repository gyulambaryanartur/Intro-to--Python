import argparse
parser= argparse.ArgumentParser()
parser.add_argument("set1",help="Input set values",type=str)
arg=parser.parse_args()

setval=arg.set1
strset=set([2,4])
print(setval)
print("Before :",strset)
strset.add(setval)
print("After :",strset)




