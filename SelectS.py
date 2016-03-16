
_ = raw_input()
lis = [ int(i) for i in raw_input().split() ]
res = []

while True:
	if lis == []: break
	min = lis.pop(0)
	for i in range(0, len(lis)):
		if min <= lis[i]: pass
		else:
			lis.append(min)
			min = lis.pop(i)
	res.append(min)
	print lis, res
	print 'end'

