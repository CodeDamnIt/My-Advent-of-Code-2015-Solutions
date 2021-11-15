#Part1
santa=open("/storage/emulated/0/Download/txt.txt","r")
text= santa.read()
floor=text.count('(')-text.count(')')
print(floor)
