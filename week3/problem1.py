import argparse
import sys
list1=["hello", 1, True]
arg=sys.argv[1]

listvalues=arg
print("Before adding:",list1)
list1.append(listvalues)
print("After adding:",list1)


