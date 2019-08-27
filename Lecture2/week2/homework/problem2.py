import datetime,time
import argparse
parser =argparse.ArgumentParser()
parser.add_argument("str",help="Dispay string  len more tahn 7  and it is odd lenght",type=str)
argument=parser.parse_args()
old_str=argument.str
if len(old_str)>6 and len(old_str)%2!=0:
    print("The old string:",old_str)
    midtext=old_str[len(old_str)//2-1:len(old_str)//2+2]
    print("Middle 3 characters:",midtext)
    newstr=old_str[:len(old_str)//2-1]+midtext.upper()+old_str[len(old_str)//2+2:]
    print("The new String is:",newstr)
else:
    print("Put appropiate values!!!!!!!")
    pass        
