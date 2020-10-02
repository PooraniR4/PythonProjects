import os
mypath='C:\Python Testleaf'
f=[]
f1=[]
for dirpath,dir,files in os.walk(mypath):
     f.extend(dir)
     f1.extend(files)

print('Directories:',f, '\n')
print('Files:',f1)
