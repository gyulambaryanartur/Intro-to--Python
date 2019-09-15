list1 = ['Anna', 'Edgar'] 
listmain= ["Eliza", "Ani", "Vardan"]
flag = 0
def dec(fn):
    def wrappers(*arg,**kwarg):
       flag = 1
       after=fn(*arg,**kwarg)
       print( 'after:',after)
       print("before changes",listmain)
    return wrappers

def add_values(list2):
    return listmain+list2

if flag:
    add_values(list1)  
else:
    add_values(list1) 
