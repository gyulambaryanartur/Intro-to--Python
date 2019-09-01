import argparse

l1=[(1, 'a'),(2, 'b'), (3, 'c')]
print(l1)
dict1={}
dict1[l1[0][0]]=l1[0][1]
dict1[l1[1][0]]=l1[1][1]
dict1[l1[2][0]]=l1[2][1]

print("dict1:",dict1)


