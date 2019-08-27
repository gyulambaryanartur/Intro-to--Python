import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--age",help="display age",type=int)
arg=parser.parse_args()
print("Happy Birthday, you are already %s years old!"%arg.age)
