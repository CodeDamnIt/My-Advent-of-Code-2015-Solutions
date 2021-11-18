#Part1
string=str(open("./Data/Day5input.txt").read()).split()
Nice=[ ]
for j in string:
	x=j.count("a") + j.count("e")+j.count("i") + j.count("o") + j.count("u")
	if x>=3:
		for i in range(len(j)-1):
			if j[i] == j[i+1]:
				if 'ab' not in j and 'cd' not in j and 'pq' not in j and 'xy' not in j:
					Nice.append(j)
print(len(set(Nice)))
#Part2
Nicer=[ ]
for a in string:
			for b in range(len(a)-2):
				if a[b] == a[b+2]:
					for c in range(len(a)-3):
						d=a[c:c+2]
						if d in a[c+2 : ]:
							Nicer.append(a)				
print(len(set(Nicer)))
