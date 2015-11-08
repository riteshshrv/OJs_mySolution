'''Codeforce: http://codeforces.com/contest/595/problem/A'''\

n,m=[int(x) for x in input().split()]
a=[[int(x) for x in input().split()] for x in range(n)]
c=0
for i in range(n):
	for j in range(0,2*m,2):
		if a[i][j]==1 or a[i][j+1]==1:
			c+=1
print(c)
