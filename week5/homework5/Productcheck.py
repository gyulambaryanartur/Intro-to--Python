prod={"candy":10, "juice": 5, "pen": 50}
def check(product, num):
    if prod.get(product):
     if    prod[product]>=num:
       return  True
     else:
       return False    
    else:
       return False

