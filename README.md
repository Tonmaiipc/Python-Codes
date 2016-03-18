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

2: B C C

3: C B B C A C C

4: B C C B A B B C C A A C B C C

5: C B B C A C C B B A A B C B B C A C C A B A A C C B B C A C C

even odd = +B
even even = -C
odd odd = -C
odd even = +B

total move = 2^(m-1)
total number of 1 piece = 2^(max-n) ; max = max pieces, n= piece no.

1: 1,3,5,7  (2^0+2n)
2: 2,6,10,14 (2^1+2^2n)
3: 4,12,20,28 (2^2+2^3n)
4: 8,24,40,56 (2^3+2^4n)
5: 16,48,80,112 (+32)

ith position of n in all moves = 2^(n-1) + 2^n * i  ; i = ith position in n
