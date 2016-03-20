m = int(raw_input())
hold =[2,3]
print 2,3,
for i in range(4,m+1):
	for x in hold:	
		if i%x == 0:
			break
		else:
			if x == hold[-1]:
				hold.append(i)
				print i,
			continue
