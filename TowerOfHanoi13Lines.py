max = int(raw_input()); moves = {}
def ABC(max,n,i):
	if (max%2==0)^(n%2==0) == True:
		if i%3==0: return 'A'; 
		if i%2==0: return 'C'; 
		else: return 'B'
	else:
		if i%3==0: return 'A'; 
		if i%2==0: return 'B';
		else: return 'C'
for n in range(1,max+1):
	for i in range(0, 2**(max-n)): moves[2**(n-1) + (2**n)*(i)] = str(n)+ABC(max,n,i)
for i in range(1,2**max): print moves[i],
