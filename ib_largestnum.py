def maxnum(n):
	length=len(str(max(n)))
	l=''.join(sorted((str(v) for v in n), reverse=True,
		key=lambda i: i*(length*2 // len(i))))
	l2=[x for x in l if not x==',']
	return ''.join(l2)

def my_maxnum(a):
	n=len(a)
	num=''
	for i in range(1,n):
		x=''.join([a[i-1],a[i]])
		y=''.join([a[i],a[i-1]])
		num+=(x if (int(x)>int(y)) else y)
	return ''.join(num)
	# l=sorted(a,reverse=True)
	# return l

s=[str(x) for x in input().split(',')]
print(my_maxnum(s))
#[3, 30, 34, 5, 9]