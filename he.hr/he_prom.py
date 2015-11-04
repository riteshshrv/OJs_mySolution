for t in range(int(input())):
	m,n=[int(x) for x in input().split()]
	bh=[int (x) for x in input().split()]
	gh=[int (x) for x in input().split()]
	bh.sort()
	gh.sort()
	if bh[0]<gh[0]:
		print("NO")
	else:
		for i in range(m):try:
				if bh[i]>gh[i]:
					del bh[0]
					del gh[0]
			except:
				break
		print ("YES")