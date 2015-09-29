def sqr(x):
	if x<0:
		return -1
	elif (x==0 or x==1):
		return x
	lb=1
	ub=x
	r=lb+(ub-lb)//2
	while(r>x/r or r+1<=x/(r+1)):
		if (r>x/r):
			ub=r
		else:
			lb=r
		r=lb+(ub-lb)//2
	return int(r)
# 		precision=3
# 		if x>0:
# 			low=0
# 			high=max(x,1)
# 			counter=0
# 			guess=(low+high)/2.0
# 			while abs(guess**2 -x)> precisionand counter<=100:
# 				if (guess**2<x):
# 					low=guess
# 				else:
# 					high=guess
# 				guess=(low+high)/2.0
# 				counter+=1
# 			assert counter<=100
# 			return guess