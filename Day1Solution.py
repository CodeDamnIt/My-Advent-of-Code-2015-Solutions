#Part1
santa=open("./Data/Day1Input.txt","r")
text= santa.read()
floor=text.count('(')-text.count(')')
print(floor)
santa.close()
#Part 2
negative=open("./Data/Day1Input.txt")
basement = 0
for i in negative:
    for j in range(len(i)):
        if (i[j] == "("):
            basement+=1
        else:
            basement-=1
        if (basement == -1):
            print(j+1)
            break
negative.close()
