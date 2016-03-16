from sys import stdin
inp = [int(i) for i in stdin.read().split()]
inp.pop(0)


for i in range(1,len(inp)):
	if inp[i-1] > inp[i]:
		#print inp
		pick = inp.pop(i)
		temp = inp[0:i]
		for j in range(0,i)[::-1]:
			if j == 0 and pick <temp[0]:
				a = [pick]
				temp = a + temp[j:]
				inp = temp + inp[i:]
				print inp
				break
				
			if pick > temp[j]:
				a = temp[0:j+1]
				a.append(pick)
				temp = a + temp[j+1:]
				inp = temp + inp[i:]
				print inp
				break
