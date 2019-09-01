import argparse
parser=argparse.ArgumentParser()
parser.add_argument("key",help="dictionary",type=str)
parser.add_argument("value",help="dictionary",type=str)
arg=parser.parse_args()
dict1={'1':'a','2':'b"'}
print("Before",dict1)

dict1[arg.key]=arg.value
print("After",dict1)



