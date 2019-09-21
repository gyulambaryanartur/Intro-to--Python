import Productcheck as ch
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("productname",help="Put prod name",type=str)
parser.add_argument("productcount",help="Put prod count",type=int)
parser.add_argument("productPrice",help="Put prod price",type=int)
arg=parser.parse_args()

def buy(product, num, price):
    if ch.check(product, num):
        s=num*price
        print(f'You bought product and spent %s ,'%s)
    else:
        print('Sorry! We are out of this product.')   
def main():
    buy(arg.productname,arg.productcount, arg.productPrice)
if __name__ == "__main__":
    
    main()    


