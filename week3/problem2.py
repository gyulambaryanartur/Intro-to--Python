import argparse
import sys
list1=["hello", 1, True]
arg=sys.argv[1]
list3=list1.copy()
listvalues=arg
print("Before adding list 1:",list1)
print("Before adding list 3:",list3)
list3.append(listvalues)
print("After adding: list1:",list1)

print("After adding list3:",list3)




