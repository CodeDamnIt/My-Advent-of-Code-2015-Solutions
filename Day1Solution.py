santa=open("/storage/emulated/0/Download/txt.txt","r")

text= santa.read()

x=text.count('(')

y=text.count(')')

floor=x-y

print(floor)
