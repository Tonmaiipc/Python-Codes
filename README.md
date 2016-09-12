## Tower of Hanoi Note

2: 1B 2C 1C

3: 1C 2B 1B 3C 1A 2C 1C

4: 1B 2C 1C 3B 1A 2B 1B 4C 1C 2A 1A 3C 1B 2C 1C

5: 1C 2B 1B 3C 1A 2C 1C 4B 1B 2A 1A 3B 1C 2B 1B 5C 1A 2C 1C 3A 1B 2A 1A 4C 1C 2B 1B 3C 1A 2C 1C

2: 1  2  1

3: 1  2  1  3  1  2  1

4: 1  2  1  3  1  2  1  4  1  2  1  3  1  2  1

5: 1  2  1  3  1  2  1  4  1  2  1  3  1  2  1  5  1  2  1  3  1  2  1  4  1  2  1  3  1  2  1

6: 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 5 1 2 1 

2: 1 2 1

3: 1 2 1 3 1 2 1

4: 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1

5: 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 5 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
# this describe the nth disc that's used on the move

2: B C C

3: C B B C A C C

4: B C C B A B B C C A A C B C C

5: C B B C A C C B B A A B C B B C A C C A B A A C C B B C A C C
# this describe the destiny of the nth disc move

even odd = +B

even even = -C

odd odd = -C

odd even = +B

total move = 2^(m-1)

total number of 1 piece = 2^(max-n) ; max = max pieces, n= piece no.

1: 1,3,5,7  (2^0+2*i)

2: 2,6,10,14 (2^1+2^2*i)

3: 4,12,20,28 (2^2+2^3*i)

4: 8,24,40,56 (2^3+2^4*i)

5: 16,48,80,112 (+32)

ith position of n in all moves = 2^(n-1) + 2^n * i  ; i = ith position in n. 
(the move of the nth disc appear after every 2^n. when multiplied by i, the result is the next number of move that requires the nth disc)

# position of the nth disc in the serial of moves (above)
# notice that for each discs, it moves in either B->C->A or C->B->A fashion
