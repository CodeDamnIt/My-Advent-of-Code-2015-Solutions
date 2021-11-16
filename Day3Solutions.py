#Part1
santa=open("./Data/Day3input.txt")
content=santa.read()
gift=[0,0]
grid= ['0,0']
for i in content:
	if i == '^':
		gift= [gift[0],gift[1]+1]
		grid.append(str(gift))
	elif i == '<':
		gift= [gift[0]-1,gift[1]]
		grid.append(str(gift))
	elif i == '>':
		gift= [gift[0]+1,gift[1]]
		grid.append(str(gift))
	else:
		gift= [gift[0],gift[1]-1]
		grid.append(str(gift))
houses=set(grid)
print(len(houses))

