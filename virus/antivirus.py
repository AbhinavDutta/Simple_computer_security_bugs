SIGNATURE = "CS547 SECURITY"
import re
prog = re.compile('def[ |.]*decrypt[.| ]*') #check if any function with substring decrypt
f=open('dummy.py')

for i,line in enumerate(f):
    result = prog.match(line)
    if(result==None):
        continue
    else:
        print('suspected malware')
        exit()

print('safe')