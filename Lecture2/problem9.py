import argparse
parser=argparse.ArgumentParser()
parser.add_argument("startindex",help="information of start index",type=int)
parser.add_argument("endindex",help="information of end index",type=int)
argum=parser.parse_args()
text=input("input text:")
print("The given text: %s"%text)
print("Start index:%s"%argum.startindex)
print("End index:%s"%argum.endindex)

print("The given text: %s"%text[int(argum.startindex):int(argum.endindex)])

