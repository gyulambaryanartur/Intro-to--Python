list1 = ['Anna', 'Edgar'] 
listmain= ["Eliza", "Ani", "Vardan"]
flag = 0
def dec1(fn):
    def wrappers(*arg,**kwarg):
        str1=fn(*arg,**kwarg)
        str2=str1[0]+str1[1:].lower()
        return str2
    return wrappers
def dec2(fn):
    def wrappers(*arg,**kwarg):
        str3=str(fn(*arg,**kwarg))
        print(str3+"!!! Welcometo the party.")

    return wrappers   
@dec2
@dec1
def Getstr():
    return "HI EVERYONE"
Getstr()    


