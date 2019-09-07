import argparse
a = [1, 4, 5, 7, 8, -2, 0, -1]

print("given a list :",a,'\n',"2 element :",a[2],'\n',"5 element:",a[4])

a_list=a.copy()
a_list.sort(reverse=True)
print("a_sorted 1:3:",a_list[1:3],'\n',"a_sorted 3:6: ",a_list[2:6])
print("Before deletion a_list",a_list)

del a_list[2:4]
print("after deletion a_list",a_list)


b = ["grapes", "Potatoes","tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]

b_sorted=sorted(b)
print("b_sorted:",b_sorted)
c=a[1:4]+b[4:7]
print("c:",c)

