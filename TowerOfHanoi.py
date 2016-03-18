

def moveNum(max):
	moves = {}
	for n in range(1,max+1): # n = piece no.
		maxPiece = 2**(max-n)
		for i in range(0, maxPiece):
			moves[2**(n-1) + (2**n)*(i)] = n
	return moves
	
def isEven(num):
	if num%2 == 0:
		iseven = True
	else:
		iseven = False
	return iseven
	
def ABC(xor, count):
	if xor == False: #-C
		if count == 1:
			abc= 'C'
		elif count == 2:
			abc= 'B'
		elif count == 3:
			abc= 'A'
			count = 0
		else:
			print "error"
	if xor == True: #+B
		if count == 1:
			abc= 'B'
		elif count == 2:
			abc= 'C'
		elif count == 3:
			abc= 'A'
			count = 0
		else:
			print "error"
	return abc,count

def alpha(moves, max):
	turn =  2 ** max - 1

	counter = {}
	for i in range(1, turn+1):
		if moves[i] in counter:
			counter[moves[i]] += 1
		else:
			counter[moves[i]] = 1
		abc, counter[moves[i]] = ABC(isEven(max)^isEven(moves[i]),counter[moves[i]])
		moves[i] = str(moves[i])+abc
	return moves

max = int(raw_input('No. of pieces:'))
moves = alpha(moveNum(max), max)
for i in range(1, 2**max):
	print moves[i],
