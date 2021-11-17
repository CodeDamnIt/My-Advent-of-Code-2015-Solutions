#Part1
santa=open("./Data/Day3input.txt")
content=santa.read()
gift=[0,0]
grid= [ ]
for i in content:
	if i == "^":
		gift= [gift[0],gift[1]+1]
		grid.append(str(gift))
	elif i == "<":
		gift= [gift[0]-1,gift[1]]
		grid.append(str(gift))
	elif i == ">":
		gift= [gift[0]+1,gift[1]]
		grid.append(str(gift))
	else:
		gift= [gift[0],gift[1]-1]
		grid.append(str(gift))
houses=set(grid)
print(len(houses))
#Part2
Claus = [0,0]
Robo = [0,0]
Grid = [ ]
j = 0
for d in content:
    j+=1 
    if d == ">":
        if j % 2 == 0:
            Claus=[Claus[0]+1,Claus[1]]
            Grid.append(str(Claus))
        else:
            Robo= [Robo[0]+1,Robo[1]]
            Grid.append(str(Robo))
    elif d == "<": 
        if j % 2 == 0:
            Claus=[Claus[0]-1,Claus[1]]
            Grid.append(str(Claus))
        else:
            Robo=[Robo[0]-1,Robo[1]]
            Grid.append(str(Robo))
    elif d == "^":
        if j % 2 == 0:
            Claus=[Claus[0],Claus[1]+1]
            Grid.append(str(Claus))
        else:
            Robo=[Robo[0],Robo[1]+1]
            Grid.append(str(Robo))
    else:
        if j % 2 == 0:
            Claus=[Claus[0],Claus[1]-1]
            Grid.append(str(Claus))  
        else:
            Robo=[Robo[0],Robo[1]-1]
            Grid.append(str(Robo))
santa.close()         
print(len(set(Grid)))

