'''Hackerearth: Number Theory 1: The Magical Shop'''

a,b=[int(x) for x in raw_input().split()]
c=raw_input()
z=0
for i in range(len(c)):
	if int(c[i]):
		z=((z%b)+(a%b))%b
		a=((a%b)*(a%b))%b
print (z%b)