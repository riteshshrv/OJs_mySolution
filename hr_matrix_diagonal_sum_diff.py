n=int(input())
m=[[None for x in range(n)] for x in range(n)]
j=n-1
lsum,rsum=0,0
for i in range(n):
    m[i]=[int(x) for x in input().split()]
    lsum+=m[i][i]
    rsum+=m[i][j]
    j-=1
print(abs(lsum-rsum))

