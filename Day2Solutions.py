#Part1 and Part 2 Both
cardboard=open("./Data/Day2input.txt","r")
content=cardboard.read()
f=content.splitlines()
Surfarea=0
Ribbon=0
for words in f:
	split=words.split('x')
	l=int(split[0])
	b=int(split[1])
	h=int(split[2])
	area=2*(l*b+b*h+l*h) + min(l*b,b*h,h*l)
	Surfarea+=area
	Ribbon+=l*b*h+min(2*(l+b),2*(b+h),2*(l+h))
print("Elves should order",Surfarea,"square feet of wrapping paper")
print("Elves should order",Ribbon,"feet of ribbon")
cardboard.close()
