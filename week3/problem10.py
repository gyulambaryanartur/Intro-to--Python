import argparse
parser= argparse.ArgumentParser()
parser.add_argument("set1",help="Input set values",type=int)
arg=parser.parse_args()

setval=arg.set1
strset=set([2,4,13,21])
print(setval)
print("Before :",strset)
strset.discard(setval)
print("After :",strset)




