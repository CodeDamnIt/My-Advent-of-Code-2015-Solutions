#Part1
santa=open("./Data/Day3input.txt")
content=santa.read()
gift=[0,0]
grid= ['0,0']
for i in content:
	if i == '^':
		gift= [gift[0],gift[1]+1]
	elif i == '<':
		gift= [gift[0]-1,gift[1]]
	elif i == '>':
		gift= [gift[0]+1,gift[1]]
	else:
		gift= [gift[0],gift[1]-1]
		
	if not str(gift[0]) + ',' + str(gift[1]) in grid:
		grid.append(str(gift[0]) + ',' + str(gift[1]) )
print(gift)
print(len(grid))
