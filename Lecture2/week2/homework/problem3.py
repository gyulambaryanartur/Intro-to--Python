import datetime,time
import argparse
initstr=input("input initial text:")
parser =argparse.ArgumentParser()
parser.add_argument("first",help="Dispay  string  which have to changed",type=str)
parser.add_argument("second",help="Dispay  string  which have to changed",type=str)

argument=parser.parse_args()
first_text=argument.first
second_text=argument.second
print("The given text:",initstr)
print("First word:",first_text)
print("Second word:",second_text)

print("output:",initstr.replace(first_text,second_text))