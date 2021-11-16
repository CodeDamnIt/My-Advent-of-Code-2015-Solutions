#Part1
cardboard=open("./Data/Day2input.txt","r")
content=cardboard.read()
f=content.splitlines()
Surfarea=0
for words in f:
	split=words.split('x')
	l=int(split[0])
	b=int(split[1])
	h=int(split[2])
	area=2*(l*b+b*h+l*h) + min(l*b,b*h,h*l)
	Surfarea+=area
print(Surfarea)
