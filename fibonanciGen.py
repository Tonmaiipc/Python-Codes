def fibo(n,m):
	if n-2 <=0:
		if m != 0 : print 1, 1,
		return 1
	else:
		sum = fibo(n-1,m) + fibo(n-2,m*0)
		if m != 0 : print sum,
		return sum

n = int(raw_input())
fibo(n,1)
