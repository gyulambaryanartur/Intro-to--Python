import argparse
a1=["Cookies", "Chocolate",8, True, -3, -5, "Chocolate", 8, False, 8]
b1=[8, True, 10, 14,"Chocolate", "Milk", "Jelly", True, False, True]
set_a=set(a1)
set_b=set(b1)
union_ab=set_a.union(set_b)
intersect_ab=set_a.intersection(set_b)

print("set_a",set_a,'\n',"set_b",set_b,'\n',"union_ab:",union_ab,'\n',"intesect_ab:",intersect_ab)
union_ab.update(['Oreo','KitKat'])
print("union_ab:",union_ab)
news_set =union_ab|intersect_ab
print(news_set)
print("Chocolate" in news_set)
news_set.remove("Oreo")
print(news_set)
t1=(1, True, "a", -2,"Anna")
t2=(1, 2, 3, 4, 5)
print(f' init t1_tuple:{t1}')
t1_list=list(t1)
t1_list.pop(True)
#del t1_list[1] or
t1=tuple(t1_list)
print(f' after  t1_tuple:{t1}')
t3=t1[0:2]+t2[0:3]
print(f't3 tuple:{t3}')
print(f't3 tuple 2 ind:{t3[2]}')
t4_list=[(1,3,5), (8,9), ("Anna", "Bob","Alice")]    
print(f't4_list [1,2]={t4_list[0][1]}')
martket={"dairy":\
 ["yogurt", "cheese"], "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana",\
  "banana"]}
print(f"Market dict Before update:{martket}")
martket["candies"]=   ["mars","kinder", "twix"]
martket["fruits"]=list(set(martket["fruits"]))
martket["fruits"].sort()
print(f"Market dict after update:{martket}")