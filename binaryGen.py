from sys import stdin
stone = map(int,stdin.read().split())
count = stone.pop(0)
stone.sort()
x = 0
min = float('inf')
while x <= int('1'*count,2)/2:
	bin = map(int,list("{0:b}".format(x).zfill(count)))
	#print bin
	p1 = sum([a*b for a,b in zip(bin,stone)])
	bin = [(1-b)*(b**b) for b in bin]
	#print bin
	p2 = sum([a*b for a,b in zip(bin,stone)])
	#print p1, p2
	dif = abs(p1-p2)
	if dif < min: min = dif
	x += 1 
print min
