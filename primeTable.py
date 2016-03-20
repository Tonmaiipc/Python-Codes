max = int(raw_input())

def primer(num,row):
	prime = None
	for i in range(0,max):
		a,b = row[i]
		if a%num == 0 and b == 0: 
			b = 1
			row[i] = (a,b)
			prime = num
		else: continue
	return row, prime

row = [(i,0) for i in range(1,max+1)]
primes = []
for ele in range(2,max+1):
	row, prime = primer(ele,row)
	if prime != None: 
		primes.append(prime)
		for ele in primes: 
			if ele != primes[-1]: print ele,
			else: print ele
		for i in range(0,max/10+1):
			if row[10*i:10*i+10] != []:
				print row[10*i:10*i+10] 
		
