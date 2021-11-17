#Part 1
import hashlib
advent=open("./Data/Day4input.txt")
key=advent.read()
for i in range(100000000000):
	hash= hashlib.md5((str(key)+str(i)).encode()).hexdigest()
	if hash[ :5] == '00000':
		print(hash)
		print(i)
		print(str(key)+str(i))
		break
#Part2
for j in range(100000000000):
	hash= hashlib.md5((str(key)+str(j)).encode()).hexdigest()
	if hash[ :6] == '000000':
		print(hash)
		print(str(key)+str(j))
		print(j)
		break
advent.close()
