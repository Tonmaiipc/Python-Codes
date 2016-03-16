num = int(raw_input())
lis = [ int(i) for i in raw_input().split()]

def logic(a,b):
	if a > b:
		return b, a, 1
	else:
		return a, b, 0

def run(lis):
	for i in range(0,num-1):
		a,b, c = logic(lis[i],lis[i+1])
		lis[i] = a; lis[i+1] = b
		global set
		set += c
		print lis
	
handle = True
while handle == True:
	set = 0
	run(lis)
	if set == 0:
		break
