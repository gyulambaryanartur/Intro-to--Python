import argparse
parser=argparse.ArgumentParser()
parser.add_argument("set",type=int)
arg=parser.parse_args()
subsetval=arg.set
strset=set([2,4,13,21])
list1=list(strset)
list1.sort()
minvalue=list1[1]
maxvalue=list1[-1]

print("IS subset",maxvalue>=subsetval>=  minvalue)




