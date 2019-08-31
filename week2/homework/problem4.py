import datetime,time
import argparse
#initstr=input("input initial text:")
initstr="Welcome to USA. usa is awesome, isn’t it?"
parser =argparse.ArgumentParser()
parser.add_argument("Countryname",help="Dispay  string  which have to changed in the text",type=str)
argument=parser.parse_args()
first_text=argument.Countryname
second_text="Armenia"
print("The given text:",initstr)
print("The %s count is:"%first_text,initstr.lower().count(first_text.lower()))
newstr=initstr.split(" ")
str_count=len(newstr)
for i in range(str_count):
    if   newstr[i].lower().isalpha(): 
      if newstr[i].lower()== first_text.lower():
     
            newstr[i]=second_text

    else:
        if newstr[i].lower()[:-1]== first_text.lower():
            newstr[i]=newstr[i].lower().replace(first_text.lower(),second_text)
            #(t,111111111111)
sep=", "            
print("The new string:",sep.join(newstr))
print("The new string:",initstr.replace(first_text,second_text))