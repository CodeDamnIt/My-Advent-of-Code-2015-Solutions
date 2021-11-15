#Part1
santa=open("./Data/Day1Input.txt","r")
text= santa.read()
floor=text.count('(')-text.count(')')
print(floor)
