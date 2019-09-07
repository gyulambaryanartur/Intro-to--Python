import sys

mess=input('<')
words=mess.split(' ')
emajs={"):":"😊" ,
"(:":"🤣"}
outp=""
for message in words:
    #outp+=emajs.get(message)+" "
    print(emajs.get(message,message))
    print(emajs.get('):'))

print(outp)    
    