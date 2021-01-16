name=input("Enter your Name\n ")
name=name.lower()
i=0
while i<len(name):
 if name[i]=='a':
     name=name.replace(name[i],'')
 elif name[i]=='e':
    name=name.replace(name[i],'')
 elif  name[i]=='i':
    name=name.replace(name[i],'')
 elif  name[i]=='o':
    name=name.replace(name[i],'')
 elif  name[i]=='u':
    name=name.replace(name[i],'')
 else:
   print()
 i=i+1
print(name)
